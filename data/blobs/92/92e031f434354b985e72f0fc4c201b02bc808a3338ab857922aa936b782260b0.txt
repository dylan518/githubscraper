import org.example.*;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class DealershipTest {
    Engine engine;
    Tyres tyres;
    Manufacturer manufacturer;
    Car car;
    Dealership dealership;
    Customer customer;

    @Before
    public void before(){
        engine = new Engine(2.0, 231, 3000);
        tyres = new Tyres("Michelin", 10000);
        manufacturer = new Manufacturer("Mini","John Cooper Works", CarType.PETROL);
        car = new Car(engine, tyres,manufacturer, 32000.00, "Moonwalk Grey");
        dealership = new Dealership(1000000.00);
        customer = new Customer("Mike Hunt", 50000.00);
    }

    @Test
    public void canAddToDealership(){
        dealership.addCar(car);
        assertEquals(1, dealership.getCar());
    }
}
