package Tuesday.Inheritance;

public class Animal {
    double weight;
    int eyes;
    int legs;

    String species;
    String sound;

    public Animal(double weight, int eyes, int legs, String species, String sound){
        this.weight = weight;
        this.eyes = eyes;
        this.legs = legs;
        this.species = species;
        this.sound = sound;
    }

    public Animal() {

    }


    public void  speak() {
        System.out.println("The animal says: " + this.sound);
    }

    public void speak_specific(){
        System.out.println("The " + this.species + " says " + this.sound);
    }



}
