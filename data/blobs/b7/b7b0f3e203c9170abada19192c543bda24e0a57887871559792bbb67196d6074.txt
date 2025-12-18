package main;

import domain.Animal;
import domain.Cat;
import domain.Dog;
import domain.Horse;

public class Main {

    public static void main(String[] args) {
        Animal dog = new Dog("Fido", "meat", (byte)3, "Greyhound");
        Animal cat = new Cat("Slippers", "mice", (byte)5, "Stray");
        Animal horse = new Horse("Thunder", "hay", (byte)5, "Andalusian");
        
        dog.hello();
        cat.hello();
        horse.hello();
    }
    
}
