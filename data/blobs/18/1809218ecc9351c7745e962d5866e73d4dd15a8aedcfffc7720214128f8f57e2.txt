package com.chartboost.sdk;

import android.content.Context;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.content.res.Resources;
import android.os.Build;
import android.os.Build.VERSION;
import android.provider.Settings.Secure;
import android.util.DisplayMetrics;
import android.view.Display;
import android.view.WindowManager;
import java.security.MessageDigest;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.TreeSet;

public class CBAPIRequest
{
  private static final String CB_PARAM_AUID = "auid";
  private static final String CB_PARAM_COUNTRY = "country";
  private static final String CB_PARAM_HEIGHT = "h";
  private static final String CB_PARAM_LANGUAGE = "language";
  private static final String CB_PARAM_MODEL = "model";
  private static final String CB_PARAM_OS = "os";
  private static final String CB_PARAM_SCALE = "scale";
  private static final String CB_PARAM_SDK = "sdk";
  private static final String CB_PARAM_UUID = "uuid";
  private static final String CB_PARAM_VERSION = "bundle";
  private static final String CB_PARAM_WIDTH = "w";
  private String action;
  private Map<String, String> body;
  private Context context;
  private Object contextInfoObject;
  private String controller;
  private List<String> params;
  private Map<String, String> query;
  
  public CBAPIRequest(Context paramContext, String paramString1, String paramString2)
  {
    this.context = paramContext;
    this.controller = paramString1;
    this.action = paramString2;
  }
  
  private String serializeDictionaryToString(Map<String, String> paramMap)
  {
    String str1 = "";
    Iterator localIterator = new TreeSet(paramMap.keySet()).iterator();
    for (;;)
    {
      if (!localIterator.hasNext()) {
        return str1;
      }
      String str2 = (String)localIterator.next();
      if ((!str2.equals("app")) && (!str2.equals("signature")))
      {
        String str3 = (String)paramMap.get(str2);
        str1 = str1 + str2 + ":" + str3 + ";";
      }
    }
  }
  
  public void appendBodyArgument(String paramString1, String paramString2)
  {
    if (this.body == null) {
      this.body = new HashMap();
    }
    this.body.put(paramString1, paramString2);
  }
  
  public void appendDeviceInfoParams()
    throws CBMissingInformationException
  {
    if (this.context == null) {
      throw new CBMissingInformationException();
    }
    if (Build.PRODUCT.equals("sdk"))
    {
      appendBodyArgument("model", "Android Simulator");
      appendBodyArgument("uuid", "ffff");
      appendBodyArgument("auid", "ffff");
    }
    for (;;)
    {
      appendBodyArgument("os", "Android " + Build.VERSION.RELEASE);
      appendBodyArgument("country", Locale.getDefault().getCountry());
      appendBodyArgument("language", Locale.getDefault().getDisplayLanguage());
      appendBodyArgument("sdk", "2.1");
      Display localDisplay = ((WindowManager)this.context.getSystemService("window")).getDefaultDisplay();
      appendBodyArgument("w", localDisplay.getWidth());
      appendBodyArgument("h", localDisplay.getHeight());
      appendBodyArgument("scale", this.context.getResources().getDisplayMetrics().density);
      try
      {
        appendBodyArgument("bundle", this.context.getPackageManager().getPackageInfo(this.context.getPackageName(), 128).versionName);
        return;
      }
      catch (Exception localException) {}
      appendBodyArgument("model", Build.MODEL);
      appendBodyArgument("uuid", Settings.Secure.getString(this.context.getContentResolver(), "android_id"));
      appendBodyArgument("auid", CBUtility.getAUID(this.context));
    }
  }
  
  public void appendQueryArgument(String paramString1, String paramString2)
  {
    if (this.query == null) {
      this.query = new HashMap();
    }
    this.query.put(paramString1, paramString2);
  }
  
  public String getAction()
  {
    return this.action;
  }
  
  public Map<String, String> getBody()
  {
    return this.body;
  }
  
  public Object getContextInfoObject()
  {
    return this.contextInfoObject;
  }
  
  public String getController()
  {
    return this.controller;
  }
  
  public List<String> getParams()
  {
    return this.params;
  }
  
  public Map<String, String> getQuery()
  {
    return this.query;
  }
  
  public void setAction(String paramString)
  {
    this.action = paramString;
  }
  
  public void setBody(Map<String, String> paramMap)
  {
    this.body = paramMap;
  }
  
  public void setContextInfoObject(Object paramObject)
  {
    this.contextInfoObject = paramObject;
  }
  
  public void setController(String paramString)
  {
    this.controller = paramString;
  }
  
  public void setParams(List<String> paramList)
  {
    this.params = paramList;
  }
  
  public void setQuery(Map<String, String> paramMap)
  {
    this.query = paramMap;
  }
  
  public void sign(String paramString1, String paramString2)
    throws Exception
  {
    Object localObject1 = "controller:" + this.controller + ";action:" + this.action + ";";
    Object localObject2 = localObject1;
    if (this.query != null) {
      localObject2 = localObject1 + serializeDictionaryToString(this.query);
    }
    localObject1 = localObject2;
    if (this.body != null) {
      localObject1 = localObject2 + serializeDictionaryToString(this.body);
    }
    localObject2 = localObject1;
    int i;
    if (this.params != null)
    {
      i = 0;
      localObject2 = this.params.iterator();
      if (!((Iterator)localObject2).hasNext()) {
        localObject2 = localObject1;
      }
    }
    else
    {
      paramString2 = (localObject2 + "app:" + paramString1 + ";signature:" + paramString2 + ";").getBytes("US-ASCII");
      localObject1 = MessageDigest.getInstance("MD5").digest(paramString2);
      paramString2 = "";
      i = 0;
    }
    for (;;)
    {
      if (i >= localObject1.length)
      {
        appendBodyArgument("app", paramString1);
        appendBodyArgument("signature", paramString2);
        return;
        String str = (String)((Iterator)localObject2).next();
        localObject1 = localObject1 + i + ":" + str + ";";
        i += 1;
        break;
      }
      paramString2 = paramString2 + String.format("%02x", new Object[] { Integer.valueOf(localObject1[i] & 0xFF) });
      i += 1;
    }
  }
}


/* Location:           D:\BaiduNetdiskDownload\AndroidKiller_v1.3.1\projects\MapleThiefv1.1\ProjectSrc\smali\
 * Qualified Name:     com.chartboost.sdk.CBAPIRequest
 * JD-Core Version:    0.7.0.1
 */