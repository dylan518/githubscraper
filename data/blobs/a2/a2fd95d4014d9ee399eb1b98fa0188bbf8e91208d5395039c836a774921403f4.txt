public class BinaryToDecimal {
    public static void main(String[] args) {

        //https://youtu.be/XtPGieo4nhs
        
        long binary = 110110111;


        System.out.println(convertToDecimal(binary));
    }

    //2^1*
    static double  convertToDecimal(long binary){
        int i = 0;
        double decimal = 0;

        while (binary > 0) {
            long reminder = binary%10;
            decimal = decimal + (reminder * Math.pow(2, i));
            binary = binary/10;
            i++;
        }
        return decimal;
    }
}
