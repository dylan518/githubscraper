import java.util.Scanner;

public class BaiTh1 {
    public static void main(String[] args) {
        // Giải chương trình bậc nhất a + bx = 0
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhập số a: ");
        int a = sc.nextInt();
        System.out.print("Nhập số b: ");
        int b = sc.nextInt();
        // th1
        if(a == 0 && b == 0) {
            System.out.println("Phương trình vô số nghiệm.");
        } else if (a == 0 && b != 0 || b == 0 && a != 0) {
            System.out.println("Phương trình vô nghiệm.");
        } else {
            System.out.println("X có giá trị là: " + -a/b);
        }
    }
}
