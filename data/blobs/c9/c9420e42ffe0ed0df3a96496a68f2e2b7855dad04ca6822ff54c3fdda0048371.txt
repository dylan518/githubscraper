package com.tutorial;

public class Main {

    public static void main(String[] args){

        //Program untuk konversi data numerik
        int numInt = 450; //Size integer adalah 4 byte
        System.out.println("Angka Integer = " + numInt + ", Nilai max dari int -> " + Integer.MAX_VALUE);

        long numLong = numInt; //Size long lebih besar dari integer
        System.out.println("Angka Long = " + numLong + ", Nilai max dari long -> " + Long.MAX_VALUE);

        //Perlu melakukan casting jika nilai data lebih besar dari tipe data
        byte numByte = (byte) numInt; //Size byte lebih kecil dari integer
        System.out.println("Angka Byte = " + numByte + ", Nilai max dari byte -> " + Byte.MAX_VALUE);

        System.out.println("\n\n");

        //Mengcasting hasil operasi pembagian
        int a = 25;
        int b = 6;
        int hasil = a / b;

        // 1. Tetap membiarkan tipe datanya integer
        System.out.println("Hasil 25 : 6 = " + hasil + " (integer) ");

        // 2. Mengubah variabel hasil menjadi float
        float hasilBagi = a / b;
        System.out.println("Hasil 25 : 6 = " + hasilBagi + " (Float) ");

        // 3. Mengcasting variabel angka hasil menjadi float
        float hasilCast = (float) a / b;
        System.out.println("Hasil 25 : 6 = " + hasilCast + " (Float) ");
    }
}
