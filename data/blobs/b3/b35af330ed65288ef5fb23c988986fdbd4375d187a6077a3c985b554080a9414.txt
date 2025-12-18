package loopanddatatypes;

public class DataTypesDemo {
    private int age = 19;
    private int fatherAge = 65;
    private String name = "Ratan";
    private int[] numPool = {1, 2, 3, 4, 5, 6};

    int getAgeDiff() {
        return fatherAge - age;  // Calculate directly
    }

    int getSumPool() {
        int sum = 0;  // Reset sum each time the method is called
        for (int num : numPool) {
            sum += num;
        }
        return sum;
    }

    String getFullName() {
        return name.concat(" Tata");  // Add a space before concatenation for readability
    }

    void printNumPool() {
        for (int num : numPool) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}