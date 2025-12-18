package com.StringBuilderMutableStrings;

public class Main {

    public static void main(String[] args) {

        String helloWorld = "Hello" + " World";
        helloWorld.concat(" and GoodBye");

        StringBuilder helloWorldBuilder = new StringBuilder("Hello" + " World");
        helloWorldBuilder.append(" and Goodbye");


        PrintInformation(helloWorld);
        PrintInformation(helloWorldBuilder);

        StringBuilder emptyString = new StringBuilder();
        emptyString.append("A".repeat(17));

        StringBuilder emptyString32 = new StringBuilder(32);
        emptyString32.append("Z".repeat(17));



        PrintInformation(emptyString);
        PrintInformation(emptyString32);

        System.out.println("____________________");

        StringBuilder builderPlus = new StringBuilder("Hello " + "World");
        builderPlus.append(" and good bye");

        builderPlus.deleteCharAt(16 ).insert(16, 'G');
        System.out.println(builderPlus);

        builderPlus.replace(16,17,"Z");
        System.out.println(builderPlus);

        builderPlus.reverse();
        System.out.println(builderPlus);

        builderPlus.reverse().setLength(11);
        System.out.println(builderPlus);
    }


    public static void PrintInformation(String string) {
        System.out.println("String = " + string);
        System.out.println("String Length = " + string.length());
    }

    public static void PrintInformation(StringBuilder builder) {
        System.out.println("StringBuilder = " + builder);
        System.out.println("StringBuilder Length = " + builder.length());

        System.out.println("Capacity = " + builder.capacity());
    }

}


