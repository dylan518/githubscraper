package src.homework2;

public class FullstackDeveloper implements Fullstack{
    private final String name;
    private final double salary;

    public FullstackDeveloper(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    @Override
    public void developServer() {
        System.out.println("Writing code for server");
    }

    @Override
    public void developGUI() {
        System.out.println("Writing code for GUI");
    }
}
