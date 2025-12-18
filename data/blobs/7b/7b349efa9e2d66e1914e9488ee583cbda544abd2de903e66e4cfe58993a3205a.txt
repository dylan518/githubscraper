package defpackage;

import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import com.google.android.inputmethod.latin.R;

/* compiled from: PG */
/* renamed from: elb  reason: default package */
/* loaded from: classes.dex */
public class elb extends dek {
    public elb(Context context, deq deqVar) {
        super(context, deqVar);
    }

    @Override // defpackage.dek, defpackage.ald
    public final Object b(ViewGroup viewGroup, int i) {
        Object b = super.b(viewGroup, i);
        ((View) b).setTag(R.id.f54730_resource_name_obfuscated_res_0x7f0b01c1, Integer.valueOf(l(i)));
        return b;
    }

    @Override // defpackage.dek, defpackage.ald
    public final void c(ViewGroup viewGroup, int i, Object obj) {
        super.c(viewGroup, i, obj);
        ((View) obj).setTag(R.id.f54730_resource_name_obfuscated_res_0x7f0b01c1, null);
    }
}
