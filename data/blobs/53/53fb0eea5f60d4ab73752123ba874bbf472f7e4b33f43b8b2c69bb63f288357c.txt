package Replit_questions;

import java.util.Scanner;

public class CatAndDog {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.nextLine().toLowerCase();

        int numDog = 0;
        int numCat = 0;
        for (int i = 0; i < str.length()-2 ; i++) {

            String temp = ""+str.charAt(i)+str.charAt(i+1)+str.charAt(i+2);

            if(temp.equalsIgnoreCase("dog")){
                numDog ++;
            }if(temp.equalsIgnoreCase("cat")){
                numCat++;
            }

        }

        System.out.println(numCat==numDog);// burada numcar==numdog oluyorsa boolean gibi isliyor ve true yaziyor
        // eger catler dog lara esit degilsede otomatik olarak false yaziyor.


/*
Print true if the string "cat" and "dog" appear the same number of times in the given string word.

Example:

input: catdog
output: true
Example:

input: catcat
output: false
Example:

input: cat-cheetah-dog-cat
output: false
 */
    }}