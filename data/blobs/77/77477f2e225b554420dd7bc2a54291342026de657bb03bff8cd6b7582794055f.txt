package methodpractice;

/**
 *
 * @author iraki
 */
//import java.util.Scanner;
public class SumOfallElements {

    static int sum(int...a)
    {
        if(a.length==0)
            return Integer.MIN_VALUE;
        int sum=0;
        for(int x:a)
        {
            sum+=x;
        }
        return sum;
    }
    
    public static void main(String[] args) {
        
        //Scanner s=new Scanner(System.in);
        System.out.println(sum(10,-5,2,8,9,24,0));
    }

}
