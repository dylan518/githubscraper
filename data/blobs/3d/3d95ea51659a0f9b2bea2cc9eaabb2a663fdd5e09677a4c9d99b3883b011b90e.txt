package 백준_1000_10000.백준_9093;

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int cycle = Integer.parseInt(br.readLine());
        for( int i=0; i< cycle; i++ ){
            StringBuilder sb = new StringBuilder();
            String[] str = br.readLine().split(" ");
            for( int j =0; j < str.length; j++ ){
                sb.append(new StringBuilder(str[j]).reverse().append(" "));
            }
            System.out.println(sb);
        }
    }
}
