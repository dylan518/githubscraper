package RaghuSir.Recursion;

public class Pro29 {
    static int evenlyDivides(int n){
        do{
            int d = n % 10;//2
            if(n % d == 0) return d;
            else if (n / d == 1) return 0;
            n /= 10;
        }while(n != 0);
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(evenlyDivides(12));
    }
}

