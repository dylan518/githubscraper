import java.util.*;
public class foverloadingarea
{
    public static void main(String[]args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter c for area of circle, s for area of square and r for area of rectangle");
        char area=sc.next().charAt(0);
        switch(area)
        {
            case 'c':
                System.out.println("Enter the radius of the circle");
                double radius=sc.nextDouble();
                area(radius);
                break;
            case 's':
                System.out.println("Enter the measurements of the sides of the square");
                int side=sc.nextInt();
                area(side);
                break;
            case 'r':
                System.out.println("Enter the length and the breadth of a rectangle");
                int l=sc.nextInt();
                int b=sc.nextInt();
                area(l,b);
                break;
            default:
                System.out.println("Please enter a valid shape to find the area of");
        }
    }
    static void area(double ra)
    {
        double area=(22/7.0)*ra*ra;
        System.out.println("The area of the circle is"+area);
    }
    static void area(int s)
    {
       int area1= s*s;
       System.out.println("The area of the square is"+area1);
    }
    static void area(int length, int breadth)
    {
        int area=length*breadth;
        System.out.println("The area of a rectangle is"+area);
    }
}