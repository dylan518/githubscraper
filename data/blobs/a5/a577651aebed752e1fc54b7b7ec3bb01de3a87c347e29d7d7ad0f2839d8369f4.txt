import java.util.Arrays;

public class Q13 {
    public static boolean binarySearch(int[] arr, int target) {

        int s = 0;
        int e = arr.length - 1;
        while (s <= e) {
            int mid = s + (e - s) / 2;
            if (arr[mid] == target) {
                return true;
            } else if (arr[mid] < target) {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        return false;
    }

    public static void main(String[] args) {

        int[] aliceSizes = { 1, 1 }, bobSizes = { 2, 2 };

        int aliceTotal = 0;
        int bobTotal = 0;
        for (int candies : aliceSizes)
            aliceTotal += candies;
        for (int candies : bobSizes)
            bobTotal += candies;

        Arrays.sort(bobSizes);

        int m = aliceSizes.length;

        for (int i = 0; i < m; i++) {

            int target = (bobTotal + 2 * aliceSizes[i] - aliceTotal) / 2;

            if (binarySearch(bobSizes, target)) {

                // return new int[] { aliceSizes[i], target };
            }
        }

        // return new int[0];
    }
}
