package com.syntax.class32;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class MapsDemo2 {
    public static void main(String[] args) {

        ArrayList<String> veggies=new ArrayList<>();
        veggies.add("potato");
        veggies.add("Carrot");
        veggies.add("Onion");


        ArrayList<String> fruit=new ArrayList<>();

        fruit.add("Apple");
        fruit.add("Orange");
        fruit.add("Banana");


        Map<String, ArrayList<String>> healthyFoods=new HashMap<>();
        healthyFoods.put("Vegetables",veggies);
        healthyFoods.put("Fruit",fruit);

        System.out.println(healthyFoods);


    }



}
