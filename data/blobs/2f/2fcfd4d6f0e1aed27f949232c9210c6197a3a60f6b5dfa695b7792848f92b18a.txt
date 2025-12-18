import java.util.*;
import java.io.*;

public class p11047 {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // n : 동전 종류 개수, k : 동전 가치의 합
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // coins : 각 동전의 가치를 내림차순으로 가지는 배열 
        int[] coins = new int[n];
        for(int i = n-1;i>=0;i--){
            coins[i] = Integer.parseInt(br.readLine());
        }

        // cnt : k원을 만드는데 필요한 최소 동전 개수
        int cnt = 0;

        // coins 배열을 돌면서 cnt에 k/coin 값을 더해주고, k를 k%coin 으로 바꿔준다.
        for(int coin:coins){
            if(coin<=k){
                cnt += k/coin;
                k = k%coin;
            }
            if(k==0) break;
        }

        // cnt 값 출력
        System.out.println(cnt);
    }
}
