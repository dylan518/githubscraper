package defpackage;

import android.animation.ObjectAnimator;
import android.view.View;
import org.chromium.chrome.browser.infobar.TranslateCompactInfoBar;
import org.chromium.components.translate.TranslateTabLayout;

/* compiled from: chromium-ChromeModern.aab-stable-519513610 */
/* loaded from: classes.dex */
public final class KW3 implements View.OnLayoutChangeListener {
    public final /* synthetic */ TranslateCompactInfoBar a;

    public KW3(TranslateCompactInfoBar translateCompactInfoBar) {
        this.a = translateCompactInfoBar;
    }

    @Override // android.view.View.OnLayoutChangeListener
    public final void onLayoutChange(View view, int i, int i2, int i3, int i4, int i5, int i6, int i7, int i8) {
        if (i == i5 && i2 == i6 && i3 == i7 && i4 == i8) {
            return;
        }
        TranslateCompactInfoBar translateCompactInfoBar = this.a;
        RW3 rw3 = translateCompactInfoBar.u;
        if (rw3 != null) {
            rw3.b();
        }
        RW3 rw32 = translateCompactInfoBar.v;
        if (rw32 != null) {
            rw32.b();
        }
        if (!translateCompactInfoBar.B) {
            ObjectAnimator objectAnimator = translateCompactInfoBar.t.V;
            if (objectAnimator != null) {
                objectAnimator.end();
                return;
            }
            return;
        }
        TranslateTabLayout translateTabLayout = translateCompactInfoBar.t;
        int i9 = 0;
        for (int i10 = 0; i10 < translateTabLayout.l(); i10++) {
            i9 += translateTabLayout.k(i10) == null ? 0 : translateTabLayout.k(i10).f.getWidth() + translateTabLayout.W + translateTabLayout.a0;
        }
        int width = i9 - translateTabLayout.getWidth();
        if (width <= 0) {
            width = 0;
        }
        if (width != 0) {
            int[] iArr = new int[1];
            if (translateTabLayout.getLayoutDirection() == 1) {
                width = 0;
            }
            iArr[0] = width;
            ObjectAnimator ofInt = ObjectAnimator.ofInt(translateTabLayout, "scrollX", iArr);
            translateTabLayout.V = ofInt;
            ofInt.setStartDelay(1000L);
            translateTabLayout.V.setDuration(300L);
            translateTabLayout.V.setInterpolator(AbstractC8142nr1.a);
            translateTabLayout.V.addListener(new C3559aX3(translateTabLayout));
            translateTabLayout.V.start();
        }
        translateCompactInfoBar.B = false;
    }
}
