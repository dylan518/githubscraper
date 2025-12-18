package Tregulov;

public class Human {
    String name;
    Car4 car;
    BankAccaunt1 bA;

    void info() {
        System.out.println("Imya: " + name + " cvet: " + car.color + " Balans banka: " + bA.balance);

    }
}
class HumanTest{
    public static void main(String[] args) {


    Human h = new Human();
    h.name = "Dabid";
    h.car = new Car4("red", "V8");
    h.bA = new BankAccaunt1(18, 200.5);
    h.info();
    }
}

class Car4 {
    Car4(String c, String e) {
        color = c;
        engine = e;
    }
    String color;
    String engine;
    }
class BankAccaunt1 {
    BankAccaunt1(int id2, double balance2) {
        id = id2;
        balance = balance2;
    }
    int id;
    double balance;
}