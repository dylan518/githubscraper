package day6;

public class Task2 {
    public static void main(String[] args) {
        Airplane myPlane = new Airplane("Boing",2020,100,500);
        myPlane.info();

        myPlane.setYear(2021);
        myPlane.setLength(101);
        myPlane.fillUp(999);
        myPlane.info();
    }
}
