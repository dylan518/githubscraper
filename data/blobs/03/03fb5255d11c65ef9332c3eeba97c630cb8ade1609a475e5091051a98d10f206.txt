package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class b2212 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sensors = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());
        int[] pos = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(pos);
        Integer[] diff = new Integer[sensors-1];
        for(int i=1;i<sensors;i++){
            diff[i-1] = pos[i]-pos[i-1];
        }
        Arrays.sort(diff, (d1, d2)-> {
            return d2 - d1;
        });
        int total=0;
        for(int i=K-1;i<diff.length;i++){
            total += diff[i];
        }
        System.out.println(total);
    }
}
