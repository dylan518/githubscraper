package com.jap.validator;

public class CredentialsValidatorImpl {
    public String validateUser(String name, String password){
        CredentialsValidator credentialsValidator=(n1,n2)->{
            if (n1.equals("admin")&& n2.equals("1234")){
                return "valid user";
            }else {
                return "invalid user";
            }
        };


        return credentialsValidator.validator(name, password);
    }



}
