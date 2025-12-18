package com.bumptech.glide.load.model;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.core.util.InterfaceC0801e;
import com.bumptech.glide.C3433j;
import com.bumptech.glide.load.C3581i;
import com.bumptech.glide.load.model.InterfaceC3627o;
import com.bumptech.glide.util.C3860j;
import com.bumptech.glide.util.pool.C3863a;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;

/* renamed from: com.bumptech.glide.load.model.s */
/* loaded from: classes.dex */
public final class C3635s {

    /* renamed from: e */
    public static final C3638c f9581e = new C3638c();

    /* renamed from: f */
    public static final C3636a f9582f = new C3636a();

    /* renamed from: a */
    public final ArrayList f9583a;

    /* renamed from: b */
    public final C3638c f9584b;

    /* renamed from: c */
    public final HashSet f9585c;

    /* renamed from: d */
    public final InterfaceC0801e<List<Throwable>> f9586d;

    /* renamed from: com.bumptech.glide.load.model.s$a */
    /* loaded from: classes.dex */
    public static class C3636a implements InterfaceC3627o<Object, Object> {
        @Override // com.bumptech.glide.load.model.InterfaceC3627o
        /* renamed from: a */
        public final boolean mo6574a(@NonNull Object obj) {
            return false;
        }

        @Override // com.bumptech.glide.load.model.InterfaceC3627o
        @Nullable
        /* renamed from: b */
        public final InterfaceC3627o.C3628a<Object> mo6573b(@NonNull Object obj, int i, int i2, @NonNull C3581i c3581i) {
            return null;
        }
    }

    /* renamed from: com.bumptech.glide.load.model.s$b */
    /* loaded from: classes.dex */
    public static class C3637b<Model, Data> {

        /* renamed from: a */
        public final Class<Model> f9587a;

        /* renamed from: b */
        public final Class<Data> f9588b;

        /* renamed from: c */
        public final InterfaceC3629p<? extends Model, ? extends Data> f9589c;

        public C3637b(@NonNull Class<Model> cls, @NonNull Class<Data> cls2, @NonNull InterfaceC3629p<? extends Model, ? extends Data> interfaceC3629p) {
            this.f9587a = cls;
            this.f9588b = cls2;
            this.f9589c = interfaceC3629p;
        }
    }

    /* renamed from: com.bumptech.glide.load.model.s$c */
    /* loaded from: classes.dex */
    public static class C3638c {
    }

    public C3635s(@NonNull C3863a.C3866c c3866c) {
        C3638c c3638c = f9581e;
        this.f9583a = new ArrayList();
        this.f9585c = new HashSet();
        this.f9586d = c3866c;
        this.f9584b = c3638c;
    }

    /* renamed from: a */
    public final synchronized <Model, Data> void m6587a(@NonNull Class<Model> cls, @NonNull Class<Data> cls2, @NonNull InterfaceC3629p<? extends Model, ? extends Data> interfaceC3629p) {
        C3637b c3637b = new C3637b(cls, cls2, interfaceC3629p);
        ArrayList arrayList = this.f9583a;
        arrayList.add(arrayList.size(), c3637b);
    }

    @NonNull
    /* renamed from: b */
    public final <Model, Data> InterfaceC3627o<Model, Data> m6586b(@NonNull C3637b<?, ?> c3637b) {
        InterfaceC3627o<Model, Data> interfaceC3627o = (InterfaceC3627o<Model, Data>) c3637b.f9589c.mo6572b(this);
        C3860j.m6404b(interfaceC3627o);
        return interfaceC3627o;
    }

    @NonNull
    /* renamed from: c */
    public final synchronized <Model, Data> InterfaceC3627o<Model, Data> m6585c(@NonNull Class<Model> cls, @NonNull Class<Data> cls2) {
        try {
            ArrayList arrayList = new ArrayList();
            Iterator it = this.f9583a.iterator();
            boolean z = false;
            while (true) {
                boolean z2 = true;
                if (!it.hasNext()) {
                    break;
                }
                C3637b<?, ?> c3637b = (C3637b) it.next();
                if (this.f9585c.contains(c3637b)) {
                    z = true;
                } else {
                    if (!c3637b.f9587a.isAssignableFrom(cls) || !c3637b.f9588b.isAssignableFrom(cls2)) {
                        z2 = false;
                    }
                    if (z2) {
                        this.f9585c.add(c3637b);
                        arrayList.add(m6586b(c3637b));
                        this.f9585c.remove(c3637b);
                    }
                }
            }
            if (arrayList.size() > 1) {
                C3638c c3638c = this.f9584b;
                InterfaceC0801e<List<Throwable>> interfaceC0801e = this.f9586d;
                c3638c.getClass();
                return new C3633r(arrayList, interfaceC0801e);
            } else if (arrayList.size() == 1) {
                return (InterfaceC3627o) arrayList.get(0);
            } else if (z) {
                return f9582f;
            } else {
                throw new C3433j.C3436c((Class<?>) cls, (Class<?>) cls2);
            }
        } catch (Throwable th) {
            this.f9585c.clear();
            throw th;
        }
    }

    @NonNull
    /* renamed from: d */
    public final synchronized ArrayList m6584d(@NonNull Class cls) {
        ArrayList arrayList;
        try {
            arrayList = new ArrayList();
            Iterator it = this.f9583a.iterator();
            while (it.hasNext()) {
                C3637b c3637b = (C3637b) it.next();
                if (!this.f9585c.contains(c3637b) && c3637b.f9587a.isAssignableFrom(cls)) {
                    this.f9585c.add(c3637b);
                    InterfaceC3627o mo6572b = c3637b.f9589c.mo6572b(this);
                    C3860j.m6404b(mo6572b);
                    arrayList.add(mo6572b);
                    this.f9585c.remove(c3637b);
                }
            }
        } catch (Throwable th) {
            this.f9585c.clear();
            throw th;
        }
        return arrayList;
    }

    @NonNull
    /* renamed from: e */
    public final synchronized ArrayList m6583e(@NonNull Class cls) {
        ArrayList arrayList;
        arrayList = new ArrayList();
        Iterator it = this.f9583a.iterator();
        while (it.hasNext()) {
            C3637b c3637b = (C3637b) it.next();
            if (!arrayList.contains(c3637b.f9588b) && c3637b.f9587a.isAssignableFrom(cls)) {
                arrayList.add(c3637b.f9588b);
            }
        }
        return arrayList;
    }
}
