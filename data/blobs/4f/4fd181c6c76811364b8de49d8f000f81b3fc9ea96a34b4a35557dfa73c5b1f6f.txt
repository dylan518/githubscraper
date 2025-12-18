package com.p7700g.p99005;

import android.content.Context;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.FrameLayout;
import androidx.appcompat.widget.TintTypedArray;
import com.p7700g.p99005.ga2;
import com.p7700g.p99005.gs;
import com.p7700g.p99005.i2;
import com.p7700g.p99005.kf2;

/* compiled from: NavigationRailView.java */
/* loaded from: classes3.dex */
public class xf2 extends tf2 {
    public static final int E = 49;
    public static final int F = 7;
    private static final int G = 49;
    public static final int H = -1;
    private final int I;
    @z1
    private View J;
    @z1
    private Boolean K;
    @z1
    private Boolean L;

    /* compiled from: NavigationRailView.java */
    /* loaded from: classes3.dex */
    public class a implements kf2.e {
        public a() {
        }

        @Override // com.p7700g.p99005.kf2.e
        @x1
        public gs a(View view, @x1 gs gsVar, @x1 kf2.f fVar) {
            xf2 xf2Var = xf2.this;
            if (xf2Var.u(xf2Var.K)) {
                fVar.b += gsVar.f(gs.m.i()).c;
            }
            xf2 xf2Var2 = xf2.this;
            if (xf2Var2.u(xf2Var2.L)) {
                fVar.d += gsVar.f(gs.m.i()).e;
            }
            boolean z = sr.Y(view) == 1;
            int p = gsVar.p();
            int q = gsVar.q();
            int i = fVar.a;
            if (z) {
                p = q;
            }
            fVar.a = i + p;
            fVar.a(view);
            return gsVar;
        }
    }

    public xf2(@x1 Context context) {
        this(context, null);
    }

    private wf2 getNavigationRailMenuView() {
        return (wf2) getMenuView();
    }

    private void p() {
        kf2.d(this, new a());
    }

    private boolean r() {
        View view = this.J;
        return (view == null || view.getVisibility() == 8) ? false : true;
    }

    private int s(int i) {
        int suggestedMinimumWidth = getSuggestedMinimumWidth();
        if (View.MeasureSpec.getMode(i) == 1073741824 || suggestedMinimumWidth <= 0) {
            return i;
        }
        int paddingLeft = getPaddingLeft();
        return View.MeasureSpec.makeMeasureSpec(Math.min(View.MeasureSpec.getSize(i), getPaddingRight() + paddingLeft + suggestedMinimumWidth), 1073741824);
    }

    /* JADX INFO: Access modifiers changed from: private */
    public boolean u(Boolean bool) {
        return bool != null ? bool.booleanValue() : sr.T(this);
    }

    @z1
    public View getHeaderView() {
        return this.J;
    }

    public int getItemMinimumHeight() {
        return ((wf2) getMenuView()).getItemMinimumHeight();
    }

    @Override // com.p7700g.p99005.tf2
    public int getMaxItemCount() {
        return 7;
    }

    public int getMenuGravity() {
        return getNavigationRailMenuView().getMenuGravity();
    }

    public void n(@s1 int i) {
        o(LayoutInflater.from(getContext()).inflate(i, (ViewGroup) this, false));
    }

    public void o(@x1 View view) {
        t();
        this.J = view;
        FrameLayout.LayoutParams layoutParams = new FrameLayout.LayoutParams(-2, -2);
        layoutParams.gravity = 49;
        layoutParams.topMargin = this.I;
        addView(view, 0, layoutParams);
    }

    @Override // android.widget.FrameLayout, android.view.ViewGroup, android.view.View
    public void onLayout(boolean z, int i, int i2, int i3, int i4) {
        super.onLayout(z, i, i2, i3, i4);
        wf2 navigationRailMenuView = getNavigationRailMenuView();
        int i5 = 0;
        if (r()) {
            int bottom = this.J.getBottom() + this.I;
            int top = navigationRailMenuView.getTop();
            if (top < bottom) {
                i5 = bottom - top;
            }
        } else if (navigationRailMenuView.t()) {
            i5 = this.I;
        }
        if (i5 > 0) {
            navigationRailMenuView.layout(navigationRailMenuView.getLeft(), navigationRailMenuView.getTop() + i5, navigationRailMenuView.getRight(), navigationRailMenuView.getBottom() + i5);
        }
    }

    @Override // android.widget.FrameLayout, android.view.View
    public void onMeasure(int i, int i2) {
        int s = s(i);
        super.onMeasure(s, i2);
        if (r()) {
            measureChild(getNavigationRailMenuView(), s, View.MeasureSpec.makeMeasureSpec((getMeasuredHeight() - this.J.getMeasuredHeight()) - this.I, Integer.MIN_VALUE));
        }
    }

    @Override // com.p7700g.p99005.tf2
    @i2({i2.a.LIBRARY_GROUP})
    @x1
    /* renamed from: q */
    public wf2 d(@x1 Context context) {
        return new wf2(context);
    }

    public void setItemMinimumHeight(@c2 int i) {
        ((wf2) getMenuView()).setItemMinimumHeight(i);
    }

    public void setMenuGravity(int i) {
        getNavigationRailMenuView().setMenuGravity(i);
    }

    public void t() {
        View view = this.J;
        if (view != null) {
            removeView(view);
            this.J = null;
        }
    }

    public xf2(@x1 Context context, @z1 AttributeSet attributeSet) {
        this(context, attributeSet, ga2.c.lc);
    }

    public xf2(@x1 Context context, @z1 AttributeSet attributeSet, int i) {
        this(context, attributeSet, i, ga2.n.ri);
    }

    public xf2(@x1 Context context, @z1 AttributeSet attributeSet, int i, int i2) {
        super(context, attributeSet, i, i2);
        this.K = null;
        this.L = null;
        this.I = getResources().getDimensionPixelSize(ga2.f.C8);
        TintTypedArray k = cf2.k(getContext(), attributeSet, ga2.o.Io, i, i2, new int[0]);
        int resourceId = k.getResourceId(ga2.o.Jo, 0);
        if (resourceId != 0) {
            n(resourceId);
        }
        setMenuGravity(k.getInt(ga2.o.Lo, 49));
        int i3 = ga2.o.Ko;
        if (k.hasValue(i3)) {
            setItemMinimumHeight(k.getDimensionPixelSize(i3, -1));
        }
        int i4 = ga2.o.No;
        if (k.hasValue(i4)) {
            this.K = Boolean.valueOf(k.getBoolean(i4, false));
        }
        int i5 = ga2.o.Mo;
        if (k.hasValue(i5)) {
            this.L = Boolean.valueOf(k.getBoolean(i5, false));
        }
        k.recycle();
        p();
    }
}