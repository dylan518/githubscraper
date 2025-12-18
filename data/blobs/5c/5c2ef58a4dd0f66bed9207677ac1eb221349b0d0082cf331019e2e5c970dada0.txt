package math_problems;

public class FindMissingNumber {

    /** INSTRUCTIONS
     * Write a method to find the missing number from the array.
     */

    public static void main(String[] args) {
        int[] array = new int[] {10, 2, 1, 4, 5, 3, 7, 8, 6};

        System.out.println(missingNum(array,10 ));

    }

    public static int missingNum(int [] array, int n){
        int sumOfArray = n * (n + 1)/ 2;

        int addArray = 0;
        for(int i = 0; i < n-1; i++){
            addArray += array[i];
        }
        return  sumOfArray - addArray;
    }
}
