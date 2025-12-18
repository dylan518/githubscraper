package org.bedu.dependecyInjection.model;

import org.springframework.stereotype.Component;

@Component
public class Person {
    private String name;
    /*
    public Person(String name){
        this.name=name;
    }
     */

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String greet(String anotherName){
        return "Hello, " + anotherName + " my name is "+ name;
    }
}
