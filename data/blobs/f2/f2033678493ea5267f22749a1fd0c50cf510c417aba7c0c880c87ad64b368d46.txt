package library.lang.ex.ex4;

import java.util.Objects;

class Product {
    private String name;
    private long price;
    private int quantity;

    public Product(String name, long price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Product product = (Product) o;
        return price == product.price && quantity == product.quantity && Objects.equals(name, product.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, price, quantity);
    }

    @Override
    public String toString() {
        return "상품: [" +
                name + ']' +
                ", 가격: [" + price +
                "], 수량: [" + quantity +
                ']';
    }

    public static void main(String[] args) {
        Product carrot1 = new Product("당근", 3000, 30);
        Product carrot2 = new Product("당근", 3000, 30);

        carrot1.equals(carrot2);

        System.out.println(carrot1.hashCode());
        System.out.println(carrot2.hashCode());

        System.out.println(carrot1.toString());
        System.out.println(carrot2.toString());
    }
}