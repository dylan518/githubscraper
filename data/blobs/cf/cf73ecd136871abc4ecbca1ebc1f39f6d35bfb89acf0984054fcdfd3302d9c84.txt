package androidx.fragment.app;

import android.annotation.SuppressLint;
import android.graphics.Rect;
import android.view.View;
import android.view.ViewGroup;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import p027c.p064i.p069g.C1849b;
import p027c.p064i.p072j.C1986r;
import p027c.p064i.p072j.C1988t;
import p027c.p064i.p072j.C2003v;

@SuppressLint({"UnknownNullness"})
/* renamed from: androidx.fragment.app.v */
public abstract class C1269v {

    /* renamed from: androidx.fragment.app.v$a */
    class C1270a implements Runnable {

        /* renamed from: f */
        final /* synthetic */ int f3665f;

        /* renamed from: o */
        final /* synthetic */ ArrayList f3666o;

        /* renamed from: p */
        final /* synthetic */ ArrayList f3667p;

        /* renamed from: q */
        final /* synthetic */ ArrayList f3668q;

        /* renamed from: r */
        final /* synthetic */ ArrayList f3669r;

        C1270a(int i, ArrayList arrayList, ArrayList arrayList2, ArrayList arrayList3, ArrayList arrayList4) {
            this.f3665f = i;
            this.f3666o = arrayList;
            this.f3667p = arrayList2;
            this.f3668q = arrayList3;
            this.f3669r = arrayList4;
        }

        public void run() {
            for (int i = 0; i < this.f3665f; i++) {
                C1988t.m8340D0((View) this.f3666o.get(i), (String) this.f3667p.get(i));
                C1988t.m8340D0((View) this.f3668q.get(i), (String) this.f3669r.get(i));
            }
        }
    }

    /* renamed from: androidx.fragment.app.v$b */
    class C1271b implements Runnable {

        /* renamed from: f */
        final /* synthetic */ ArrayList f3671f;

        /* renamed from: o */
        final /* synthetic */ Map f3672o;

        C1271b(ArrayList arrayList, Map map) {
            this.f3671f = arrayList;
            this.f3672o = map;
        }

        public void run() {
            int size = this.f3671f.size();
            for (int i = 0; i < size; i++) {
                View view = (View) this.f3671f.get(i);
                String H = C1988t.m8347H(view);
                if (H != null) {
                    C1988t.m8340D0(view, C1269v.m5224i(this.f3672o, H));
                }
            }
        }
    }

    /* renamed from: androidx.fragment.app.v$c */
    class C1272c implements Runnable {

        /* renamed from: f */
        final /* synthetic */ ArrayList f3674f;

        /* renamed from: o */
        final /* synthetic */ Map f3675o;

        C1272c(ArrayList arrayList, Map map) {
            this.f3674f = arrayList;
            this.f3675o = map;
        }

        public void run() {
            int size = this.f3674f.size();
            for (int i = 0; i < size; i++) {
                View view = (View) this.f3674f.get(i);
                C1988t.m8340D0(view, (String) this.f3675o.get(C1988t.m8347H(view)));
            }
        }
    }

    /* renamed from: d */
    protected static void m5222d(List<View> list, View view) {
        int size = list.size();
        if (!m5223h(list, view, size)) {
            list.add(view);
            for (int i = size; i < list.size(); i++) {
                View view2 = list.get(i);
                if (view2 instanceof ViewGroup) {
                    ViewGroup viewGroup = (ViewGroup) view2;
                    int childCount = viewGroup.getChildCount();
                    for (int i2 = 0; i2 < childCount; i2++) {
                        View childAt = viewGroup.getChildAt(i2);
                        if (!m5223h(list, childAt, size)) {
                            list.add(childAt);
                        }
                    }
                }
            }
        }
    }

    /* renamed from: h */
    private static boolean m5223h(List<View> list, View view, int i) {
        for (int i2 = 0; i2 < i; i2++) {
            if (list.get(i2) == view) {
                return true;
            }
        }
        return false;
    }

    /* renamed from: i */
    static String m5224i(Map<String, String> map, String str) {
        for (Map.Entry next : map.entrySet()) {
            if (str.equals(next.getValue())) {
                return (String) next.getKey();
            }
        }
        return null;
    }

    /* renamed from: l */
    protected static boolean m5225l(List list) {
        return list == null || list.isEmpty();
    }

    /* renamed from: A */
    public abstract void mo4260A(Object obj, ArrayList<View> arrayList, ArrayList<View> arrayList2);

    /* renamed from: B */
    public abstract Object mo4261B(Object obj);

    /* renamed from: a */
    public abstract void mo4262a(Object obj, View view);

    /* renamed from: b */
    public abstract void mo4263b(Object obj, ArrayList<View> arrayList);

    /* renamed from: c */
    public abstract void mo4264c(ViewGroup viewGroup, Object obj);

    /* renamed from: e */
    public abstract boolean mo4265e(Object obj);

    /* access modifiers changed from: package-private */
    /* renamed from: f */
    public void mo4294f(ArrayList<View> arrayList, View view) {
        if (view.getVisibility() == 0) {
            boolean z = view instanceof ViewGroup;
            ViewGroup viewGroup = view;
            if (z) {
                ViewGroup viewGroup2 = (ViewGroup) view;
                boolean a = C2003v.m8474a(viewGroup2);
                viewGroup = viewGroup2;
                if (!a) {
                    int childCount = viewGroup2.getChildCount();
                    for (int i = 0; i < childCount; i++) {
                        mo4294f(arrayList, viewGroup2.getChildAt(i));
                    }
                    return;
                }
            }
            arrayList.add(viewGroup);
        }
    }

    /* renamed from: g */
    public abstract Object mo4266g(Object obj);

    /* access modifiers changed from: package-private */
    /* renamed from: j */
    public void mo4295j(Map<String, View> map, View view) {
        if (view.getVisibility() == 0) {
            String H = C1988t.m8347H(view);
            if (H != null) {
                map.put(H, view);
            }
            if (view instanceof ViewGroup) {
                ViewGroup viewGroup = (ViewGroup) view;
                int childCount = viewGroup.getChildCount();
                for (int i = 0; i < childCount; i++) {
                    mo4295j(map, viewGroup.getChildAt(i));
                }
            }
        }
    }

    /* access modifiers changed from: protected */
    /* renamed from: k */
    public void mo4296k(View view, Rect rect) {
        int[] iArr = new int[2];
        view.getLocationOnScreen(iArr);
        rect.set(iArr[0], iArr[1], iArr[0] + view.getWidth(), iArr[1] + view.getHeight());
    }

    /* renamed from: m */
    public abstract Object mo4267m(Object obj, Object obj2, Object obj3);

    /* renamed from: n */
    public abstract Object mo4268n(Object obj, Object obj2, Object obj3);

    /* access modifiers changed from: package-private */
    /* renamed from: o */
    public ArrayList<String> mo4297o(ArrayList<View> arrayList) {
        ArrayList<String> arrayList2 = new ArrayList<>();
        int size = arrayList.size();
        for (int i = 0; i < size; i++) {
            View view = arrayList.get(i);
            arrayList2.add(C1988t.m8347H(view));
            C1988t.m8340D0(view, (String) null);
        }
        return arrayList2;
    }

    /* renamed from: p */
    public abstract void mo4269p(Object obj, View view);

    /* renamed from: q */
    public abstract void mo4270q(Object obj, ArrayList<View> arrayList, ArrayList<View> arrayList2);

    /* renamed from: r */
    public abstract void mo4271r(Object obj, View view, ArrayList<View> arrayList);

    /* access modifiers changed from: package-private */
    /* renamed from: s */
    public void mo4298s(ViewGroup viewGroup, ArrayList<View> arrayList, Map<String, String> map) {
        C1986r.m8331a(viewGroup, new C1272c(arrayList, map));
    }

    /* renamed from: t */
    public abstract void mo4272t(Object obj, Object obj2, ArrayList<View> arrayList, Object obj3, ArrayList<View> arrayList2, Object obj4, ArrayList<View> arrayList3);

    /* renamed from: u */
    public abstract void mo4273u(Object obj, Rect rect);

    /* renamed from: v */
    public abstract void mo4274v(Object obj, View view);

    /* renamed from: w */
    public void mo4275w(Fragment fragment, Object obj, C1849b bVar, Runnable runnable) {
        runnable.run();
    }

    /* access modifiers changed from: package-private */
    /* renamed from: x */
    public void mo4299x(View view, ArrayList<View> arrayList, Map<String, String> map) {
        C1986r.m8331a(view, new C1271b(arrayList, map));
    }

    /* access modifiers changed from: package-private */
    /* renamed from: y */
    public void mo4300y(View view, ArrayList<View> arrayList, ArrayList<View> arrayList2, ArrayList<String> arrayList3, Map<String, String> map) {
        int size = arrayList2.size();
        ArrayList arrayList4 = new ArrayList();
        for (int i = 0; i < size; i++) {
            View view2 = arrayList.get(i);
            String H = C1988t.m8347H(view2);
            arrayList4.add(H);
            if (H != null) {
                C1988t.m8340D0(view2, (String) null);
                String str = map.get(H);
                int i2 = 0;
                while (true) {
                    if (i2 >= size) {
                        break;
                    } else if (str.equals(arrayList3.get(i2))) {
                        C1988t.m8340D0(arrayList2.get(i2), H);
                        break;
                    } else {
                        i2++;
                    }
                }
            }
        }
        C1986r.m8331a(view, new C1270a(size, arrayList2, arrayList3, arrayList, arrayList4));
    }

    /* renamed from: z */
    public abstract void mo4276z(Object obj, View view, ArrayList<View> arrayList);
}
