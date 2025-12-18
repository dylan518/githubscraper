//USACO 2015 December Contest, Silver
//Problem 3. Breed Counting
//java solution
import java.util.*;
import java.io.*;


public class CodeForces {
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("bcount.in"));
        PrintWriter pw = new PrintWriter("bcount.out");
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());
        Position [] arr = new Position[N+1];
        arr[0]=new Position(0,0,0);
        int a = 0;
        int b =0;
        int c =0;

        for(int i=1; i<=N; i++)
        {

            int num=Integer.parseInt(br.readLine());
            if(num==1)
                a++;
            else if(num==2)
                b++;

            else
                c++;
            arr[i] = new Position(a,b,c);
        }
        for(int i=0; i<Q; i++)
        {
            st = new StringTokenizer(br.readLine());
            int first = Integer.parseInt(st.nextToken());
            int sec = Integer.parseInt(st.nextToken());
            pw.println((arr[sec].num1 - arr[first-1].num1) + " " + (arr[sec].num2 - arr[first-1].num2) + " " + (arr[sec].num3 - arr[first-1].num3));
        }
        pw.close();


        }
        private static class Position
        {
            int num1;
            int num2;
            int num3;
            public Position(int num1, int num2, int num3)
            {
                this.num1= num1;
                this.num2 = num2;
                this.num3 = num3;
            }
        }

}
