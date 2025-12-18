package recursion;

public class Count {

    public void countRec(int start){
        if(start<=5){
            System.out.println(start);
            start++;
            countRec(start);
        }
    }

    public static void main(String[] args) {
        System.out.println("this is recursion code ");
        int count=0;
        Count c= new Count();
        c.countRec(count);
    }
}
