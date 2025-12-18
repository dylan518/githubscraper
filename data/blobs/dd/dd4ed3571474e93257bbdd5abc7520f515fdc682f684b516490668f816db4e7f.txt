package JavaOOPsConceptsAndBasics;

class Test{
    final int x=100; //final keyword applied on variable
}

public class FinalKeyword {
    public static void main(String[] args) {
        Test t = new Test();
      //  t.x=200; //Not possible after applying final keyword
        System.out.println(t.x);
    }
}
