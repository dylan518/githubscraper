package rutuja.constructor;

public class NoParamConstructor {
    int a;
    float b;
    //No Parameter/args Constructor
    public NoParamConstructor(){
        a=20;
        b=10.8f;
        System.out.println("a is ="+a);
        System.out.println("b is ="+b);
    }
    public void NoParameterConstructor(){
        System.out.println("I am in NoParameterConstructor()method");
    }

    public static void main(String[] args) {
        NoParamConstructor obj=new NoParamConstructor();
        obj.NoParameterConstructor();

    }
}
