/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  kotlin.Metadata
 *  kotlin.jvm.functions.Function0
 *  kotlin.jvm.internal.Intrinsics
 *  kotlin.jvm.internal.Lambda
 *  okhttp3.Address
 *  okhttp3.CertificatePinner
 *  okhttp3.Handshake
 *  okhttp3.internal.tls.CertificateChainCleaner
 */
package okhttp3.internal.connection;

import java.security.cert.Certificate;
import java.util.List;
import kotlin.Metadata;
import kotlin.jvm.functions.Function0;
import kotlin.jvm.internal.Intrinsics;
import kotlin.jvm.internal.Lambda;
import okhttp3.Address;
import okhttp3.CertificatePinner;
import okhttp3.Handshake;
import okhttp3.internal.tls.CertificateChainCleaner;

@Metadata(d1={"\u0000\n\n\u0000\n\u0002\u0010 \n\u0002\u0018\u0002\u0010\u0000\u001a\b\u0012\u0004\u0012\u00020\u00020\u0001H\n"}, d2={"<anonymous>", "", "Ljava/security/cert/Certificate;"}, k=3, mv={1, 5, 1}, xi=48)
static final class RealConnection.connectTls.1
extends Lambda
implements Function0<List<? extends Certificate>> {
    final Address $address;
    final CertificatePinner $certificatePinner;
    final Handshake $unverifiedHandshake;

    RealConnection.connectTls.1(CertificatePinner certificatePinner, Handshake handshake, Address address) {
        this.$certificatePinner = certificatePinner;
        this.$unverifiedHandshake = handshake;
        this.$address = address;
        super(0);
    }

    public final List<Certificate> invoke() {
        CertificateChainCleaner certificateChainCleaner = this.$certificatePinner.getCertificateChainCleaner$okhttp();
        Intrinsics.checkNotNull((Object)certificateChainCleaner);
        return certificateChainCleaner.clean(this.$unverifiedHandshake.peerCertificates(), this.$address.url().host());
    }
}
