package com.api;
import org.json.JSONObject;

import static com.api.Constants.*;
public class Users {
    RestUtil rest;
    public Users(){
        rest = new RestUtil();
        rest.login(DEFAULT_USER,DEFAULT_PASSWORD).given();
    }
    public void createUser(String firstName,String lastName, String status,String email,String phoneNum){
        JSONObject json = new JSONObject();
        json.put("first_name",firstName);
        json.put("last_name",lastName);
        json.put("active",status);
        json.put("email",email);
        json.put("phone",phoneNum);
        rest.addPayLoad(json,CREATEUSER).postRequest(CREATEUSER);
    }
}
