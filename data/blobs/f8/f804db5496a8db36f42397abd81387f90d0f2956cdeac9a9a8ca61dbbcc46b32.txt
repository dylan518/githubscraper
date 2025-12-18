
package SUPER_KEYWORD;


public class SuperMethod {
    
    void eat()
    {
        System.out.println("Eating...");
    }   
    void Call()
    {
        System.out.println("Calling can be any sound.");
    }
    void sound()
    {
        System.out.println("Any kind of sound.");
    }
}
class Dog extends SuperMethod{
    
    void eat()
    {
        System.out.println("Eating Bread...");
    }
    void sound()
    {
        System.out.println("Meaooo...");
    }
    void work()
    {
        System.out.println("Super Keyword should be used if subclass contains the same method as parent class."
                           +" In other words, it is used if method is overridden.");
        eat();
        super.eat();
    }
}

class TestSuperMethod{
    
    public static void main(String[] args) {
        
        Dog obj1 = new Dog();
        obj1.work();
        obj1.Call();
        
        SuperMethod obj = new SuperMethod();
        obj.eat();
        obj=obj1;
        obj.eat();
        //obj.sound();// We can only access subclass method from super class using overide it.
        //obj.work();
    }
}
