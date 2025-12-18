import java.util.ArrayList;

public class rotateBits {
    public static void main(String[] args) {
    
    }

     ArrayList<Integer> rotate(int N, int D)
    {
        // your code here
        ArrayList<Integer> ans = new ArrayList<>();
        D %= 16;
        int a = (N << D | (N >> (16-D))) & 65535;
        int b = (N >> D | (N << (16-D))) & 65535;
        ans.add(a);
        ans.add(b);
        return ans;
    }


}
