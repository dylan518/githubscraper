import java.util.*;
class Student{
     String name;
     int roll;
     public Student(String n,int r){
        name=n;
        roll=r;
     }
     Student(){}

        public void returndata(){
        System.out.println("Name : "+name);
        System.out.println("Roll Number :"+roll);
        
    }

    

}




public class App {
    public static void main(String[] args) throws Exception {
       Student c1= new Student();
       
       
       int a;
       String b;
       Scanner sc= new Scanner(System.in);
       System.out.print("enter name =");
       b=sc.nextLine();

       c1.name=b;
       System.out.print("enter roll =");
       a=sc.nextInt();
       c1.roll=a;
       c1.returndata();
       sc.close();

    
    System.out.print(c1.name);
}
}
