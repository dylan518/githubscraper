/**
Java ile bir sayının "Palindrom Sayı" olup olmadığını bulan bir program yapıyoruz.
Palindromik sayı, iki taraftan okunduğu zaman okunuş yönüyle aynı olan sayılardır.
Örnek: 1, 4, 8, 99, 101, 363, 4004, 9889....
**/
import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner scan=new Scanner(System.in);
	    System.out.print("Sayı giriniz: ");
	    int inp=scan.nextInt();
	    if(inp<0){
	        inp*=-1;
	    }
        if(isPalindrome(inp)==true){
            System.out.print(inp+" bir Palindrom sayıdır.");
        }
        else{
            System.out.print(inp+" bir Palindrom sayı değildir.");
        }
    }
    public static boolean isPalindrome(int x){
        if(x<10){
            return true;
        }
        else{
            int half=digitnumber(x)/2;
            int digit=(int)(Math.pow(10,half));
            int first=x/digit;
            if(digitnumber(x)%2==1){
                first/=10;
            }
            int second=reverse(x%digit);
            if(first==second){
                return true;
            }
            else{
                return false;
            }
        }
    }
    public static int reverse(int x){
        int rev=0;
        while(x!=0){
            int rem=x%10;
            rev=rev*10+rem;
            x/=10;
        }
        return rev;
    }
    public static int digitnumber(int x){
        int cnt=0;
        while(x>0){
            cnt+=1;
            x/=10;
        }
        return cnt;
    }
    
}

