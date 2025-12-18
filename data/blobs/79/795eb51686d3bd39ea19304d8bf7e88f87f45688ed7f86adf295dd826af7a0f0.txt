package com.learn.springboot.models;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class Bank {
    
    @Id
    public int id;

    public String name;
    public String type;

    public Bank() {

    }

    public Bank(int id, String name, String type) {
        this.id = id;
        this.name = name;
        this.type = type;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setType(String type) {
        this.type = type;
    }


    public int getId() {
        return this.id;
    }
    public String getName() {
        return this.name;
    }
    public String getType() {
        return this.type;
    }


}
