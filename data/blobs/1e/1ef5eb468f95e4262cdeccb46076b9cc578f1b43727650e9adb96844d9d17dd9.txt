import java.util.Scanner;

public class fictorial {
    public static void main(String[] args) {
       Scanner sc= new  Scanner(System.in);
       System.out.println("Enter number for fictorial:");
       int n=sc.nextInt();
       int fic=1;
       for(int i=1;i<=n;i++){
        fic=fic*i;
       }
       System.out.println("Fictorial is:"+fic);

       sc.close();
    }
}
