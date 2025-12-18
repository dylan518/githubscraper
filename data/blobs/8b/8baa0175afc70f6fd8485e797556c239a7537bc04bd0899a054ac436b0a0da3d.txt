package com.example.ddg_vip.class_DDG;

import java.util.Date;

public class Discount {
    private Integer discountId;
    private String discription;
    private Date time;
    private Float sale;

    public Discount() {
    }

    public Discount(Integer discountId, String discription, Date time, Float sale) {
        this.discountId = discountId;
        this.discription = discription;
        this.time = time;
        this.sale = sale;
    }

    public Integer getDiscountId() {
        return discountId;
    }

    public void setDiscountId(Integer discountId) {
        this.discountId = discountId;
    }

    public String getDiscription() {
        return discription;
    }

    public void setDiscription(String discription) {
        this.discription = discription;
    }

    public Date getTime() {
        return time;
    }

    public void setTime(Date time) {
        this.time = time;
    }

    public Float getSale() {
        return sale;
    }

    public void setSale(Float sale) {
        this.sale = sale;
    }
}
/*CREATE TABLE `discount` (
        `discountId` int(11) NOT NULL,
        `discription` varchar(1000) NOT NULL,
        `time` datetime NOT NULL,
        `sale` float NOT NULL*/