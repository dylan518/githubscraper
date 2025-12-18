package com.journeyapps.barcodescanner;

import android.content.Context;
import android.os.Handler;
import android.os.Message;
import android.util.AttributeSet;
import java.util.HashMap;
import java.util.List;
import ma.C3602k;
import p113hb.C2457b;
import p113hb.C2464i;
import p113hb.C2466k;
import p113hb.C2467l;
import p113hb.C2468m;
import p113hb.C2476u;
import p113hb.InterfaceC2456a;
import p113hb.InterfaceC2465j;
import p129ia.C2684p;
import p129ia.EnumC2673e;

/* loaded from: classes.dex */
public class BarcodeView extends C1392a {

    /* renamed from: I */
    public EnumC1388b f5225I;

    /* renamed from: J */
    public InterfaceC2456a f5226J;

    /* renamed from: K */
    public C2467l f5227K;

    /* renamed from: L */
    public InterfaceC2465j f5228L;

    /* renamed from: M */
    public Handler f5229M;

    /* renamed from: N */
    public final Handler.Callback f5230N;

    /* renamed from: com.journeyapps.barcodescanner.BarcodeView$a */
    /* loaded from: classes.dex */
    public class C1387a implements Handler.Callback {
        public C1387a() {
        }

        @Override // android.os.Handler.Callback
        public boolean handleMessage(Message message) {
            int i10 = message.what;
            if (i10 == C3602k.f12691g) {
                C2457b c2457b = (C2457b) message.obj;
                if (c2457b != null && BarcodeView.this.f5226J != null && BarcodeView.this.f5225I != EnumC1388b.NONE) {
                    BarcodeView.this.f5226J.mo5884b(c2457b);
                    if (BarcodeView.this.f5225I == EnumC1388b.SINGLE) {
                        BarcodeView.this.m5867N();
                    }
                }
                return true;
            }
            if (i10 == C3602k.f12690f) {
                return true;
            }
            if (i10 != C3602k.f12692h) {
                return false;
            }
            List<C2684p> list = (List) message.obj;
            if (BarcodeView.this.f5226J != null && BarcodeView.this.f5225I != EnumC1388b.NONE) {
                BarcodeView.this.f5226J.mo5883a(list);
            }
            return true;
        }
    }

    /* renamed from: com.journeyapps.barcodescanner.BarcodeView$b */
    /* loaded from: classes.dex */
    public enum EnumC1388b {
        NONE,
        SINGLE,
        CONTINUOUS
    }

    public BarcodeView(Context context) {
        super(context);
        this.f5225I = EnumC1388b.NONE;
        this.f5226J = null;
        this.f5230N = new C1387a();
        m5864K();
    }

    public BarcodeView(Context context, AttributeSet attributeSet) {
        super(context, attributeSet);
        this.f5225I = EnumC1388b.NONE;
        this.f5226J = null;
        this.f5230N = new C1387a();
        m5864K();
    }

    /* renamed from: G */
    public final C2464i m5860G() {
        if (this.f5228L == null) {
            this.f5228L = m5861H();
        }
        C2466k c2466k = new C2466k();
        HashMap hashMap = new HashMap();
        hashMap.put(EnumC2673e.NEED_RESULT_POINT_CALLBACK, c2466k);
        C2464i mo9833a = this.f5228L.mo9833a(hashMap);
        c2466k.m9834b(mo9833a);
        return mo9833a;
    }

    /* renamed from: H */
    public InterfaceC2465j m5861H() {
        return new C2468m();
    }

    /* renamed from: I */
    public void m5862I(InterfaceC2456a interfaceC2456a) {
        this.f5225I = EnumC1388b.CONTINUOUS;
        this.f5226J = interfaceC2456a;
        m5865L();
    }

    /* renamed from: J */
    public void m5863J(InterfaceC2456a interfaceC2456a) {
        this.f5225I = EnumC1388b.SINGLE;
        this.f5226J = interfaceC2456a;
        m5865L();
    }

    /* renamed from: K */
    public final void m5864K() {
        this.f5228L = new C2468m();
        this.f5229M = new Handler(this.f5230N);
    }

    /* renamed from: L */
    public final void m5865L() {
        m5866M();
        if (this.f5225I == EnumC1388b.NONE || !m5915t()) {
            return;
        }
        C2467l c2467l = new C2467l(getCameraInstance(), m5860G(), this.f5229M);
        this.f5227K = c2467l;
        c2467l.m9843i(getPreviewFramingRect());
        this.f5227K.m9845k();
    }

    /* renamed from: M */
    public final void m5866M() {
        C2467l c2467l = this.f5227K;
        if (c2467l != null) {
            c2467l.m9846l();
            this.f5227K = null;
        }
    }

    /* renamed from: N */
    public void m5867N() {
        this.f5225I = EnumC1388b.NONE;
        this.f5226J = null;
        m5866M();
    }

    public InterfaceC2465j getDecoderFactory() {
        return this.f5228L;
    }

    public void setDecoderFactory(InterfaceC2465j interfaceC2465j) {
        C2476u.m9873a();
        this.f5228L = interfaceC2465j;
        C2467l c2467l = this.f5227K;
        if (c2467l != null) {
            c2467l.m9844j(m5860G());
        }
    }

    @Override // com.journeyapps.barcodescanner.C1392a
    /* renamed from: u */
    public void mo5868u() {
        m5866M();
        super.mo5868u();
    }

    @Override // com.journeyapps.barcodescanner.C1392a
    /* renamed from: x */
    public void mo5869x() {
        super.mo5869x();
        m5865L();
    }
}
