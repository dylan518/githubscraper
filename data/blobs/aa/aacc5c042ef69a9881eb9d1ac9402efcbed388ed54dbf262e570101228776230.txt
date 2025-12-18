package evtpsrqpack.loopstask;

import java.util.Scanner;

public class LoopsTaskCls3 {
    public static void main(String[] args) {
        Scanner scanner= new Scanner(System.in);
        System.out.println("esasi daxil edin");
        int a = scanner.nextInt();
        System.out.println("quvveti daxil edin");
        int b = scanner.nextInt();
        int netice = 1;

        for (int i =1; i<=b;i++){
            netice =netice*a;

        }
        System.out.println(netice);
    }
}
