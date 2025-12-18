package com.project.vowelcounter;

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        // deklarasi variabel inputUser sebagai scanner untuk membaca input dari pengguna
        Scanner inputUser;
        // variabel sentence untuk menyimpan kalimat yang akan dihitung huruf-hurufnya
        String sentence;
        // variabel untuk menghitung jumlah huruf vokal, konsonan, whitespace, dan karakter lain pada kalimat
        int vowelCount, vowelConsonant, vowelWhitespace, vowelLetter;
        // variabel untuk menyimpan karakter pada setiap iterasi
        char ch;

        // pengambilan text user ke terminal
        inputUser = new Scanner(System.in);
        System.out.print("Masukan text : ");
        sentence = inputUser.nextLine();

        // inisialisasi
        vowelCount = 0;
        vowelConsonant = 0;
        vowelWhitespace = 0;
        vowelLetter = 0;

        // logika penghitungan huruf vokal,konsonan,spasi,dan karakter khusus
        for(int i = 0; i < sentence.length(); i++){
            ch = sentence.charAt(i);
            if(isVowel(ch)){
                vowelCount++;
            }else if(isConsonants(ch)){
                vowelConsonant++;
            }else if(Character.isWhitespace(ch)){
                vowelWhitespace++;
            }else if(Character.isLetter(ch)){
                vowelLetter++;
            }else{
                vowelLetter++;
            }
        }

        // output
        System.out.println("Jumblah huruf Vokal pada text adalah : " + vowelCount);
        System.out.println("Jumblah huruf Konsonan pada text adalah : " + vowelConsonant);
        System.out.println("Jumblah karakter Whitespace/Spasi pada text adalah : " + vowelWhitespace);
        System.out.println("Jumblah Karakter Khusus pada text adalah : " + vowelLetter);
    }

    // mathod untuk membedakan mana karakter khusus, huruf vokal, konsonan, dan spasi
    public static boolean isVowel(char ch){
        return "aiueoAIUEO".indexOf(ch) != -1;
    }
    public static boolean isConsonants(char ch) {
        return Character.isLetter(ch) && !isVowel(ch);
    }
}
