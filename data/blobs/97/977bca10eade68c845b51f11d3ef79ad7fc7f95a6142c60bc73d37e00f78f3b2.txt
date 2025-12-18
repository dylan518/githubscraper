package defpackage;

import java.io.IOException;
import java.io.InterruptedIOException;
import java.util.concurrent.TimeUnit;

/* loaded from: classes2.dex */
public class xg extends d93 {
    public static final tg Companion = new tg();
    private static final long IDLE_TIMEOUT_MILLIS;
    private static final long IDLE_TIMEOUT_NANOS;
    private static final int TIMEOUT_WRITE_SIZE = 65536;
    private static xg head;
    private boolean inQueue;
    private xg next;
    private long timeoutAt;

    static {
        long millis = TimeUnit.SECONDS.toMillis(60L);
        IDLE_TIMEOUT_MILLIS = millis;
        IDLE_TIMEOUT_NANOS = TimeUnit.MILLISECONDS.toNanos(millis);
    }

    public static final long access$remainingNanos(xg xgVar, long j) {
        return xgVar.timeoutAt - j;
    }

    public final IOException access$newTimeoutException(IOException iOException) {
        return newTimeoutException(iOException);
    }

    public final void enter() {
        long timeoutNanos = timeoutNanos();
        boolean hasDeadline = hasDeadline();
        if (timeoutNanos == 0 && !hasDeadline) {
            return;
        }
        Companion.getClass();
        synchronized (xg.class) {
            if (!this.inQueue) {
                this.inQueue = true;
                if (head == null) {
                    head = new xg();
                    new ug().start();
                }
                long nanoTime = System.nanoTime();
                if (timeoutNanos != 0 && hasDeadline) {
                    this.timeoutAt = Math.min(timeoutNanos, deadlineNanoTime() - nanoTime) + nanoTime;
                } else if (timeoutNanos != 0) {
                    this.timeoutAt = timeoutNanos + nanoTime;
                } else if (hasDeadline) {
                    this.timeoutAt = deadlineNanoTime();
                } else {
                    throw new AssertionError();
                }
                long access$remainingNanos = access$remainingNanos(this, nanoTime);
                xg xgVar = head;
                while (xgVar.next != null && access$remainingNanos >= access$remainingNanos(xgVar.next, nanoTime)) {
                    xgVar = xgVar.next;
                }
                this.next = xgVar.next;
                xgVar.next = this;
                if (xgVar == head) {
                    xg.class.notify();
                }
            } else {
                throw new IllegalStateException("Unbalanced enter/exit".toString());
            }
        }
    }

    public final boolean exit() {
        Companion.getClass();
        synchronized (xg.class) {
            if (this.inQueue) {
                this.inQueue = false;
                for (xg xgVar = head; xgVar != null; xgVar = xgVar.next) {
                    if (xgVar.next == this) {
                        xgVar.next = this.next;
                        this.next = null;
                        return false;
                    }
                }
                return true;
            }
            return false;
        }
    }

    public IOException newTimeoutException(IOException iOException) {
        InterruptedIOException interruptedIOException = new InterruptedIOException("timeout");
        if (iOException != null) {
            interruptedIOException.initCause(iOException);
        }
        return interruptedIOException;
    }

    public final dw2 sink(dw2 dw2Var) {
        return new vg(this, dw2Var);
    }

    public final mx2 source(mx2 mx2Var) {
        return new wg(this, mx2Var);
    }

    public void timedOut() {
    }

    public final <T> T withTimeout(v31 v31Var) {
        enter();
        try {
            T t = (T) v31Var.invoke();
            if (!exit()) {
                return t;
            }
            throw access$newTimeoutException(null);
        } catch (IOException e) {
            if (!exit()) {
                throw e;
            }
            throw access$newTimeoutException(e);
        } finally {
            exit();
        }
    }
}
