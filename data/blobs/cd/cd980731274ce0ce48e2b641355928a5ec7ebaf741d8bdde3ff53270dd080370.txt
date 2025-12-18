package hl0;

import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.drawable.Drawable;
import android.text.style.ImageSpan;
import java.lang.ref.WeakReference;
import kotlin.jvm.internal.p;

/* compiled from: CenteredImageSpan.kt */
public final class a extends ImageSpan {

    /* renamed from: a  reason: collision with root package name */
    private WeakReference<Drawable> f20189a;

    /* JADX INFO: super call moved to the top of the method (can break code semantics) */
    public a(Drawable drawable, int i11) {
        super(drawable, i11);
        p.j(drawable, "drawable");
    }

    private final Drawable a() {
        Drawable drawable;
        WeakReference<Drawable> weakReference = this.f20189a;
        if (weakReference == null) {
            drawable = null;
        } else {
            drawable = (Drawable) weakReference.get();
        }
        if (drawable != null) {
            return drawable;
        }
        Drawable drawable2 = getDrawable();
        this.f20189a = new WeakReference<>(drawable2);
        return drawable2;
    }

    public void draw(Canvas canvas, CharSequence charSequence, int i11, int i12, float f11, int i13, int i14, int i15, Paint paint) {
        p.j(canvas, "canvas");
        p.j(paint, "paint");
        Drawable a11 = a();
        if (a11 != null) {
            canvas.save();
            canvas.translate(f11, (float) ((i13 + ((i15 - i13) / 2)) - (a11.getBounds().height() / 2)));
            a11.draw(canvas);
            canvas.restore();
        }
    }

    public int getSize(Paint paint, CharSequence charSequence, int i11, int i12, Paint.FontMetricsInt fontMetricsInt) {
        p.j(paint, "paint");
        Drawable a11 = a();
        if (a11 == null) {
            return 0;
        }
        if (fontMetricsInt != null) {
            Paint.FontMetricsInt fontMetricsInt2 = paint.getFontMetricsInt();
            fontMetricsInt.ascent = fontMetricsInt2.ascent;
            fontMetricsInt.descent = fontMetricsInt2.descent;
            fontMetricsInt.top = fontMetricsInt2.top;
            fontMetricsInt.bottom = fontMetricsInt2.bottom;
        }
        return a11.getBounds().right;
    }
}
