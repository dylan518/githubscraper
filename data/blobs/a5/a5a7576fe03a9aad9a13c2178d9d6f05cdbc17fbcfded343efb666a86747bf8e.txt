package org.gmail.ollga.task2;

import java.util.Objects;
import java.util.Scanner;

public class HelloViacheslav {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a name");
        String name = scan.nextLine();

        String message = (Objects.equals(name, "Viacheslav")) ? "Hello, Viacheslav" : "No such name";
        System.out.println(message);
    }
}

