package randomjavaprograme;

public class xyz {
    public static void main(String[] args) {
        int ans = numberconversion(new int[]{1,2,3,4} , 1) ;
        System.out.println(ans);
    }

    static int numberconversion(int[] num, int  k ){
        StringBuilder number = new StringBuilder();
        for (int i = 0; i < num.length; i++) {
            number.append(num[i]);
        }
        int result = Integer.parseInt(number.toString()) + k ;
        return result ; 
    }
}
