import java.io.*;

public class BOJ1100 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int answer = 0;
        for(int i = 0; i < 8; i++) {
            char[] tmp = br.readLine().toCharArray();
            for(int j = i%2; j < 8; j += 2) {
                if(tmp[j] == 'F') answer++;
            }
        }
        System.out.println(answer);
    }
}