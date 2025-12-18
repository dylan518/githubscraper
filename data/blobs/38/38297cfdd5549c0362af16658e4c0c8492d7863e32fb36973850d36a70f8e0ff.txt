package PRact;

public class PractLinear {
    static int LinearAlgo(int[] array, int target) {
        if (array.length == 0) {
            return -1;
        }
        for (int i = 0; i <array.length ; i++) {
            int element = array[i];
            if (element==target){
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] ars={-1,2,3,4,5,6,7,8,9,10,-11,-1};
        int target = -132;
        int ans  = LinearAlgo(ars,target);
        System.out.print(ans);

    }
}
