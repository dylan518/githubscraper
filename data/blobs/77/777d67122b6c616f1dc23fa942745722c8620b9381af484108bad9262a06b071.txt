package p029e1;

import java.io.Serializable;
import p029e1.C1523g;
import p077m1.C1910p;
import p083n1.C2422g;
import p083n1.C2423h;

/* renamed from: e1.c */
public final class C1516c implements C1523g, Serializable {

    /* renamed from: d */
    private final C1523g f6164d;

    /* renamed from: e */
    private final C1523g.C1526b f6165e;

    /* renamed from: e1.c$a */
    static final class C1517a extends C2423h implements C1910p<String, C1523g.C1526b, String> {

        /* renamed from: e */
        public static final C1517a f6166e = new C1517a();

        C1517a() {
            super(2);
        }

        /* renamed from: a */
        public final String mo3751g(String str, C1523g.C1526b bVar) {
            C2422g.m10285e(str, "acc");
            C2422g.m10285e(bVar, "element");
            if (str.length() == 0) {
                return bVar.toString();
            }
            return str + ", " + bVar;
        }
    }

    public C1516c(C1523g gVar, C1523g.C1526b bVar) {
        C2422g.m10285e(gVar, "left");
        C2422g.m10285e(bVar, "element");
        this.f6164d = gVar;
        this.f6165e = bVar;
    }

    /* renamed from: c */
    private final boolean m6570c(C1523g.C1526b bVar) {
        return C2422g.m10281a(get(bVar.getKey()), bVar);
    }

    /* renamed from: e */
    private final boolean m6571e(C1516c cVar) {
        while (m6570c(cVar.f6165e)) {
            C1523g gVar = cVar.f6164d;
            if (gVar instanceof C1516c) {
                cVar = (C1516c) gVar;
            } else {
                C2422g.m10283c(gVar, "null cannot be cast to non-null type kotlin.coroutines.CoroutineContext.Element");
                return m6570c((C1523g.C1526b) gVar);
            }
        }
        return false;
    }

    /* renamed from: f */
    private final int m6572f() {
        int i = 2;
        C1516c cVar = this;
        while (true) {
            C1523g gVar = cVar.f6164d;
            cVar = gVar instanceof C1516c ? (C1516c) gVar : null;
            if (cVar == null) {
                return i;
            }
            i++;
        }
    }

    public boolean equals(Object obj) {
        if (this != obj) {
            if (obj instanceof C1516c) {
                C1516c cVar = (C1516c) obj;
                if (cVar.m6572f() != m6572f() || !cVar.m6571e(this)) {
                    return false;
                }
            }
            return false;
        }
        return true;
    }

    public <R> R fold(R r, C1910p<? super R, ? super C1523g.C1526b, ? extends R> pVar) {
        C2422g.m10285e(pVar, "operation");
        return pVar.mo3751g(this.f6164d.fold(r, pVar), this.f6165e);
    }

    public <E extends C1523g.C1526b> E get(C1523g.C1528c<E> cVar) {
        C2422g.m10285e(cVar, "key");
        C1516c cVar2 = this;
        while (true) {
            E e = cVar2.f6165e.get(cVar);
            if (e != null) {
                return e;
            }
            C1523g gVar = cVar2.f6164d;
            if (!(gVar instanceof C1516c)) {
                return gVar.get(cVar);
            }
            cVar2 = (C1516c) gVar;
        }
    }

    public int hashCode() {
        return this.f6164d.hashCode() + this.f6165e.hashCode();
    }

    public C1523g minusKey(C1523g.C1528c<?> cVar) {
        C2422g.m10285e(cVar, "key");
        if (this.f6165e.get(cVar) != null) {
            return this.f6164d;
        }
        C1523g minusKey = this.f6164d.minusKey(cVar);
        return minusKey == this.f6164d ? this : minusKey == C1529h.f6170d ? this.f6165e : new C1516c(minusKey, this.f6165e);
    }

    public C1523g plus(C1523g gVar) {
        return C1523g.C1524a.m6582a(this, gVar);
    }

    public String toString() {
        return '[' + ((String) fold("", C1517a.f6166e)) + ']';
    }
}
