package streams;

import java.util.List;
import java.util.stream.Collectors;

public class StreamTeeingExample {

    public static void main(String[] args) {

        // Coleccionadores adicionales
        List<Integer> numbers = List.of(1, 2, 3, 4, 5);

        double average = numbers
                .stream()
                .collect(Collectors.teeing(
                        Collectors.summingDouble( i -> i),
                        Collectors.counting(),
                        (sum, count) -> sum / count
                ));

        System.out.println("El promedio del array es: "+ average);
    }
}
