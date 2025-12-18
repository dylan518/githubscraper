package exam;

public class TrueTest {
    public static boolean twoMoreTrue(String... args) {
        
        assert args.length >= 3;

        int trueCount = 0;

        for(int i = 0;i<3;i++){
            trueCount += Boolean.valueOf(args[i]) ? 1 : 0;
        }


        return trueCount >= 2;
    }

    public static void main(String[] args) {
        System.out.println(twoMoreTrue(args));
    }
}

// $ java TrueTest true True AnythingButTrueIsFalse
// true
// $ java TrueTest 0 x true true true
// false
// $ java TrueTest true true
// Exception in thread "main" java.lang.IllegalArgumentException: TrueTest: three boolean arguments
// required
// ...
