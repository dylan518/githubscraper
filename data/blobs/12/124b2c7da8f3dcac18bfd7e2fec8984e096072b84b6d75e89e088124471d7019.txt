package com.syntax.class21;

public class AnimalTester {
    public static void main(String[] args) {
        Dog dog=new Dog("Tom","red","German",25);
        dog.printInfo();

        Dog dog1=new Dog("Charley","white","russian",2);
        dog1.printInfo();

        Animal animal=new Animal("Charley","black","swiss",23);
        animal.printInfo();

        Cat cat=new Cat("Peter","grey","british",1);
        cat.printInfo();
    }
}
