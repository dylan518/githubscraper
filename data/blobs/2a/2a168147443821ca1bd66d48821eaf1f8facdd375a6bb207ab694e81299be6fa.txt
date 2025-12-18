package by.bog.ArrayDemo;


import java.util.Scanner;
import java.util.Arrays;
public class Task3 {
    public static void main(String[] args) {


        Scanner sc = new Scanner(System.in);
        String[] array = new String[7];
        int index = 0;

        while (index < array.length) {
            String input = sc.next();
            if (input.equals("end")) {
                break;
            }
            array[index] = input;
            index++;
        }

        System.out.println(Arrays.toString(array));
    }
}
