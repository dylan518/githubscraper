package com.dsa2024.javaqa.relation;

// Handles the details of a product
class Product {
    private String name;
    private double price;

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }
}

// Handles calculations related to product prices
class PriceCalculator {
    public double calculateTotalPrice(Product product, int quantity) {
        return product.getPrice() * quantity;
    }
}

// Handles displaying product information
class ProductDisplay {
    public void showProductDetails(Product product) {
        System.out.println("Product: " + product.getName());
        System.out.println("Price: " + product.getPrice());
    }
}

// High Cohesion Each class has a single, well-defined responsibility, Single
// Responsibility Principle (SRP)
public class HighCohesion {
    public static void main(String[] args) {
        Product product = new Product("Laptop", 1000.00);
        PriceCalculator calculator = new PriceCalculator();
        ProductDisplay display = new ProductDisplay();

        display.showProductDetails(product);
        double total = calculator.calculateTotalPrice(product, 2);
        System.out.println("Total Price for 2 items: " + total);
    }
}
