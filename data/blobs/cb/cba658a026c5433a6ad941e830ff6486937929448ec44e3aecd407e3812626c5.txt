public class String_EX {
    public static void main(String[] args) {
        String message = greeting();
        System.out.println(message);

        String p_message = personal("Chetan");
        System.out.println(p_message);
    }

    private static String personal(String name) {

        String message = "Hello " + name;

        return message;

    }

    static String greeting() {
        String greet = "Hello, hope you are doing well";
        return greet;
    }
}


