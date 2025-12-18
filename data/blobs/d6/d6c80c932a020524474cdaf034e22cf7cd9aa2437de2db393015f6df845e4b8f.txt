import java.util.*;

public class Array_sorting {

    public static int removeDuplicates(int[] nums) {
        int j = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[j]) {
                nums[j + 1] = nums[i];
                j++;
            }
        }
        return j + 1;
    }

    public static void main(String args[]) {
        int[] arr = { 1, 1, 2, 2, 3, 3, 4, 4 };
        System.out.println(removeDuplicates(arr));
        String str = "arnab pratihar";
        String[] str1 = (str.split(" "));
        System.out.println(str1[str1.length - 1].length());
    }

}
