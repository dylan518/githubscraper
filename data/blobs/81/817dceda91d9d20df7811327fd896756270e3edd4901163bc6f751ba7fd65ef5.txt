package stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class anymatch {
    public static void main(String[] args) {
        // creating a list
        List<Integer>list= Arrays.asList(3,4,6,8,5,20,16,15);

//        boolean answer = list.stream().anyMatch(n
//                -> (n * (n + 1)) / 4 == 5);

//        System.out.println(answer);

        // Creating a Stream of Strings
        Stream<String> stream = Stream.of("geeks", "for"
                , "GeeksforGeeks");

        boolean answer = stream.anyMatch(str -> Character.isUpperCase(str.charAt(2)));

        System.out.println(answer);

    }
}
