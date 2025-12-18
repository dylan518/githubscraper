package Java;
class Super{
    public void meth(){
        System.out.println("I am a overridding method of Super class");
    }
}
class Sub extends Super{
    @Override
    public void meth(){
        System.out.println("I am a overridding method of Sub class");
    }
}
public class MethodOverridding {
    public static void main(String[] args){
        Sub ob=new Sub();
        ob.meth();
    }
}
// If a method is overrrided then the code which is present in the derived or sub class is executed.