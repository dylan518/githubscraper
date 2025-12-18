package lesson9;

import java.time.LocalDate;
import java.util.*;

public class Main {
    public static void main(String[] args) {
//        Map<String, UserProfile> users = new HashMap<>();
//        users.put("sergei", new UserProfile("Sergei", "sergei@mail.com"));
//        users.put("viktor", new UserProfile("Viktor", "viktor@mail.com"));
//        System.out.println(users);
//
//        users.put("sergei", new UserProfile("Alexei", "alexei@mail.com"));
//        System.out.println(users);
//
//        users.remove("viktor");
//
//        if (users.containsKey("viktor")) {
//            UserProfile viktor = users.get("viktor");
//            viktor.lastVisitTime = LocalDate.now();
//            System.out.println(viktor);
//        } else {
//            users.put("viktor", new UserProfile("Viktor", "viktor@mail.com"));
//
//        }
//
//        Set<String> keys = users.keySet();
//        Iterator<String> keysIt = keys.iterator();
//        while (keysIt.hasNext()) {
//            String key = keysIt.next();
//            UserProfile profile = users.get(key);
//            System.out.println(key + " -> " + profile);
//        }
//
//        Collection<UserProfile> values = users.values();
//        values.forEach(System.out::println);

         String text = "Dsf aFbd klfdasd";
         Map<Character, Integer> letterList = new HashMap<>();

         for(char letter: text.toCharArray()){
             if (Character.isLetter(letter)){
                 letter = Character.toLowerCase(letter);
                 if (letterList.containsKey(letter)){
                     letterList.put(letter, letterList.get(letter) + 1);
                 }else {
                     letterList.put(letter, 1);
                 }
             }
         }

        System.out.println(letterList.toString());
    }
}
