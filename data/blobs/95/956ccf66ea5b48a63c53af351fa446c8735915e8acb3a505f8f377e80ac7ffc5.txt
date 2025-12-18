package com.rkjavahub.generics;

import java.util.ArrayList;
import java.util.List;

public class GenericCollection {
    public static void main(String[] args) {
        List<Integer> tList = new ArrayList<Integer>();
        tList.add(10);
        // tList.add("Rohit"); // compile time error
    }
}
