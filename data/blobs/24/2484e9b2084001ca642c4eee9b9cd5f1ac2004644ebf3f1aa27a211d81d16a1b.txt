package ch14.lamda;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.function.Consumer;

public class RamdaExam {
    public static void main(String[] args) {
        List<String> items = Arrays.asList("apple" , "banana" , "cherry");

        Consumer<String> RamdaTest = new Consumer<String>() {
            @Override
            public void accept(String s) {
                System.out.println(s);
            }
        };
        items.forEach(item -> System.out.println(item));



        new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i=0;i<5;i++){
                    System.out.println("Thread: "+ i);
                }
            }
        }).start();


        new Thread(()->{
            for(int i=0;i<5;i++){
                System.out.println("RamdaThread: "+ i);
            }
        }).start();

        List<Integer> numbers = Arrays.asList(1, 3, 2, 4, 6, 5, 8, 7, 9, 10);
        //일반적인형태
//        Collections.sort(numbers, new Comparator<Integer>() {
//            @Override
//            public int compare(Integer o1, Integer o2) {
//                return o1.compareTo(o2);
//            }
//        });
        //람다식 표현
        Collections.sort(numbers , (Integer o1, Integer o2) -> o1.compareTo(o2));

        numbers.forEach(new Consumer<Integer>(){
            @Override
            public void accept(Integer integer) {
                System.out.println(integer);
            }
        });
        numbers.forEach((Integer integer)-> System.out.println(integer));
    }
}
