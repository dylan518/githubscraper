package byLevel.Lv9_약수배수소수;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        // 배열 초기화
        int[] arr = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            arr[i] = i;
        }

        // 2 ~ 제곱근까지
        for (int i = 2; i < Math.sqrt(arr.length); i++) {
            if(arr[i] == 0) continue;
            // 예를 들어 2인 경우, 2를 제외한 2의 배수들을 제거해야 한다.
            // -> 4부터 시작해서 6 8 10 .. 이런식으로 나가야 하기 때문에 j에 i를 계속 더해준다.
            for (int j = i + i; j < arr.length; j += i) {
                arr[j] = 0;
            }
        }

        // 출력
        for (int i : arr) {
            if(i != 0) System.out.print(i + " ");
        }
    }
}
