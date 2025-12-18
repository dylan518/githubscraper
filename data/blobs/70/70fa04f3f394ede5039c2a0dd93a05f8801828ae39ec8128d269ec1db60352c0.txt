package com.github.philippepeter.javatraining.session1;

public class MyFirstClass {

    private int variable = 2;

    void sayHello(String name) {
        System.out.println("Hello " + name + " my internal state is " + variable);
    }

    void setVariable(int variable) {
        this.variable = variable;
    }


}
