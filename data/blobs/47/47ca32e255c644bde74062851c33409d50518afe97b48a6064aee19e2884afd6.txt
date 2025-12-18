public class ex8 {

    public static int[] findDifferences(int[] a) {
        double sum = 0;
        for (int value : a) {
            sum += value; // Sum all elements in the array
        }

        double average = sum / a.length; // Calculate the average

        int maxDifference = Integer.MIN_VALUE;
        int minDifference = Integer.MAX_VALUE;

        for (int value : a) {
            int difference = (int) Math.abs(average - value); // Calculate the absolute difference from the average
            maxDifference = Math.max(maxDifference, difference); // Update max difference if necessary
            minDifference = Math.min(minDifference, difference); // ~~     min ~~
        }

        return new int[]{maxDifference, minDifference}; // Return the max and min differences
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5}; // Sample array for demonstration
        int[] differences = findDifferences(array); // Calculate differences
        System.out.println("Max Difference: " + differences[0]); // Output the max difference
        System.out.println("Min Difference: " + differences[1]); // ~~         min ~~
    }
}