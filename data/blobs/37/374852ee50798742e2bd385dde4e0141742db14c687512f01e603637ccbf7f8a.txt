package com.test.one.utils;


import net.sf.json.JSONArray;
import net.sf.json.JSONObject;
import net.sf.json.JsonConfig;

import java.util.List;

public class JSONUtils {

    JSONUtils jsonUtils;
    public JSONUtils() {
        if(jsonUtils==null){
            jsonUtils=new JSONUtils();
        }
    }

    /**
     * Bean转jsonString
     *
     * @param obj
     */
    public static String javaToJSON(Object obj) {

        JSONObject jsonObject = JSONObject.fromObject(obj);
        String jsonString = jsonObject.toString();

        return jsonString;
    }

    /**
     * json转Bean
     */
    public static Object jsonToBean(String json, Object object) {
        JSONObject jsonObject = JSONObject.fromObject(json);
        object = JSONObject.toBean(jsonObject, object.getClass());
        return object;
    }

    /**
     * list转json
     */
    public static String listToJson(List list) {
        return JSONObject.fromObject(list).toString();
    }

    /**
     * json转list
     */

    public static List jsonToList(String json,Object obj) {
        List list = JSONArray.toList(JSONArray.fromObject(json), obj, new JsonConfig());
        return list;
    }
}
