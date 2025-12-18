public class subString {
    public static String substring(String str,int si,int ei){
        String substr ="";
        for(int i=si; i<ei; i++){
            substr += str.charAt(i);
        }
        return substr;
    }
    public static void main(String args[]){
        String s="helloworld";
        // System.out.println(s.substring(5,10));
        System.out.println(substring(s,5,10));

    }
    
}
