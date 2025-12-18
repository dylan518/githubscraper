import java.util.Scanner;

public class DeleteElementArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = {10, 20, 30, 40, 50};
        int size = arr.length;
        System.out.print("Enter element to delete: ");
        int element = sc.nextInt();
        int[] newArr = new int[size - 1];
        int index = 0;
        
        for (int i = 0; i < size; i++) {
            if (arr[i] != element) {
                newArr[index++] = arr[i];
            }
        }
        
        System.out.print("Array elements after deleting the element: ");
        for (int i = 0; i < index; i++) {
            System.out.print(newArr[i] + " ");
        }
    }
}
