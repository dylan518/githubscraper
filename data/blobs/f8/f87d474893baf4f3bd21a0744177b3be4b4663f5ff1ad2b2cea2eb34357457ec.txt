abstract class Car {  // abstract class
    public abstract void drive();

    public void playMusic() {
        System.out.println("Play Music");
    }
}

class WagonR extends Car {   // concreate class
    public void drive() {
        System.out.println("Driving...");
    }
}

public class AbstractDemo {
    public static void main(String[] args) {
        Car obj = new WagonR();
        obj.drive();
        obj.playMusic();
    }
}

// -- if a method is abstract then class must be abstract
// -- but if a class is abstract it may have abstact method or not or only simple
// methods only or may be both.
// -- we can't create of abject of abstract class( or we can create object of concreate class)