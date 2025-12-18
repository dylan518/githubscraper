package org.js9.model;

public class Product extends BaseEntity{
    private String name;
    private double price;
    private double quantityToBuy;
    private  double quantityInStore = 0;


    public Product() {
        this.name = "Generic Product";
        this.price = 0.0;
        this.quantityInStore = 0.0;
    }

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
        this.quantityToBuy = 0;
    }


    public Product(String name, double price, double quantityInStore) {
        this.name = name;
        this.price = price;
        this.quantityInStore = quantityInStore;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public double getQuantityToBuy() {
        return quantityToBuy;
    }

    public void setQuantityToBuy(double quantityToBuy) {
        this.quantityToBuy = quantityToBuy;
    }

    public  double getQuantityInStore() {
        return quantityInStore;
    }

    public  void setQuantityInStore(double quantityInStore) {
        this.quantityInStore = quantityInStore;
    }

    @Override
    public String toString() {
        return "Product{" +
                "name='" + name + '\'' +
                ", price=" + price +
                ", quantityToBuy=" + quantityToBuy +", " +
                "quantityToInStore=" + getQuantityInStore() +
                " } " + super.toString();
    }
}
