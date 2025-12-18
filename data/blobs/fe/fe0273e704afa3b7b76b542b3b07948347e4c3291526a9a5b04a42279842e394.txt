package androidx.window.layout;

import fk.p;
import java.util.List;
import rk.l;
import sk.j;

/* compiled from: WindowLayoutInfo.kt */
public final class z {

    /* renamed from: a  reason: collision with root package name */
    public final List<c> f3722a;

    public z(List<? extends c> list) {
        this.f3722a = list;
    }

    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || !j.a(z.class, obj.getClass())) {
            return false;
        }
        return j.a(this.f3722a, ((z) obj).f3722a);
    }

    public final int hashCode() {
        return this.f3722a.hashCode();
    }

    public final String toString() {
        return p.Q0(this.f3722a, ", ", "WindowLayoutInfo{ DisplayFeatures[", "] }", (l) null, 56);
    }
}
