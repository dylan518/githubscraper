package com.rick.pattern_11_proxy.d05_protect_proxy;

/**
 * @Author: Rick
 * @Date: 2022/9/24 08:24
 */
public class PersonImpl implements Person {
    String name;
    String gender;
    String interests;
    int rating;
    int ratingCount = 0;

    public PersonImpl(String name, String gender, String interests, int rating, int ratingCount) {
        this.name = name;
        this.gender = gender;
        this.interests = interests;
        this.rating = rating;
        this.ratingCount = ratingCount;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String getGender() {
        return gender;
    }

    @Override
    public String getInterests() {
        return interests;
    }

    @Override
    public int getGeekRating() {
        if (ratingCount == 0) return 0;
        return rating / ratingCount;
    }


    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public void setGender(String gender) {
        this.gender = gender;
    }

    @Override
    public void setInterests(String interests) {
        this.interests = interests;
    }

    @Override
    public void setGeekRating(int rating) {
        this.rating += rating;
        ratingCount++;
    }
}
