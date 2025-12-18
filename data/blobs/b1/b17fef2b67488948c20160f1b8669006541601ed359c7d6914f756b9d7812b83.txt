package practice1;

public class ArrayMethodPractice3 {
    public static void main(String[] args) {
        int[] arr = {13, 90, 10, 79, 101, 25, 123, 38, 5, 16, 64, 55, 17};
        int[] arr2 = {38, 118, 26, 17, 41, 53, 10, 88, 92, 102, 67, 22, 55};
        // commonメソッドの呼び出し
        System.out.println("共通する数値の個数：" + common(arr, arr2));
    }
    // ここにcommonメソッドを定義してください。
    public static int common(int[] array, int[] array2){
        int num = 0;

        for (int i = 0; i< array.length; i++){
            for (int j = 0; j < array2.length; j++) {
                if (array[i] == array2[j]) {
                    num = num + 1;
                }
            }
        }

        return num;
    }
}
