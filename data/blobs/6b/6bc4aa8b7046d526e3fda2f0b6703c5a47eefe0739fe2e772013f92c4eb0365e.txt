package com.juaracoding.oop;
import java.util.Date;

public class MainOOP {
    public static void main(String[] args) {
//        Date date = new Date();
//        System.out.println(date);

        Fruit apple = new Fruit();
        apple.grams = 60;
        apple.calsPerGram = 15;
        System.out.println(apple.totalCalories());
        System.out.println(apple);

        Fruit avocado = new Fruit();
        avocado.grams = 220;
        avocado.calsPerGram = 354;
        System.out.println(avocado.totalCalories());
        System.out.println(avocado);

        Kotak kotakSatu = new Kotak(5);
        kotakSatu.drawKotak();
        System.out.println(kotakSatu.getLuasKotak());

        Kotak kotakDua = new Kotak(8);
        kotakDua.drawKotak();
        System.out.println(kotakDua.getLuasKotak());

        Car car1 = new Car("Bensin");
        car1.warna();
        car1.mesin();
        System.out.println(car1.getTahunPembuatan());


        Product product1 = new Product("SSD1", "KingStone SSD", 350000, "Fast and Good Quality SSD", "C:\\JuaraCoding\\java-fundamental\\img\\ssd1.jpg");
        product1.detailProduct();
        product1.addToCart();

        Product product2 = new Product("SSD2", "Samsung SSD", 400000, "Good SSD!", "C:\\JuaraCoding\\java-fundamental\\img\\ssd1.jpg");
        product2.detailProduct();
        product2.addToCart();
    }
}
