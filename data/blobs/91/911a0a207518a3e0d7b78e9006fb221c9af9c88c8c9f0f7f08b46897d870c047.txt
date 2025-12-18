import java.util.*;

public class Main{

    public static void main(String[] args){
    
        Calendar c = Calendar.getInstance();
        TimeZone ny = TimeZone.getTimeZone("America/New_York");
        c.setTimeZone(ny);
        System.out.println(c.getTime());
    }
}
