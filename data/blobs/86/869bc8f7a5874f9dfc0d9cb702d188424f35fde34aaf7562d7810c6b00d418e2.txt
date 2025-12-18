package codeptit;
import java.util.Scanner;
public class XauNhiPhan {
    static long[] f = new long[94];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        f[1] = 1; f[2] = 1;
        for (int i = 3; i <93; i++) f[i] = f[i-2] + f[i-1];
        int t = sc.nextInt();
        while (t-- >0) {
            int n = sc.nextInt();
            long k = sc.nextLong();
            System.out.println(Try(k,n));
        }
    }
    public static String Try(long k, int n) {
        if (n == 1) return "0";
        if (n == 2) return "1";
        if (k <= f[n-2] ) return Try(k,n-2);
        return Try(k -f[n-2],n-1);
    }
}