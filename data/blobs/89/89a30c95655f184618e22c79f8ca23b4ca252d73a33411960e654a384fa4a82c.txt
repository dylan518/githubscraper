import java.io.*;
import java.util.*;


class Pair{
    int x,y;
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    public static int n,m;
    public static int[][] arr;
    public static ArrayList<Pair> colored;

    public static Pair[] dir = {new Pair(0,1),new Pair(0,-1),new Pair(1,0),new Pair(-1,0)};
    public static boolean[][] visited;


    public static void coloring (int value, Pair st){
        if (visited[st.x][st.y]){
            return ;
        }
        visited[st.x][st.y] = true;

        for (int i=0; i<4; i++){
            Pair next = new Pair(st.x+dir[i].x, st.y+dir[i].y);
            if (next.x<n && next.y<m && next.x>=0 && next.y>=0 && !visited[next.x][next.y] && Math.abs(arr[next.x][next.y]-arr[st.x][st.y]) <= value){
                coloring(value,next);
            }
        }
    }

    public static boolean is_possible(int value){
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                visited[i][j] = false;
            }
        }

        coloring(value, colored.get(0));
        
        for (int i=1; i<colored.size(); i++){
            Pair curr = colored.get(i);
            if (!visited[curr.x][curr.y]){
                return false;
            }
        }

        return true;
        
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());

        arr = new int[n][m];
        visited = new boolean[n][m];
        colored = new ArrayList<>();

        for (int i=0; i<n; i++){
            stk = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++){
                arr[i][j] = Integer.parseInt(stk.nextToken());
                
            }
        }

        for (int i=0; i<n; i++){
            stk = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++){
                if (Integer.parseInt(stk.nextToken())==1) colored.add(new Pair(i,j));                
            }
        }

        int st = 0;
        int end = (int)Math.pow(10,9);
        int ans = end;

        while (st<=end){
            int mid = (st+end)/2;

            if (is_possible(mid)){
                end = mid-1;
                ans = Math.min(ans,mid);
            } else{
                st = mid+1;
            }
        }

        System.out.println(ans);

    }
}