package Basics;

public class MaxArrayValue {
    public static void main(String[] args) {
        int max=0;
        int[] arr= {1,5,3,8,9,2,345345,43242};
        for(int number:arr){
               if(number>max){
                     max=number;
                 }
        }
        System.out.println(max);
    }

}
