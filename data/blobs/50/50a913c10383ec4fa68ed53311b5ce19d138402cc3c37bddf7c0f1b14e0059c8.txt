package visitor;

import transport.Animal;
import transport.Person;
import transport.Shipment;

public class PriceTransportVisitor implements TransportVisitor {

    @Override
    public void visit(Animal animal) {
        int price = (int) (animal.getWeight() * 0.2);
        System.out.println("Price per kilometer for a animal: " + price + " PLN");
    }

    @Override
    public void visit(Person person) {
        int price = 6;
        if (person.isRegularCustomer()) {
            price = price / 2;
        }
        System.out.println("Price per kilometer for a person: "
                + price + " PLN");
    }

    @Override
    public void visit(Shipment shipment) {
        int price = 2;
        if (shipment.isLarge())
            price *= 3;
        System.out.println("Price per kilomer for a shipment: " + price + " PLN");
    }

}
