package com.google.android.gms.internal.ads;

import android.util.Pair;
import java.util.Objects;

/* compiled from: com.google.android.gms:play-services-ads@@21.0.0 */
/* loaded from: classes.dex */
public abstract class zzci {
    public static final zzci zza = new zzcd();
    public static final zzl zzb = new zzl() { // from class: com.google.android.gms.internal.ads.zzcc
    };

    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj instanceof zzci) {
            zzci zzciVar = (zzci) obj;
            if (zzciVar.zzc() == zzc() && zzciVar.zzb() == zzb()) {
                zzch zzchVar = new zzch();
                zzcf zzcfVar = new zzcf();
                zzch zzchVar2 = new zzch();
                zzcf zzcfVar2 = new zzcf();
                for (int i2 = 0; i2 < zzc(); i2++) {
                    if (!zze(i2, zzchVar, 0L).equals(zzciVar.zze(i2, zzchVar2, 0L))) {
                        return false;
                    }
                }
                for (int i3 = 0; i3 < zzb(); i3++) {
                    if (!zzd(i3, zzcfVar, true).equals(zzciVar.zzd(i3, zzcfVar2, true))) {
                        return false;
                    }
                }
                return true;
            }
            return false;
        }
        return false;
    }

    public final int hashCode() {
        zzch zzchVar = new zzch();
        zzcf zzcfVar = new zzcf();
        int zzc = zzc() + 217;
        for (int i2 = 0; i2 < zzc(); i2++) {
            zzc = (zzc * 31) + zze(i2, zzchVar, 0L).hashCode();
        }
        int zzb2 = zzb() + (zzc * 31);
        for (int i3 = 0; i3 < zzb(); i3++) {
            zzb2 = (zzb2 * 31) + zzd(i3, zzcfVar, true).hashCode();
        }
        return zzb2;
    }

    public abstract int zza(Object obj);

    public abstract int zzb();

    public abstract int zzc();

    public abstract zzcf zzd(int i2, zzcf zzcfVar, boolean z);

    public abstract zzch zze(int i2, zzch zzchVar, long j2);

    public abstract Object zzf(int i2);

    public int zzg(boolean z) {
        return zzo() ? -1 : 0;
    }

    public int zzh(boolean z) {
        if (zzo()) {
            return -1;
        }
        return zzc() - 1;
    }

    public final int zzi(int i2, zzcf zzcfVar, zzch zzchVar, int i3, boolean z) {
        int i4 = zzd(i2, zzcfVar, false).zzd;
        if (zze(i4, zzchVar, 0L).zzp == i2) {
            int zzj = zzj(i4, i3, z);
            if (zzj == -1) {
                return -1;
            }
            return zze(zzj, zzchVar, 0L).zzo;
        }
        return i2 + 1;
    }

    public int zzj(int i2, int i3, boolean z) {
        if (i3 == 0) {
            if (i2 == zzh(z)) {
                return -1;
            }
            return i2 + 1;
        } else if (i3 != 1) {
            if (i3 == 2) {
                return i2 == zzh(z) ? zzg(z) : i2 + 1;
            }
            throw new IllegalStateException();
        } else {
            return i2;
        }
    }

    public int zzk(int i2, int i3, boolean z) {
        if (i2 == zzg(false)) {
            return -1;
        }
        return i2 - 1;
    }

    public final Pair zzl(zzch zzchVar, zzcf zzcfVar, int i2, long j2) {
        Pair zzm = zzm(zzchVar, zzcfVar, i2, j2, 0L);
        Objects.requireNonNull(zzm);
        return zzm;
    }

    public final Pair zzm(zzch zzchVar, zzcf zzcfVar, int i2, long j2, long j3) {
        zzcw.zza(i2, 0, zzc());
        zze(i2, zzchVar, j3);
        if (j2 == -9223372036854775807L) {
            long j4 = zzchVar.zzm;
            j2 = 0;
        }
        int i3 = zzchVar.zzo;
        zzd(i3, zzcfVar, false);
        while (i3 < zzchVar.zzp) {
            long j5 = zzcfVar.zzf;
            int i4 = (j2 > 0L ? 1 : (j2 == 0L ? 0 : -1));
            if (i4 == 0) {
                break;
            }
            int i5 = i3 + 1;
            long j6 = zzd(i5, zzcfVar, false).zzf;
            if (i4 < 0) {
                break;
            }
            i3 = i5;
        }
        zzd(i3, zzcfVar, true);
        long j7 = zzcfVar.zzf;
        long j8 = zzcfVar.zze;
        if (j8 != -9223372036854775807L) {
            j2 = Math.min(j2, j8 - 1);
        }
        long max = Math.max(0L, j2);
        Object obj = zzcfVar.zzc;
        Objects.requireNonNull(obj);
        return Pair.create(obj, Long.valueOf(max));
    }

    public zzcf zzn(Object obj, zzcf zzcfVar) {
        return zzd(zza(obj), zzcfVar, true);
    }

    public final boolean zzo() {
        return zzc() == 0;
    }
}
