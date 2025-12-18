package com.ua.robot.homework20;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("Список слів доступних для перекладу: броколі, помідор, спаржа, яблоко, мандарин, огірок, тиква, апельсин,капуста, буряк");
        Scanner myObj = new Scanner(System.in);
        System.out.println("Введіть слово зі списку: ");
        String sourceWord = myObj.nextLine();


        Map<String, List<String>> dict = new HashMap<>();
        dict.put("броколі", List.of("broccoli", "ブロッコリー", "Brokkoli"));
        dict.put("помідор", List.of("tomato", "トマト", "Tomate"));
        dict.put("спаржа", List.of("asparagus", "アスパラガス", "Spargel"));
        dict.put("яблоко", List.of("apple", "ひとつのりんご", "Apfel"));
        dict.put("мандарин", List.of("tangerine", "タンジェリン", "Mandarine"));
        dict.put("огірок", List.of("cucumber", "キュウリ", "Gurke"));
        dict.put("тиква", List.of("pumpkin", "かぼちゃ", "Kürbis"));
        dict.put("апельсин", List.of("orange", "オレンジ", "orange"));
        dict.put("капуста", List.of("cabbage", "キャベツ", "Kohl"));
        dict.put("буряк", List.of("beet", "ビート", "Rübe"));

        System.out.println("Переклад слова " + sourceWord + " на англійську, японську та німецьку мови: " + dict.get(sourceWord.toLowerCase()));

    }
}
