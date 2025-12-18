class D {
    //main method 
    public static void main(String[] args) {
        Float a = 2.3f;
        Byte b = 3;
        //float + byte => float

        Object c = a + b;

        System.out.println(c instanceof Float);
    }    
}
/*OUTPUT:true
true output aya kyuki float or byte mil k float banate h,or float object k sath is-a relationship
pass krta h to true output produce hoga...
*/