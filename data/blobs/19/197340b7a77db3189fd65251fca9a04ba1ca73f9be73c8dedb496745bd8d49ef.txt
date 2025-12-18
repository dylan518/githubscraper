package com.nanchen.compresshelper;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Matrix;
import android.graphics.Paint;
import android.graphics.Rect;
import android.media.ExifInterface;
import android.net.Uri;
import android.text.TextUtils;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class a {
    private static int a(BitmapFactory.Options options, int i2, int i3) {
        int i4;
        int i5 = options.outHeight;
        int i6 = options.outWidth;
        if (i5 > i3 || i6 > i2) {
            i4 = Math.round(((float) i5) / ((float) i3));
            int round = Math.round(((float) i6) / ((float) i2));
            if (i4 >= round) {
                i4 = round;
            }
        } else {
            i4 = 1;
        }
        while (((float) (i6 * i5)) / ((float) (i4 * i4)) > ((float) (i2 * i3 * 2))) {
            i4++;
        }
        return i4;
    }

    static Bitmap a(Context context, Uri uri, float f2, float f3, Bitmap.Config config) {
        int i2;
        float f4 = f2;
        float f5 = f3;
        String b2 = c.b(context, uri);
        BitmapFactory.Options options = new BitmapFactory.Options();
        options.inJustDecodeBounds = true;
        Bitmap decodeFile = BitmapFactory.decodeFile(b2, options);
        Bitmap bitmap = null;
        if (decodeFile == null) {
            try {
                FileInputStream fileInputStream = new FileInputStream(b2);
                BitmapFactory.decodeStream(fileInputStream, (Rect) null, options);
                fileInputStream.close();
            } catch (FileNotFoundException e2) {
                e2.printStackTrace();
            } catch (IOException e3) {
                e3.printStackTrace();
            }
        }
        int i3 = options.outHeight;
        int i4 = options.outWidth;
        if (i3 == -1 || i4 == -1) {
            try {
                ExifInterface exifInterface = new ExifInterface(b2);
                i3 = exifInterface.getAttributeInt("ImageLength", 1);
                i4 = exifInterface.getAttributeInt("ImageWidth", 1);
            } catch (IOException e4) {
                e4.printStackTrace();
            }
        }
        if (i4 <= 0 || i3 <= 0) {
            Bitmap decodeFile2 = BitmapFactory.decodeFile(b2);
            if (decodeFile2 == null) {
                return null;
            }
            i4 = decodeFile2.getWidth();
            i3 = decodeFile2.getHeight();
        }
        float f6 = (float) i4;
        float f7 = (float) i2;
        float f8 = f6 / f7;
        float f9 = f4 / f5;
        if (f7 > f5 || f6 > f4) {
            if (f8 < f9) {
                i4 = (int) ((f5 / f7) * f6);
                i2 = (int) f5;
            } else {
                i2 = f8 > f9 ? (int) ((f4 / f6) * f7) : (int) f5;
                i4 = (int) f4;
            }
        }
        options.inSampleSize = a(options, i4, i2);
        options.inJustDecodeBounds = false;
        options.inPurgeable = true;
        options.inInputShareable = true;
        options.inTempStorage = new byte[16384];
        try {
            decodeFile = BitmapFactory.decodeFile(b2, options);
            if (decodeFile == null) {
                try {
                    FileInputStream fileInputStream2 = new FileInputStream(b2);
                    BitmapFactory.decodeStream(fileInputStream2, (Rect) null, options);
                    fileInputStream2.close();
                } catch (IOException e5) {
                    e5.printStackTrace();
                }
            }
        } catch (OutOfMemoryError e6) {
            e6.printStackTrace();
        }
        if (i2 <= 0 || i4 <= 0) {
            return null;
        }
        try {
            bitmap = Bitmap.createBitmap(i4, i2, config);
        } catch (OutOfMemoryError e7) {
            e7.printStackTrace();
        }
        float f10 = ((float) i4) / ((float) options.outWidth);
        float f11 = ((float) i2) / ((float) options.outHeight);
        Matrix matrix = new Matrix();
        matrix.setScale(f10, f11, 0.0f, 0.0f);
        Canvas canvas = new Canvas(bitmap);
        canvas.setMatrix(matrix);
        canvas.drawBitmap(decodeFile, 0.0f, 0.0f, new Paint(2));
        try {
            int attributeInt = new ExifInterface(b2).getAttributeInt("Orientation", 0);
            Matrix matrix2 = new Matrix();
            if (attributeInt == 6) {
                matrix2.postRotate(90.0f);
            } else if (attributeInt == 3) {
                matrix2.postRotate(180.0f);
            } else if (attributeInt == 8) {
                matrix2.postRotate(270.0f);
            }
            return Bitmap.createBitmap(bitmap, 0, 0, bitmap.getWidth(), bitmap.getHeight(), matrix2, true);
        } catch (IOException e8) {
            e8.printStackTrace();
            return bitmap;
        }
    }

    /* JADX WARNING: Removed duplicated region for block: B:17:0x0038 A[SYNTHETIC, Splitter:B:17:0x0038] */
    /* JADX WARNING: Removed duplicated region for block: B:23:0x0043 A[SYNTHETIC, Splitter:B:23:0x0043] */
    /* Code decompiled incorrectly, please refer to instructions dump. */
    static java.io.File a(android.content.Context r7, android.net.Uri r8, float r9, float r10, android.graphics.Bitmap.CompressFormat r11, android.graphics.Bitmap.Config r12, int r13, java.lang.String r14, java.lang.String r15, java.lang.String r16) {
        /*
            java.lang.String r0 = r11.name()
            java.lang.String r4 = r0.toLowerCase()
            r1 = r7
            r2 = r14
            r3 = r8
            r5 = r15
            r6 = r16
            java.lang.String r1 = a(r1, r2, r3, r4, r5, r6)
            r2 = 0
            java.io.FileOutputStream r3 = new java.io.FileOutputStream     // Catch:{ FileNotFoundException -> 0x0032 }
            r3.<init>(r1)     // Catch:{ FileNotFoundException -> 0x0032 }
            r0 = r7
            r2 = r8
            r4 = r9
            r5 = r10
            r6 = r12
            android.graphics.Bitmap r0 = a(r7, r8, r9, r10, r12)     // Catch:{ FileNotFoundException -> 0x002d, all -> 0x002a }
            r2 = r11
            r4 = r13
            r0.compress(r11, r13, r3)     // Catch:{ FileNotFoundException -> 0x002d, all -> 0x002a }
            r3.close()     // Catch:{ IOException -> 0x003b }
            goto L_0x003b
        L_0x002a:
            r0 = move-exception
            r2 = r3
            goto L_0x0041
        L_0x002d:
            r0 = move-exception
            r2 = r3
            goto L_0x0033
        L_0x0030:
            r0 = move-exception
            goto L_0x0041
        L_0x0032:
            r0 = move-exception
        L_0x0033:
            r0.printStackTrace()     // Catch:{ all -> 0x0030 }
            if (r2 == 0) goto L_0x003b
            r2.close()     // Catch:{ IOException -> 0x003b }
        L_0x003b:
            java.io.File r0 = new java.io.File
            r0.<init>(r1)
            return r0
        L_0x0041:
            if (r2 == 0) goto L_0x0046
            r2.close()     // Catch:{ IOException -> 0x0046 }
        L_0x0046:
            throw r0
        */
        throw new UnsupportedOperationException("Method not decompiled: com.nanchen.compresshelper.a.a(android.content.Context, android.net.Uri, float, float, android.graphics.Bitmap$CompressFormat, android.graphics.Bitmap$Config, int, java.lang.String, java.lang.String, java.lang.String):java.io.File");
    }

    private static String a(Context context, String str, Uri uri, String str2, String str3, String str4) {
        File file = new File(str);
        if (!file.exists()) {
            file.mkdirs();
        }
        if (TextUtils.isEmpty(str3)) {
            str3 = "";
        }
        if (TextUtils.isEmpty(str4)) {
            str4 = str3 + c.a(c.a(context, uri))[0];
        }
        return file.getAbsolutePath() + File.separator + str4 + "." + str2;
    }
}
