package javaapplication10;

import java.util.Scanner;

public class JavaApplication10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int no = sc.nextInt();
        String[] name = new String[no];
        int i;
        for(i = 0; i < no; i++){
            name[i] = sc.next();
        }
        System.out.println("==========");
        for(i = 0; i < no; i+=2){
            System.out.println(name[i]);
        }
        for(i = no - 1 - (no % 2); i > 0; i-=2){
            System.out.println(name[i]);
        }
    }

}
