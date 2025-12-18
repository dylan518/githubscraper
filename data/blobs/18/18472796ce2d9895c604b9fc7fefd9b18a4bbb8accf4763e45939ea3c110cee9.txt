package site.javadev.lesson_13;

import java.util.ArrayList;
import java.util.List;

/**1. Создай список из слов "мама", "мыла", "раму".
 2. После каждого слова вставь в список строку, содержащую слово "именно".
 3. Вывести результат на экран, каждый элемент списка с новой строки.*/
public class Task02 {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        List<String> result = new ArrayList<>();
        list.add("мама");
        list.add("мыла");
        list.add("раму");
        for (int i = 0; i < list.size(); i++) {
            result.add(list.get(i));
            result.add("именно");

        }
        for(String s : result){
            System.out.println(s);
        }
    }
}


