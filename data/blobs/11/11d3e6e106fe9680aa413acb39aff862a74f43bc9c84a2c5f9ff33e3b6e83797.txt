package o6;

import android.os.Bundle;
import android.os.Parcel;
import android.os.Parcelable;
import n.i;

public final class a extends n0.a {
    public static final Parcelable.Creator<a> CREATOR = new C0110a();

    /* renamed from: q  reason: collision with root package name */
    public final i<String, Bundle> f7747q;

    /* renamed from: o6.a$a  reason: collision with other inner class name */
    public static class C0110a implements Parcelable.ClassLoaderCreator<a> {
        public final Object createFromParcel(Parcel parcel) {
            return new a(parcel, (ClassLoader) null);
        }

        public final Object[] newArray(int i10) {
            return new a[i10];
        }

        public final Object createFromParcel(Parcel parcel, ClassLoader classLoader) {
            return new a(parcel, classLoader);
        }
    }

    public a(Parcel parcel, ClassLoader classLoader) {
        super(parcel, classLoader);
        int readInt = parcel.readInt();
        String[] strArr = new String[readInt];
        parcel.readStringArray(strArr);
        Bundle[] bundleArr = new Bundle[readInt];
        parcel.readTypedArray(bundleArr, Bundle.CREATOR);
        this.f7747q = new i<>(readInt);
        for (int i10 = 0; i10 < readInt; i10++) {
            this.f7747q.put(strArr[i10], bundleArr[i10]);
        }
    }

    public a(Parcelable parcelable) {
        super(parcelable);
        this.f7747q = new i<>();
    }

    public final String toString() {
        return "ExtendableSavedState{" + Integer.toHexString(System.identityHashCode(this)) + " states=" + this.f7747q + "}";
    }

    public final void writeToParcel(Parcel parcel, int i10) {
        parcel.writeParcelable(this.f7340o, i10);
        i<String, Bundle> iVar = this.f7747q;
        int i11 = iVar.f7333q;
        parcel.writeInt(i11);
        String[] strArr = new String[i11];
        Bundle[] bundleArr = new Bundle[i11];
        for (int i12 = 0; i12 < i11; i12++) {
            strArr[i12] = iVar.h(i12);
            bundleArr[i12] = iVar.l(i12);
        }
        parcel.writeStringArray(strArr);
        parcel.writeTypedArray(bundleArr, 0);
    }
}
