public class Bool {
    public static void main(String[] args) {
        boolean isRight = true;//Declaring a boolean
        int x = 10;
        System.out.println(x > 15);//Checking using boolean, any sign can be used
        int myAge = 25;
        int votingAge = 18;

        if (myAge >= votingAge) {//Boolean in an if statement
            System.out.println("Old enough to vote!");
        } else {
            System.out.println("Not old enough to vote.");
        }
    }
}
