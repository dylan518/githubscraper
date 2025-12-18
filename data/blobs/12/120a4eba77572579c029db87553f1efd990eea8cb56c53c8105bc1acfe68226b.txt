package com.learning;

public class ImplDemo implements InterfaceA, InterfaceB{
    @Override
    public String getSomething(String input) {
        final String str = "Hi ";
        return str + input;
    }

    public static void main(String[] args) {
        ImplDemo implDemo = new ImplDemo();
        System.out.println(implDemo.getSomething("Pradeep"));
    }
}
