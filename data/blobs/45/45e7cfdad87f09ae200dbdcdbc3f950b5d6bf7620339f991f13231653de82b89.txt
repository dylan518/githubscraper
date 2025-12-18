import java.util.Scanner;

public class palindromicNumber {
    public static void main(String[] args) {
        //回文数
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入需要判断的数字:");
        int number = sc.nextInt();
        int count = 0;//计算循环的次数，同样记录数组的元素个数
        int[] array = new int[100];//定义有100个元素的数组
        while (number > 0) {
            //记录每一位数字
            array[count] = number % 10;
            //更新计数器count
            count++;
            //更新number数值
            number=number/10;
        }
        //对数组的奇偶进行判断
        boolean t = ((count + 1) % 2 == 0);
        if (t) {
            //元素个数为奇数
            for (int i = 0, j = count-1; i<=j; i++, j--) {
                if (array[i] != array[j]) {
                    //不满足条件时
                    System.out.println("此数字不是回文数");
                    return;
                }
            }
            System.out.println("此数字是回文数");
        } else {
            //元素个数为偶数
            for (int i = 0, j = count-1; i<=j; i++, j--) {
                if (array[i] != array[j]) {
                    //不满足条件时
                    System.out.println("此数字不是回文数");
                    return;
                }
            }
            System.out.println("此数字是回文数");
        }
    }
}