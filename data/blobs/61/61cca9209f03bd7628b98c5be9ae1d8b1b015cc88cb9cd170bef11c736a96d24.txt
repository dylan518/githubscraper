package ej3;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * [This is the app to sort un Arraylist.
 *
 * @version [1.01.001 2022-07-04]
 *
 * @author [Alexander Betancur - alexbetbu@gmail.com]
 *
 */

public class App {
    public static void main(String[] args) {
        System.out.println("Random Numbers List generated : ");

        ArrayList<Integer> listNumber = new ArrayList<Integer>();

        for(int i = 0; i < 10; i++) {
            double data = Math.random()*100;
            int number = (int)data;
            listNumber.add(i, number);
        }

        for(int i = 0; i < listNumber.size(); i++) {
            System.out.print(listNumber.get(i) + " ");
        }

        System.out.println("\nPress 1 to order by bubble sort method");
        System.out.println("Press 2 to order by quick sort method");

        Scanner input_scanner = new Scanner(System.in);
        char data = input_scanner.nextLine().charAt(0);

            switch(data) {
                case '1':
                    Sorter.bubbleSort(listNumber);
                    System.out.println("Array ordered by BubbleSort Method");
                    break;

                case '2':
                    Sorter.quickSort(listNumber, 0, listNumber.size()-1);
                    System.out.println("Array ordered by QuickSort Method");
                    break;

                default:
                    System.out.println("No valid data. Array not ordered");
            }

        for(int i = 0; i < listNumber.size(); i++) {
            System.out.print(listNumber.get(i) + " ");
        }
    }
}
