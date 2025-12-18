package org.spongycastle.asn1.x509;

import org.spongycastle.asn1.ASN1Encodable;
import org.spongycastle.asn1.ASN1Object;
import org.spongycastle.asn1.ASN1Primitive;
import org.spongycastle.asn1.ASN1Sequence;
import org.spongycastle.asn1.DERSequence;
import org.spongycastle.util.Strings;

public class GeneralNames extends ASN1Object {
    public final GeneralName[] a;

    public GeneralNames(GeneralName generalName) {
        this.a = new GeneralName[]{generalName};
    }

    public static GeneralNames g(Object obj) {
        if (obj instanceof GeneralNames) {
            return (GeneralNames) obj;
        }
        if (obj != null) {
            return new GeneralNames(ASN1Sequence.q(obj));
        }
        return null;
    }

    public final ASN1Primitive b() {
        return new DERSequence((ASN1Encodable[]) this.a);
    }

    public final GeneralName[] h() {
        GeneralName[] generalNameArr = this.a;
        GeneralName[] generalNameArr2 = new GeneralName[generalNameArr.length];
        System.arraycopy(generalNameArr, 0, generalNameArr2, 0, generalNameArr.length);
        return generalNameArr2;
    }

    public final String toString() {
        StringBuffer stringBuffer = new StringBuffer("GeneralNames:");
        String str = Strings.a;
        stringBuffer.append(str);
        int i = 0;
        while (true) {
            GeneralName[] generalNameArr = this.a;
            if (i == generalNameArr.length) {
                return stringBuffer.toString();
            }
            stringBuffer.append("    ");
            stringBuffer.append(generalNameArr[i]);
            stringBuffer.append(str);
            i++;
        }
    }

    public GeneralNames(ASN1Sequence aSN1Sequence) {
        this.a = new GeneralName[aSN1Sequence.size()];
        for (int i = 0; i != aSN1Sequence.size(); i++) {
            this.a[i] = GeneralName.g(aSN1Sequence.s(i));
        }
    }
}
