package defpackage;

/* JADX INFO: Access modifiers changed from: package-private */
/* renamed from: bnb  reason: default package */
/* loaded from: classes2.dex */
public final class bnb implements Runnable {
    private final /* synthetic */ String a;
    private final /* synthetic */ long b;
    private final /* synthetic */ bkz c;

    /* JADX INFO: Access modifiers changed from: package-private */
    public bnb(bkz bkzVar, String str, long j) {
        this.c = bkzVar;
        this.a = str;
        this.b = j;
    }

    @Override // java.lang.Runnable
    public final void run() {
        bkz bkzVar = this.c;
        String str = this.a;
        long j = this.b;
        bkzVar.c();
        aat.a(str);
        if (bkzVar.b.isEmpty()) {
            bkzVar.c = j;
        }
        Integer num = bkzVar.b.get(str);
        if (num != null) {
            bkzVar.b.put(str, Integer.valueOf(num.intValue() + 1));
        } else if (bkzVar.b.size() >= 100) {
            bkzVar.q().f.a("Too many ads visible");
        } else {
            bkzVar.b.put(str, 1);
            bkzVar.a.put(str, Long.valueOf(j));
        }
    }
}
