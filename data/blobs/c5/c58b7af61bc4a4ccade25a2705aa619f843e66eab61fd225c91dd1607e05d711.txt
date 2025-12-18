
class A{//we can't make outer class static it will give error. we can make inner class static

    int age;
    public void show(){
        System.out.println("In Show");
    }
    static class B{
        public void config(){
            System.out.println("In Config");
        }
    }
}

class X{
    public void show(){
        System.out.println("In X Show");
    }
}
class Y extends X{
    public void show(){
        System.out.println("In B Show");
    }
}


abstract class H{
    public abstract void show();
}

public class Hello{
    public static void main(String[] args) {
        A obj=new A();
        obj.show();

        // A.B obj1=obj.new B();//we need object to run non static class
        //if we dont need an object then make class static
        A.B obj1=new A.B();
        obj1.config();



        //Anonymous inner class
        // X obj2=new Y();
        // obj2.show();
        //when we compile the code every classes makes it .class file
        //if we want to use some classes for particular reason than why we make the new class for that we use below method

        X obj3=new X(){//by this we can use some particular work and we dont need to create extra class it is inner class and it is known as anonymous inner class
            public void show(){//new implementation
                System.out.println("In New Show");
            }
        };
        obj3.show();



        H obj4=new H(){
            public void show(){//providing the implementation of abstract class here in anonymous inner class
                System.out.println("In H Show");
            }
        };
        obj4.show();
 
    }
}
