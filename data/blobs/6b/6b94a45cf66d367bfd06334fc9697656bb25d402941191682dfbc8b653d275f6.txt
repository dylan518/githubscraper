public class palindromeNumber {
    
    public static void main(String[] args) {
        int n=121;
        int rev=0,temp;
        temp = n;
        while (temp > 0) {
            rev = (rev*10) + (temp % 10);
            temp /=10;
        }

        System.out.println(rev);
    }
}
