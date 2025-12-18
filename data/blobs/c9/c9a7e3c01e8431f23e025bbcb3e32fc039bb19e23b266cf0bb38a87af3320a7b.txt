package com.mycompany.youtubee.entities;

public class user 
{
    private String address;
    private String mobile;
    private String firstname;
    private String lastname;
    private String emailid;
    private String password;
    private String role;
    private String gender;
    private String profile;
    
     public user(String address,String mobile,String firstname, String lastname, String emailid, String password, String role, String gender)
    {
        this.address=address;
        this.mobile=mobile;
        this.firstname=firstname;
        this.lastname=lastname;
        this.emailid=emailid;
        this.password=password;
        this.role=role;
        this.gender=gender;
    }

    public user(String address, String mobile, String firstname, String lastname, String emailid, String password, String role, String gender, String profile) {
        this.address = address;
        this.mobile = mobile;
        this.firstname = firstname;
        this.lastname = lastname;
        this.emailid = emailid;
        this.password = password;
        this.role = role;
        this.gender = gender;
        this.profile = profile;
    }
    public user()
    {
        
    }

    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getMobile() {
        return mobile;
    }

    public void setMobile(String mobile) {
        this.mobile = mobile;
    }
    public String getFirstname() {
        return firstname;
    }
    
    public String getGender() {
        return gender;
    }

    public String getLastname() {
        return lastname;
    }

    public String getEmailid() {
        return emailid;
    }

    public String getPassword() {
        return password;
    }

    public String getRole() {
        return role;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public void setEmailid(String emailid) {
        this.emailid = emailid;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void setRole(String role) {
        this.role = role;
    }
    
    public void setGender(String gender) {
        this.gender = gender;
    }
    
}
