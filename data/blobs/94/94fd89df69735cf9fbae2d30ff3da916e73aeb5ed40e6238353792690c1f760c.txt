package questions;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

/**
 *
 * 描述
 * 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
 *
 *
 * 数据范围： 1 \le n \le 2 \times 10^{9} + 14 \1≤n≤2×10
 * 9
 *  +14
 * 输入描述：
 * 输入一个整数
 *
 * 输出描述：
 * 按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
 *
 * 示例1
 * 输入：
 * 180
 * 复制
 * 输出：
 * 2 2 3 3 5
 */
public class PrimeFactor {
    public static void main(String[] args) {
        System.out.println("请输入整数：");
        Scanner scanner = new Scanner(System.in);
        int i = scanner.nextInt();
        int n = 2;
        List<Integer> list = new ArrayList<>();
        while (n<=i) {
            int tmp = i;
            while(tmp % n == 0) {
                list.add(n);
                tmp = tmp / n;
            }
            i = tmp;
            n++;
        }
        String res = "";
        Iterator<Integer> iterator = list.iterator();
        while(iterator.hasNext()) {
            Integer next = iterator.next();
            res += next + " ";
        }
        System.out.println("输出：" + res);
    }
}
