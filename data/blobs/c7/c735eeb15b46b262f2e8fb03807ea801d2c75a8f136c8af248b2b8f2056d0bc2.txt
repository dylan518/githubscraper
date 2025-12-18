package Scope;

class C2{
    int v = 10;
    void m(){
        int v = 20;
        System.out.println(v);
    }
}

public class ScopeDemo8 {
    public static void main(String[] args) {
        C2 c = new C2();
        c.m();
    }
}
