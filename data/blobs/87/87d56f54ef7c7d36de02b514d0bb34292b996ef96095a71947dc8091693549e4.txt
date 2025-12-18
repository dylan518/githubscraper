// 1. Compile-Time Polymorphism in Java
// 1.1 Method Overloading
// When there are multiple functions with the same name but different parameters then these functions are said to be overloaded. Functions can be overloaded by changes in the number of arguments or/and a change in the type of arguments.
// Java Program for Method overloading
// By using Different Types of Arguments 
class Helper {
    // Method with 2 integer parameters
    static int multiply(int a, int b) {
        return a * b;
    }

    // Only changing the return type cannot results in function overloading
    // static double multiply(int a, int b) {
    // return a * b;
    // }

    // Method 2 With same name but with 2 double parameters
    static double multiply(double a, double b) {
        return a * b;
    }

    // Java program for Method Overloading
    // by Using Different Numbers of Arguments
    static int multiple(int a, int b, int c) {
        return a * b * c;
    }
}

// 2. Runtime Polymorphism in Java
// It is also known as Dynamic Method Dispatch. It is a process in which a
// function call to the overridden method is resolved at Runtime. This type of
// polymorphism is achieved by Method Overriding. Method overriding, on the
// other hand, occurs when a derived class has a definition for one of the
// member functions of the base class. That base function is said to be
// overridden.
// Java Program for Method Overriding
class Parent {
    void print() {
        System.out.println("Parent Class");
    }
}

class SubClass1 extends Parent {
    @Override
    void print() {
        System.out.println("SubClass 1");
    }

    void printHello() {
        System.out.println("Hello");
    }
}

class SubClass2 extends Parent {
    @Override
    void print() {
        System.out.println("SubClass 2");
    }

    void printWorld() {
        System.out.println("World");
    }
}

public class PolymorphismImplementation {
    public static void main(String[] args) {
        System.out.println(Helper.multiply(2, 4));
        System.out.println(Helper.multiply(5.5, 6.3));
        System.out.println(Helper.multiple(2, 7, 3));
        // ----------------------------------------------
        Parent a;
        a = new SubClass1();
        a.print();
        a = new SubClass2();
        a.print();
    }
}
