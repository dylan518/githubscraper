package Interface.MultipleInheritance;

public interface Market {
    double manipulate();
    void sale(double user, double items);
}

class User {
    public void purchase() {
        System.out.println("Item Purchased Successfully");
    }

    double demand = 1;
    double price = 1000;

}

class Seller extends User implements Market {
    double no_of_user;
    double no_of_items;

    public double manipulate() {
        super.demand = no_of_user / no_of_items;
        super.price = super.price * super.demand;
        return super.price;
    }

    public void sale(double no_of_user, double no_of_items) {
        this.no_of_user = no_of_user;
        this.no_of_items = no_of_items;
        manipulate();
        super.demand = no_of_user / no_of_items;
        if (super.demand < 1) {
            int discount = (int) ((1 - super.demand) * 100);
            System.out.println("Sale available of " + discount + "% off");
            System.out.println("Price of item is Rs " + (int) (super.price) + "/-");
            purchase();
        } else if (super.demand >= 1) {
            System.out.println("Price of item is Rs " + (int) (super.price) + "/-");
            System.out.println("No Sale available");
        }
    }

}