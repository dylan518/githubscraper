public class PrintAllPossibleStringsCombinationsWithSpaces {

    public static void main(String[] args) {
        String str = "ABC";

        int n = (int)Math.pow(2,str.length()-1);
        int length=str.length();

        for(int i=0;i<n;i++){
            for(int j=0;j<length;j++){
                System.out.print(str.charAt(j));
                if((i & (1 << j)) > 0 ){
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
