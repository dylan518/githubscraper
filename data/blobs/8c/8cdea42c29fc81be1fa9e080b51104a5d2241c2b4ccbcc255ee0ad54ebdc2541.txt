package Lambda_Supplier;

import java.util.function.Supplier;

public class Main {
    public static void main(String[] args) {
        Supplier<String> supplier = () -> "Hello, this is Supplier example!";
        System.out.println(supplier.get());
    }
}
