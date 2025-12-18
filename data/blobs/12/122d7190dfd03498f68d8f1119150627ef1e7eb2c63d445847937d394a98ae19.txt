import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        System.out.println(recursive(n, 0));

    }

    public static int recursive(int n, int count) {
        if (n == 1) {
            return count;
        }

        if (n % 2 == 0) {
            return recursive(n / 2, count + 1);
        } else {
            return recursive(n / 3, count + 1);
        }
    }

}