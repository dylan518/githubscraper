import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 트리 {
    static ArrayList<Integer>[] arr;
    static boolean[] deleted;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        arr = new ArrayList[t];
        deleted = new boolean[t];

        for(int i=0; i<t; i++){
            arr[i] = new ArrayList<>();
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        int root = 0;
        for(int i=0; i<t; i++){
            int n = Integer.parseInt(st.nextToken());
            if(n == -1) {
                root = i;
                continue;
            }
            arr[n].add(i);
        }
        int target = Integer.parseInt(br.readLine());
        deleted[target] = true;

        if(target == root){
            System.out.println(0);
            return;
        }
        dfs(root);

        System.out.println(answer);
    }

    public static void dfs(int now){
        if(deleted[now]) return;

        int children = 0;
        for(int i=0; i<arr[now].size(); i++){
            if(!deleted[arr[now].get(i)]) {
                dfs(arr[now].get(i));
                children++;
            }
        }

        if(children == 0){
            answer++;
        }
    }
}
