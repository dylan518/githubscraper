package me.rerere.matrix.thirdparty.okhttp3.internal.http1;

import java.lang.invoke.MethodHandles;
import java.net.ProtocolException;
import java.util.concurrent.TimeUnit;
import me.rerere.matrix.internal.o3;
import me.rerere.matrix.thirdparty.kotlin.jvm.internal.Intrinsics;
import me.rerere.matrix.thirdparty.kotlin.text.StringsKt;
import me.rerere.matrix.thirdparty.okhttp3.HttpUrl;
import me.rerere.matrix.thirdparty.okhttp3.internal.Util;
import me.rerere.matrix.thirdparty.okhttp3.internal.http.HttpHeaders;
import me.rerere.matrix.thirdparty.okio.Buffer;
import me.rerere.matrix.thirdparty.org.jetbrains.annotations.NotNull;

public final class Http1ExchangeCodec$ChunkedSource extends Http1ExchangeCodec$AbstractSource {
  @NotNull
  private final HttpUrl url;
  
  private boolean hasMoreChunks;
  
  private long bytesRemainingInChunk;
  
  private static final long b = o3.a(6882105375795373235L, 9166594172546291873L, MethodHandles.lookup().lookupClass()).a(122231118978498L);
  
  public Http1ExchangeCodec$ChunkedSource(HttpUrl paramHttpUrl) {
    super(paramHttp1ExchangeCodec);
    this.url = paramHttpUrl;
    this.bytesRemainingInChunk = -1L;
    this.hasMoreChunks = true;
  }
  
  public long read(@NotNull Buffer paramBuffer, long paramLong) {
    // Byte code:
    //   0: getstatic me/rerere/matrix/thirdparty/okhttp3/internal/http1/Http1ExchangeCodec$ChunkedSource.b : J
    //   3: ldc2_w 72612327516534
    //   6: lxor
    //   7: lstore #4
    //   9: aload_1
    //   10: ldc 'sink'
    //   12: invokestatic checkNotNullParameter : (Ljava/lang/Object;Ljava/lang/String;)V
    //   15: lload_2
    //   16: lconst_0
    //   17: lcmp
    //   18: iflt -> 29
    //   21: iconst_1
    //   22: goto -> 30
    //   25: invokestatic a : (Ljava/lang/NumberFormatException;)Ljava/lang/NumberFormatException;
    //   28: athrow
    //   29: iconst_0
    //   30: ifne -> 60
    //   33: iconst_0
    //   34: istore #7
    //   36: ldc 'byteCount < 0: '
    //   38: lload_2
    //   39: invokestatic valueOf : (J)Ljava/lang/Long;
    //   42: invokestatic stringPlus : (Ljava/lang/String;Ljava/lang/Object;)Ljava/lang/String;
    //   45: astore #7
    //   47: new java/lang/IllegalArgumentException
    //   50: dup
    //   51: aload #7
    //   53: invokevirtual toString : ()Ljava/lang/String;
    //   56: invokespecial <init> : (Ljava/lang/String;)V
    //   59: athrow
    //   60: aload_0
    //   61: invokevirtual getClosed : ()Z
    //   64: ifne -> 75
    //   67: iconst_1
    //   68: goto -> 76
    //   71: invokestatic a : (Ljava/lang/NumberFormatException;)Ljava/lang/NumberFormatException;
    //   74: athrow
    //   75: iconst_0
    //   76: ifne -> 99
    //   79: iconst_0
    //   80: istore #7
    //   82: ldc 'closed'
    //   84: astore #7
    //   86: new java/lang/IllegalStateException
    //   89: dup
    //   90: aload #7
    //   92: invokevirtual toString : ()Ljava/lang/String;
    //   95: invokespecial <init> : (Ljava/lang/String;)V
    //   98: athrow
    //   99: aload_0
    //   100: getfield hasMoreChunks : Z
    //   103: ifne -> 114
    //   106: ldc2_w -1
    //   109: lreturn
    //   110: invokestatic a : (Ljava/lang/NumberFormatException;)Ljava/lang/NumberFormatException;
    //   113: athrow
    //   114: aload_0
    //   115: getfield bytesRemainingInChunk : J
    //   118: lconst_0
    //   119: lcmp
    //   120: ifeq -> 141
    //   123: aload_0
    //   124: getfield bytesRemainingInChunk : J
    //   127: ldc2_w -1
    //   130: lcmp
    //   131: ifne -> 167
    //   134: goto -> 141
    //   137: invokestatic a : (Ljava/lang/NumberFormatException;)Ljava/lang/NumberFormatException;
    //   140: athrow
    //   141: aload_0
    //   142: invokespecial readChunkSize : ()V
    //   145: aload_0
    //   146: getfield hasMoreChunks : Z
    //   149: ifne -> 167
    //   152: goto -> 159
    //   155: invokestatic a : (Ljava/lang/NumberFormatException;)Ljava/lang/NumberFormatException;
    //   158: athrow
    //   159: ldc2_w -1
    //   162: lreturn
    //   163: invokestatic a : (Ljava/lang/NumberFormatException;)Ljava/lang/NumberFormatException;
    //   166: athrow
    //   167: aload_0
    //   168: aload_1
    //   169: aload_0
    //   170: getfield bytesRemainingInChunk : J
    //   173: lstore #8
    //   175: lload_2
    //   176: lload #8
    //   178: invokestatic min : (JJ)J
    //   181: invokespecial read : (Lme/rerere/matrix/thirdparty/okio/Buffer;J)J
    //   184: lstore #6
    //   186: lload #6
    //   188: ldc2_w -1
    //   191: lcmp
    //   192: ifne -> 223
    //   195: aload_0
    //   196: getfield this$0 : Lme/rerere/matrix/thirdparty/okhttp3/internal/http1/Http1ExchangeCodec;
    //   199: invokevirtual getConnection : ()Lme/rerere/matrix/thirdparty/okhttp3/internal/connection/RealConnection;
    //   202: invokevirtual noNewExchanges$okhttp : ()V
    //   205: new java/net/ProtocolException
    //   208: dup
    //   209: ldc 'unexpected end of stream'
    //   211: invokespecial <init> : (Ljava/lang/String;)V
    //   214: astore #8
    //   216: aload_0
    //   217: invokevirtual responseBodyComplete : ()V
    //   220: aload #8
    //   222: athrow
    //   223: aload_0
    //   224: aload_0
    //   225: getfield bytesRemainingInChunk : J
    //   228: lload #6
    //   230: lsub
    //   231: putfield bytesRemainingInChunk : J
    //   234: lload #6
    //   236: lreturn
    // Exception table:
    //   from	to	target	type
    //   9	25	25	java/lang/NumberFormatException
    //   60	71	71	java/lang/NumberFormatException
    //   99	110	110	java/lang/NumberFormatException
    //   114	134	137	java/lang/NumberFormatException
    //   123	152	155	java/lang/NumberFormatException
    //   141	163	163	java/lang/NumberFormatException
  }
  
  public void close() {
    try {
      if (getClosed())
        return; 
    } catch (NumberFormatException numberFormatException) {
      throw a(null);
    } 
    try {
      if (this.hasMoreChunks)
        try {
          if (!Util.discard(this, 100, TimeUnit.MILLISECONDS)) {
            Http1ExchangeCodec.this.getConnection().noNewExchanges$okhttp();
            responseBodyComplete();
          } 
        } catch (NumberFormatException numberFormatException) {
          throw a(null);
        }  
    } catch (NumberFormatException numberFormatException) {
      throw a(null);
    } 
    setClosed(true);
  }
  
  private static NumberFormatException a(NumberFormatException paramNumberFormatException) {
    return paramNumberFormatException;
  }
}


/* Location:              C:\Users\Administrator\Desktop\Matrix_7.0.0_alpha28(3)(1).jar!\me\rerere\matrix\thirdparty\okhttp3\internal\http1\Http1ExchangeCodec$ChunkedSource.class
 * Java compiler version: 8 (52.0)
 * JD-Core Version:       1.1.3
 */