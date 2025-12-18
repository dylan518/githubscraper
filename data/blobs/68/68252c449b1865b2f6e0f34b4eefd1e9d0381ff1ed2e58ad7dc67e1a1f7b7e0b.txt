package Day12.Casting.Upcasting ;


// Upcasting 
// Upcasting is the process of type casting Child class object to parent class Object 
// we acn achieve upcasting as follow :
// Parent p = new Child() ;
//          or
// Parent p = new parent() ;
// Child c = new Child() ;
// p = c ;
// p.a                  // Accessible
// p.b                  // Accessible 
// p.c                  // Not Accessible (parent cannot access child class members)
// please observe oveririding properties in upcasting
// cant access data members of child class in upcasting
// but we can acces overrided method of child class (if no overrrided we can call parent class methods)



class First{
    int a ;
    int b ;
    void print(){
        System.out.println("First");
    }
}


class Second extends First{
    int c ;
    void print(){
        System.out.println("Second") ;
    }
    void displayRecords(){
        System.out.println("Child DisplayRecord") ;
    }
}



public class Main {
    public static void main(String[] args) {
        First f = new Second() ;
        // System.out.println(f.a) ;
        // System.out.println(f.b) ;
        System.out.println(f.c) ;
        // f.displayRecords() ;
    }
}
