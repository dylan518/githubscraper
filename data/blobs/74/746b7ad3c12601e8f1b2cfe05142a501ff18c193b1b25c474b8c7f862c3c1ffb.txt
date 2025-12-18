import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Product p1 = new Product("Coolmate", "Sport Polo ProMax-S1", 349, Size.L, "green");
        Product p2 = new Product("Coolmate", "Sport Polo ProMax-S2", 249, Size.M, "black");
        Product p3 = new Product("Coolmate", "Sport Polo ProMax-S1", 349, Size.L, "black");
        Product p4 = new Product("Uniqlo", "Sport Polo Unisex", 509, Size.XL, "yellow");
        Product p5 = new Product("Uniqlo", "Sport Polo Unisex", 509, Size.L, "white");
        User user1 = new User("Tai", "ThanhTai", "abcdeq123 Australia");
        User user2 = new User("Tai", "ThanhTai", "asfjsadlk Vietnam");
        User user3 = new User("Tai2", "ThanhTai2", "adsjka1 USA");
        System.out.println(Arrays.toString(User.users));
        Scanner scanner = new Scanner(System.in);
        User user;
        int count = 0;
        do {
            System.out.println("Enter your username:");
            String userName =scanner.nextLine();
            System.out.println("Enter your password");
            String password = scanner.nextLine();
            user = User.getUser(userName, password);
            count++;
        } while (user == null && count < 5);
        if (user != null) {
            while (true) {
                System.out.println("Please choose item you wanted to buy by index or press any key to exit");
                int index = 0;
                outer:
                for (Product product : Product.stocks) {
                    if (user.shoppingCart.chosenProducts != null) {
                        for (Product chosenP : user.shoppingCart.chosenProducts) {
                            if (chosenP.productName.equals(product.productName)
                                    && chosenP.color.equals(product.color)
                                    && chosenP.size.equals(product.size)) {
                                index++;
                                continue outer;
                            }
                        }
                    }
                    System.out.println((index++) + ". " + product);
                }
                if (scanner.hasNextInt()) {
                    user.shoppingCart.addItem(Product.stocks[scanner.nextInt()]);
                    System.out.println(Arrays.toString(user.shoppingCart.chosenProducts));
                } else  {
                    break;
                }
            }
            if (user.shoppingCart.chosenProducts != null) {
                System.out.println("Your order is: " + Arrays.toString(user.shoppingCart.chosenProducts));
                System.out.println("your total price is: " + user.getTotal());
            }
        }
    }

}
