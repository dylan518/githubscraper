import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Set<Integer> newSet = new HashSet<>();
        newSet.add(123);
        newSet.add(124);
        newSet.add(125);
        newSet.add(126);

        System.out.println("Các số chia hết cho 3 trong tập hợp là:");
        for (Integer num : newSet) {
            if (isDivisibleByThree(num)) {
                System.out.println(num);
            }
        }
    }

    private static boolean isDivisibleByThree(int number) {
        while (number > 2) {
            number -= 3;
        }
        return number == 0;
    }
}


