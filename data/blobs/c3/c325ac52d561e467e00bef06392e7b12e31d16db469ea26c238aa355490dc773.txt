package com.kodilla.spring.basic.spring_dependency_injection.homework;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import static org.junit.jupiter.api.Assertions.*;


@SpringBootTest
class ShippingCenterTest {

    @Test
    public void packageShouldBeNotDeliveredIfPackageWeightAbove30() {
        ApplicationContext context = new AnnotationConfigApplicationContext("com.kodilla.spring.basic");
        ShippingCenter bean = context.getBean(ShippingCenter.class);
        String result = bean.sendPackage("Cracow", 30.01);
        Assertions.assertEquals("Package not delivered to: Cracow", result);
    }

    @Test
    public void packageShouldBeDeliveredIfPackageWeightUnder30() {
        ApplicationContext context = new AnnotationConfigApplicationContext("com.kodilla.spring.basic");
        ShippingCenter bean = context.getBean(ShippingCenter.class);
        String result = bean.sendPackage("Cracow", 29.9);
        Assertions.assertEquals("Package delivered to: Cracow", result);
    }

    @Test
    public void shouldReturnCorrectMessage() {
        ApplicationContext context = new AnnotationConfigApplicationContext("com.kodilla.spring.basic");
        ShippingCenter bean = context.getBean(ShippingCenter.class);
        String message = bean.sendPackage("address", 1.0);
        Assertions.assertNotNull(message);
    }


}