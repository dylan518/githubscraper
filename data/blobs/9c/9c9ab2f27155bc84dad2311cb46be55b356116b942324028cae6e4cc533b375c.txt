public class BinarySearch {
    static int binarySearch(int[] arr, int low, int high, int target) {
        if (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                return binarySearch(arr, mid + 1, high, target);
            } else {
                return binarySearch(arr, low, mid - 1, target);
            }
        }
        return -1;  
    }

    public static void main(String[] args) {
        int[] array = {2, 4, 6, 8, 10, 12, 14, 16};
        int target = 10;
        int result = binarySearch(array, 0, array.length - 1, target);

        if (result == -1) {
            System.out.println("Element not found in the array.");
        } else {
            System.out.println("Element found at index: " + result);
        }
    }
}