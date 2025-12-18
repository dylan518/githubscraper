package lombok;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        Order o1 = new Order();
        o1.getId();
        new Order("1", new ArrayList<>(), "shipping");

        o1.set

        Product p1 = new Product("1", "name");
        Product p2 = p1.withName("abc");

        Order o2 = Order.builder()
                .id("id")
                .shippingAddress("address")
                .build();
    }
}
