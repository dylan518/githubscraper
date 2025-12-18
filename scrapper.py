import os
import sys
import subprocess
import tempfile
from collections import defaultdict
from itertools import islice
import hashlib
from pathlib import Path
import time
import random
import threading

from datasets import load_dataset
from dotenv import load_dotenv
from tqdm import tqdm
import duckdb

# ----------------------------
# Load .env
# ----------------------------
load_dotenv()

HF_TOKEN = (
    os.getenv("HF_TOKEN")
    or os.getenv("HUGGINGFACE_TOKEN")
    or os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
if not HF_TOKEN:
    print(
        "[WARN] No HF token found in environment (.env). Proceeding unauthenticated.",
        file=sys.stderr,
    )

MAX_REPOS = int(os.getenv("MAX_REPOS", 5))
MAX_FILES_PER_REPO = int(os.getenv("MAX_FILES_PER_REPO", 5))

DATASET = "nvidia/Nemotron-Pretraining-Code-v2"
CONFIG = os.getenv("DATASET_CONFIG", "Nemotron-Code-Metadata")
SPLIT = "train"
DB_PATH = os.getenv("DB_PATH", os.path.join("data", "index.duckdb"))
BLOB_DIR = os.getenv("BLOB_DIR", os.path.join("data", "blobs"))
CONCURRENCY = int(os.getenv("CONCURRENCY", 8))
RETRY_LIMIT = int(os.getenv("RETRY_LIMIT", 5))
BACKOFF_BASE_SECONDS = float(os.getenv("BACKOFF_BASE_SECONDS", 2.0))
BACKOFF_MAX_SECONDS = float(os.getenv("BACKOFF_MAX_SECONDS", 60.0))
MAX_RECORDS = os.getenv("MAX_RECORDS")  # optional cap on streamed records
MAX_RECORDS = int(MAX_RECORDS) if MAX_RECORDS not in (None, "", "None") else None
LOG_EVERY_N = int(os.getenv("LOG_EVERY_N", 25))
VERBOSE = os.getenv("VERBOSE", "0") == "1"
LOG_META_EVERY_N = int(os.getenv("LOG_META_EVERY_N", 500))
META_SCAN_LIMIT = int(os.getenv("META_SCAN_LIMIT", 5000))
GIT_CMD_TIMEOUT = float(os.getenv("GIT_CMD_TIMEOUT", 180.0))

# Reduce noisy external progress bars when not verbose
if not VERBOSE:
    os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
    os.environ.setdefault("HF_DATASETS_DISABLE_PROGRESS_BAR", "1")

# ----------------------------
# Helpers
# ----------------------------
def run(cmd, cwd=None):
    return subprocess.run(
        cmd,
        cwd=cwd,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

def _is_rate_limited(stderr_text):
    if not stderr_text:
        return None
    txt = stderr_text.lower()
    patterns = [
        "rate limit",  # generic
        "http 429",
        "api rate limit exceeded",
        "secondary rate limit",
        "you have exceeded",
        "abuse detection",
    ]
    for p in patterns:
        if p in txt:
            return p
    return None

def run_with_retries(cmd, cwd=None, retries=RETRY_LIMIT):
    attempt = 0
    start_ts = time.time()
    while True:
        try:
            if VERBOSE:
                print(f"[CMD] {' '.join(cmd)} cwd={cwd or os.getcwd()}", flush=True)
            t0 = time.time()
            cp = subprocess.run(
                cmd,
                cwd=cwd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
                timeout=GIT_CMD_TIMEOUT,
            )
            if VERBOSE:
                dt = time.time() - t0
                print(f"[OK ] {' '.join(cmd)} took {dt:.2f}s", flush=True)
            return cp
        except subprocess.TimeoutExpired:
            attempt += 1
            reason = "timeout"
            backoff = min(BACKOFF_MAX_SECONDS, BACKOFF_BASE_SECONDS * (2 ** (attempt - 1)))
            sleep_s = random.uniform(backoff / 2, backoff)
            record_retry(source="git", repo=None, commit=None, cmd=cmd, reason=reason, stderr_text=None, backoff_seconds=sleep_s)
            if attempt > retries:
                raise
            if VERBOSE:
                total_dt = time.time() - start_ts
                print(f"[RETRY] {' '.join(cmd)} reason={reason} sleep={sleep_s:.2f}s attempt={attempt}/{retries} elapsed={total_dt:.1f}s", flush=True)
            time.sleep(sleep_s)
        except subprocess.CalledProcessError as e:
            attempt += 1
            stderr_text = e.stderr.decode("utf-8", "ignore") if e.stderr else ""
            rl = _is_rate_limited(stderr_text)
            reason = rl or "transient"
            backoff = min(BACKOFF_MAX_SECONDS, BACKOFF_BASE_SECONDS * (2 ** (attempt - 1)))
            # Full jitter
            sleep_s = random.uniform(backoff / 2, backoff)
            if rl:
                record_rate_limit(source="git", repo=None, commit=None, message=rl, backoff_seconds=sleep_s)
            else:
                record_retry(source="git", repo=None, commit=None, cmd=cmd, reason=reason, stderr_text=stderr_text, backoff_seconds=sleep_s)
            if attempt > retries:
                raise
            if VERBOSE:
                total_dt = time.time() - start_ts
                print(f"[RETRY] {' '.join(cmd)} reason={reason} sleep={sleep_s:.2f}s attempt={attempt}/{retries} elapsed={total_dt:.1f}s", flush=True)
            time.sleep(sleep_s)

def _resolve_commit_in_repo(repo_dir, commit_prefix):
    """
    Try to resolve a short commit prefix to a full SHA using local refs.
    Returns full SHA or None.
    """
    try:
        # Fast path: rev-parse may expand unique prefix if known
        cp = run_with_retries(["git", "rev-parse", "--verify", f"{commit_prefix}"], cwd=repo_dir)
        full = cp.stdout.decode("utf-8", "ignore").strip()
        if full:
            return full
    except Exception:
        pass
    try:
        # Fallback: scan all commits reachable from all refs (metadata only, no blobs)
        cp = run_with_retries(["git", "rev-list", "--all"], cwd=repo_dir)
        lines = [l.strip() for l in cp.stdout.decode("utf-8", "ignore").splitlines() if l.strip()]
        matches = [sha for sha in lines if sha.startswith(commit_prefix)]
        if len(matches) == 1:
            return matches[0]
    except Exception:
        pass
    return None

def safe_git_fetch(repo_url, commit, paths):
    """
    Conservative fetch: metadata-only (no blobs), resolve commit locally, then
    read specific file blobs via 'git show <commit>:<path>'.
    """
    with tempfile.TemporaryDirectory() as td:
        run_with_retries(["git", "init"], cwd=td)
        run_with_retries(["git", "remote", "add", "origin", repo_url], cwd=td)
        # Fetch refs metadata only (no blobs), without depth so the target commit
        # is reachable from some advertised ref.
        try:
            run_with_retries(
                ["git", "fetch", "--filter=blob:none", "--tags", "--prune", "origin"],
                cwd=td,
            )
        except subprocess.CalledProcessError as e:
            stderr_text = e.stderr.decode("utf-8", "ignore") if e.stderr else ""
            print(f"[WARN] fetch-refs failed {repo_url}@{commit} -> {stderr_text}", flush=True)
            record_failure(
                source="git",
                repo=repo_url,
                commit=commit,
                path=None,
                stage="fetch_refs",
                message=str(e),
                stderr_text=stderr_text,
            )
            raise
        resolved = _resolve_commit_in_repo(td, commit)
        if not resolved:
            msg = f"Could not resolve commit prefix {commit} in {repo_url}"
            print(f"[WARN] {msg}", flush=True)
            record_failure(
                source="git",
                repo=repo_url,
                commit=commit,
                path=None,
                stage="resolve_commit",
                message=msg,
                stderr_text=None,
            )
            raise RuntimeError(msg)

        contents = {}
        for p in paths:
            try:
                cp = run_with_retries(["git", "show", f"{resolved}:{p}"], cwd=td)
                contents[p] = cp.stdout.decode("utf-8", "ignore")
            except subprocess.CalledProcessError as e:
                err = e.stderr.decode("utf-8", "ignore") if e.stderr else str(e)
                print(f"[WARN] show failed {repo_url}@{resolved}:{p} -> {err}", flush=True)
                record_failure(
                    source="git",
                    repo=repo_url,
                    commit=resolved,
                    path=p,
                    stage="show",
                    message=str(e),
                    stderr_text=err,
                )
        return contents

def ensure_output_dirs():
    Path(BLOB_DIR).mkdir(parents=True, exist_ok=True)
    Path(os.path.dirname(DB_PATH)).mkdir(parents=True, exist_ok=True)

def write_blob_and_get_info(text):
    """
    Content-addressed storage:
    data/blobs/ab/abcdef...123.txt where 'ab' are the first 2 hex chars of sha256.
    Returns (sha256_hex, blob_rel_path).
    """
    text_bytes = text.encode("utf-8", "ignore")
    sha256_hex = hashlib.sha256(text_bytes).hexdigest()
    subdir = os.path.join(BLOB_DIR, sha256_hex[:2])
    Path(subdir).mkdir(parents=True, exist_ok=True)
    blob_abs_path = os.path.join(subdir, f"{sha256_hex}.txt")
    if not os.path.exists(blob_abs_path):
        with open(blob_abs_path, "wb") as f:
            f.write(text_bytes)
    blob_rel_path = os.path.relpath(blob_abs_path, start=os.getcwd())
    return sha256_hex, blob_rel_path

def get_db_connection():
    ensure_output_dirs()
    conn = duckdb.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS files (
            repo TEXT,
            commit TEXT,
            path TEXT,
            sha256 TEXT,
            n_chars BIGINT,
            blob_rel_path TEXT,
            created_at TIMESTAMP DEFAULT now()
        );
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS rate_limits (
            source TEXT,
            repo TEXT,
            commit TEXT,
            message TEXT,
            backoff_seconds DOUBLE,
            created_at TIMESTAMP DEFAULT now()
        );
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS retries (
            source TEXT,
            repo TEXT,
            commit TEXT,
            cmd TEXT,
            reason TEXT,
            stderr TEXT,
            backoff_seconds DOUBLE,
            created_at TIMESTAMP DEFAULT now()
        );
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS failures (
            source TEXT,
            repo TEXT,
            commit TEXT,
            path TEXT,
            stage TEXT,
            message TEXT,
            stderr TEXT,
            created_at TIMESTAMP DEFAULT now()
        );
        """
    )
    return conn
db_lock = threading.Lock()

def record_rate_limit(source, repo, commit, message, backoff_seconds):
    try:
        conn = duckdb.connect(DB_PATH)
        conn.execute(
            """
            INSERT INTO rate_limits (source, repo, commit, message, backoff_seconds)
            VALUES (?, ?, ?, ?, ?)
            """,
            (source, repo, commit, str(message) if message else None, float(backoff_seconds)),
        )
        conn.close()
    except Exception:
        # best-effort logging; avoid crashing on telemetry
        pass

def record_retry(source, repo, commit, cmd, reason, stderr_text, backoff_seconds):
    try:
        conn = duckdb.connect(DB_PATH)
        conn.execute(
            """
            INSERT INTO retries (source, repo, commit, cmd, reason, stderr, backoff_seconds)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (source, repo, commit, " ".join(cmd) if isinstance(cmd, (list, tuple)) else str(cmd),
             str(reason) if reason else None, stderr_text, float(backoff_seconds)),
        )
        conn.close()
    except Exception:
        # best-effort logging
        pass

def record_failure(source, repo, commit, path, stage, message, stderr_text):
    try:
        conn = duckdb.connect(DB_PATH)
        conn.execute(
            """
            INSERT INTO failures (source, repo, commit, path, stage, message, stderr)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (source, repo, commit, path, stage, str(message) if message else None, stderr_text),
        )
        conn.close()
    except Exception:
        # best-effort logging
        pass

# ----------------------------
# Metadata → repo resolver
# ----------------------------
def record_to_repo_url(rec):
    """
    You must provide this mapping.
    If your internal copy already has repo_url, use it directly.
    """
    def first_non_empty(keys):
        for k in keys:
            v = rec.get(k)
            if v:
                return v
        return None

    raw = first_non_empty(
        [
            "repo_url",
            "repo",
            "repo_name",
            "url",
            "github_url",
            "github_repo",
            "repository",
            "repo_html_url",
        ]
    )
    if not raw:
        return None
    raw = str(raw).strip()
    # Normalize "owner/repo" to https clone URL
    if raw.startswith("http://") or raw.startswith("https://") or raw.startswith("git@"):
        return raw
    if "/" in raw and " " not in raw and not raw.endswith(".git"):
        return f"https://github.com/{raw}.git"
    return raw

def record_to_commit(rec):
    for k in ["commit_id", "commit", "sha", "commit_sha", "git_commit"]:
        v = rec.get(k)
        if v:
            return str(v).strip()
    return None

def record_to_rel_path(rec):
    for k in ["rel_path", "path", "filepath", "file_path"]:
        v = rec.get(k)
        if v:
            return str(v).strip()
    return None

# ----------------------------
# Stream NVIDIA metadata
# ----------------------------
load_kwargs = {
    "split": SPLIT,
    "streaming": True,
}
if HF_TOKEN:
    load_kwargs["token"] = HF_TOKEN

ds = load_dataset(DATASET, CONFIG, **load_kwargs)

groups = defaultdict(list)

def planned_files_count(groups_dict):
    return sum(min(len(paths), MAX_FILES_PER_REPO) for _, paths in groups_dict.items())

stream_iter = islice(ds, 0, MAX_RECORDS) if MAX_RECORDS else ds
records_seen = 0
first_keys_samples = []
target_files = MAX_REPOS * MAX_FILES_PER_REPO
for rec in stream_iter:
    records_seen += 1
    if len(first_keys_samples) < 5:
        try:
            first_keys_samples.append(sorted(list(rec.keys())))
        except Exception:
            pass

    repo = record_to_repo_url(rec)
    commit = record_to_commit(rec)
    path = record_to_rel_path(rec)
    if not (repo and commit and path):
        continue

    key = (repo, commit)
    # Only accept new groups until MAX_REPOS reached
    if key not in groups:
        if len(groups) < MAX_REPOS:
            groups[key] = [path]
        else:
            # We've hit the repo cap; skip new groups but keep filling existing ones
            pass
    else:
        # Fill up to MAX_FILES_PER_REPO per group, avoid duplicates
        if len(groups[key]) < MAX_FILES_PER_REPO and path not in groups[key]:
            groups[key].append(path)

    if VERBOSE and LOG_META_EVERY_N > 0 and records_seen % LOG_META_EVERY_N == 0:
        print(
            f"[DISCOVERY] records={records_seen} groups={len(groups)} planned_files={planned_files_count(groups)}/{target_files}",
            flush=True,
        )

    # Stop when we've planned enough files or reached meta scan limit with nothing found
    if planned_files_count(groups) >= target_files:
        break
    if META_SCAN_LIMIT and records_seen >= META_SCAN_LIMIT and len(groups) == 0:
        print(
            f"[WARN] Scanned {records_seen} records but found no usable repo/commit/path fields. "
            f"First record keys samples: {first_keys_samples}",
            flush=True,
        )
        break

# ----------------------------
# Fetch a lot of files concurrently and persist
# ----------------------------
conn = get_db_connection()
insert_if_missing_stmt = """
INSERT INTO files (repo, commit, path, sha256, n_chars, blob_rel_path)
SELECT ?, ?, ?, ?, ?, ?
WHERE NOT EXISTS (
    SELECT 1 FROM files WHERE repo = ? AND commit = ? AND path = ?
)
"""
num_written = 0
sample_rows = []

planned_files = sum(min(len(paths), MAX_FILES_PER_REPO) for _, paths in groups.items())
if VERBOSE:
    print(f"[INFO] Planned to fetch {planned_files} files across {len(groups)} repos")

files_counter_lock = threading.Lock()
files_counter = [0]  # mutable single-element container for cross-thread updates

def _bump_and_log():
    with files_counter_lock:
        files_counter[0] += 1
        c = files_counter[0]
    if VERBOSE and LOG_EVERY_N > 0 and c % LOG_EVERY_N == 0:
        print(f"[PROGRESS] files={c}/{planned_files}", flush=True)
    return c

def process_group(item, pbar):
    (repo, commit), paths = item
    try:
        selected = paths[:MAX_FILES_PER_REPO]
        if VERBOSE:
            print(f"[INFO] Fetching up to {len(selected)} files from {repo}@{commit}", flush=True)
        blobs = safe_git_fetch(repo, commit, selected)
        local_written = 0
        local_samples = []
        # open a per-thread connection to avoid sharing a connection across threads
        tconn = duckdb.connect(DB_PATH)
        for p, txt in blobs.items():
            sha256_hex, blob_rel_path = write_blob_and_get_info(txt)
            n_chars = len(txt)
            tconn.execute(
                insert_if_missing_stmt,
                (repo, commit, p, sha256_hex, n_chars, blob_rel_path, repo, commit, p),
            )
            local_written += 1
            try:
                pbar.update(1)
            except Exception:
                pass
            total_so_far = _bump_and_log()
            if VERBOSE:
                print(f"[SAVED #{total_so_far}] {repo}@{commit}:{p} -> {blob_rel_path} ({n_chars} chars)", flush=True)
            if len(local_samples) < 3:
                local_samples.append(
                    {
                        "repo": repo,
                        "commit": commit,
                        "path": p,
                        "n_chars": n_chars,
                        "sha256": sha256_hex,
                        "blob": blob_rel_path,
                    }
                )
        tconn.close()
        return local_written, local_samples, None
    except Exception as e:
        msg = str(e)
        if _is_rate_limited(msg):
            record_rate_limit(source="git", repo=repo, commit=commit, message=msg, backoff_seconds=0.0)
        return 0, [], f"[WARN] {repo}@{commit}: {msg}"

from concurrent.futures import ThreadPoolExecutor, as_completed

with tqdm(total=planned_files, desc="Files", position=0, disable=not VERBOSE) as files_pbar:
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as ex:
        futures = [ex.submit(process_group, item, files_pbar) for item in groups.items()]
        for fut in tqdm(as_completed(futures), total=len(futures), desc="Persisting", position=1, disable=not VERBOSE):
            w, samples, warn = fut.result()
            num_written += w
            if warn:
                print(warn)
            for s in samples:
                if len(sample_rows) < 10:
                    sample_rows.append(s)

if VERBOSE and sample_rows:
    print("\nSaved samples:")
    for r in sample_rows:
        print(r)
print(f"\n[OK] Wrote {num_written} file records")
print(f"[OK] Files scraped total: {files_counter[0]} / planned {planned_files}")
print(f"[OK] DuckDB index: {os.path.relpath(DB_PATH, start=os.getcwd())}")
print(f"[OK] Blob store:   {os.path.relpath(BLOB_DIR, start=os.getcwd())}")
rate_counts = conn.execute("SELECT COUNT(*) FROM rate_limits").fetchone()[0]
if rate_counts:
    print(f"[INFO] Rate limit events recorded: {rate_counts}")
    top_msgs = conn.execute("""
        SELECT message, COUNT(*) c
        FROM rate_limits
        GROUP BY 1
        ORDER BY c DESC
        LIMIT 5
    """).fetchall()
    for msg, c in top_msgs:
        print(f"  - {c}x: {msg}")
retry_counts = conn.execute("SELECT COUNT(*) FROM retries").fetchone()[0]
if retry_counts:
    print(f"[INFO] Retry events (non-rate-limit) recorded: {retry_counts}")
    top_retry = conn.execute("""
        SELECT reason, COUNT(*) c
        FROM retries
        GROUP BY 1
        ORDER BY c DESC
        LIMIT 5
    """).fetchall()
    for reason, c in top_retry:
        print(f"  - {c}x: {reason}")
fail_counts = conn.execute("SELECT COUNT(*) FROM failures").fetchone()[0]
if fail_counts:
    print(f"[INFO] Failure events recorded: {fail_counts}")
    top_fail = conn.execute("""
        SELECT stage, substr(coalesce(stderr, message), 1, 100) snippet, COUNT(*) c
        FROM failures
        GROUP BY 1, 2
        ORDER BY c DESC
        LIMIT 5
    """).fetchall()
    for stage, snippet, c in top_fail:
        print(f"  - {c}x {stage}: {snippet}")
