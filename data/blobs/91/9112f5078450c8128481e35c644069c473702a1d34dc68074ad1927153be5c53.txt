package day_45_review.inheritance;

public class FinalKeyWord {

    //Final keyword: it means constant/değiştirilemez

    //final variable
//      we initialize in same statement or
//      we initialize in constructor or
//      we initialize in init block


    //statement
    final double PI = 3.14;
    final double PI2;
    final double PI3;
    final static double PI4;

    //constructor
    FinalKeyWord(){
        PI2=3.14;
    }

    //init block
    {
        PI3=3.14;
    }

    static {
        PI4=3.14;
    }

    //method
    //can not be overriden

    //class
    //can not be inherited
    //immutable consept. For instance String class, being final is needed

}
//final class A{//
//
//}
//class Sub extends A{
//
//}
