package pack2;
import pack1.A;     //to access pack1
public class C extends A{          //A is parent C is child
    public void m6(){System.out.println("pack2 m6 public");}

    public static void main(String[] args){
        C c1=new C();    
        c1.m1();
        c1.m3();
        
        
        /*A a2=new A();          //A is from A.java
        a2.m1();*/
    }
}
