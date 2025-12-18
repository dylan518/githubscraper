package _11_List;

import java.util.ArrayList;
import java.util.List;

public class C04_squareOfNums {
    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>();
        nums.add(5);
        nums.add(3);
        nums.add(0, 7);
        nums.add(2, 8);

        for (int i = 0; i < nums.size(); i++) {
            nums.set(i, nums.get(i) * nums.get(i));
        }
        System.out.println("Square of the numbers in the given list = " + nums);
    }
}

