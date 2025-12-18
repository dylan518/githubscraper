package org.webrtc;

import java.util.Arrays;

public class IceCandidate
{
  public final PeerConnection.AdapterType adapterType;
  public final String sdp;
  public final int sdpMLineIndex;
  public final String sdpMid;
  public final String serverUrl;
  
  public IceCandidate(String paramString1, int paramInt, String paramString2)
  {
    this.sdpMid = paramString1;
    this.sdpMLineIndex = paramInt;
    this.sdp = paramString2;
    this.serverUrl = "";
    this.adapterType = PeerConnection.AdapterType.UNKNOWN;
  }
  
  @CalledByNative
  IceCandidate(String paramString1, int paramInt, String paramString2, String paramString3, PeerConnection.AdapterType paramAdapterType)
  {
    this.sdpMid = paramString1;
    this.sdpMLineIndex = paramInt;
    this.sdp = paramString2;
    this.serverUrl = paramString3;
    this.adapterType = paramAdapterType;
  }
  
  private static boolean objectEquals(Object paramObject1, Object paramObject2)
  {
    if (paramObject1 == null) {
      return paramObject2 == null;
    }
    return paramObject1.equals(paramObject2);
  }
  
  public boolean equals(Object paramObject)
  {
    boolean bool1 = paramObject instanceof IceCandidate;
    boolean bool2 = false;
    if (!bool1) {
      return false;
    }
    paramObject = (IceCandidate)paramObject;
    bool1 = bool2;
    if (objectEquals(this.sdpMid, paramObject.sdpMid))
    {
      bool1 = bool2;
      if (this.sdpMLineIndex == paramObject.sdpMLineIndex)
      {
        bool1 = bool2;
        if (objectEquals(this.sdp, paramObject.sdp)) {
          bool1 = true;
        }
      }
    }
    return bool1;
  }
  
  @CalledByNative
  String getSdp()
  {
    return this.sdp;
  }
  
  @CalledByNative
  String getSdpMid()
  {
    return this.sdpMid;
  }
  
  public int hashCode()
  {
    return Arrays.hashCode(new Object[] { this.sdpMid, Integer.valueOf(this.sdpMLineIndex), this.sdp });
  }
  
  public String toString()
  {
    StringBuilder localStringBuilder = new StringBuilder();
    localStringBuilder.append(this.sdpMid);
    localStringBuilder.append(":");
    localStringBuilder.append(this.sdpMLineIndex);
    localStringBuilder.append(":");
    localStringBuilder.append(this.sdp);
    localStringBuilder.append(":");
    localStringBuilder.append(this.serverUrl);
    localStringBuilder.append(":");
    localStringBuilder.append(this.adapterType.toString());
    return localStringBuilder.toString();
  }
}


/* Location:           E:\android_tools\AndroidKiller_v1.3.1\projects\hoxin-release\ProjectSrc\smali\
 * Qualified Name:     org.webrtc.IceCandidate
 * JD-Core Version:    0.7.0.1
 */