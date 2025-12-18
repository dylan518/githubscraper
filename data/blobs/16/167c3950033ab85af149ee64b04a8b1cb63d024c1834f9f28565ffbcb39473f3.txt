package org.example.POJO;

public class Customer {

    private String webshopID;
    private String id;
    private String name;
    private String address;

    public Customer() {
    }

    public Customer(String webshopID, String id, String name, String address) {
        this.webshopID = webshopID;
        this.id = id;
        this.name = name;
        this.address = address;
    }

    public String getWebshopID() {
        return webshopID;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getAddress() {
        return address;
    }

    @Override
    public String toString() {
        return
                //"Customer: " +
                "webshopID: " + webshopID +
                ", id: " + id +
                ", name: " + name +
                ", address: " + address;
    }
}