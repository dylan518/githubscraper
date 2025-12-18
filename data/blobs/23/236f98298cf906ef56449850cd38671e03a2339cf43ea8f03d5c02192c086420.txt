package Practice;



public class Array {
    public static void main(String[] args) {
        //Write a code where you define an integer array with size/length of 10
        //even numbers starting from 90
        //90,92,94,96,98,100,102,104,106,108

        int[] Array =new int[10];
        
        int start = 90;
        for (int i = 0; i < Array.length ; i++) {
            Array[i] = start;
            start += 2;
        }
        for (int i = 0; i <Array.length ; i++) {
            System.out.println("The value in index: "+" is: "+Array[i]);

        }

    }
}
