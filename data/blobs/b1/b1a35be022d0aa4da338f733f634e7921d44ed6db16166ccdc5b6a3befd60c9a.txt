package days42;

public class varArgs {

    public static void main(String[] args) {

        sum(1, 2, 3, 4, 5);

        sum2(1, 2, 3, 4, 5);

        int[] array = {1, 2, 3, 4, 5};
        sum3(array);

        concatStr("Mercedes","Bmw","Proton","Jaguar");



    }

    public static void sum(int... numbers) {

        int sum = 0;

        for (int value : numbers) {
            sum = sum + value;
        }
        System.out.println(sum);

    }

    public static void sum2(int... numbers) {

        int sum = 0;

        for (int i = 0; i < numbers.length; i++) {

            sum = sum + numbers[i];
        }
        System.out.println(sum);
    }

    public static void sum3(int[] numbers) {

        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            sum = sum + numbers[i];
        }
        System.out.println(sum);

    }

    public static void concatStr(String... str) {

        String str2 = "";

        for (String value : str) {
            str2=str2+value.charAt(1);
        }
        System.out.println(str2);

    }


}





