public class abhi2 {
    public static boolean isDivisible35(int num) {
        return num > 0 && num % 3 == 0 && num % 5 == 0;
    }
    public static void main(String[] args) {
        System.out.println("Main method started");
        
        int number = 15; 
        boolean result = isDivisible35(number);
        
        System.out.println("is number " + number + "is divisible by both 3 and 5 " + result);
        
        System.out.println("Main method ended");
    }
}
