package components;

public class IncrementalSingleton {

    private static IncrementalSingleton instance = null;
    private static int count = 0;
    private int numero;

    private IncrementalSingleton() {
        this.numero = ++count;
    }

    public static IncrementalSingleton getInstance() {

        if (instance == null) {
            instance = new IncrementalSingleton();
        }
        return instance;
    }

    @Override
    public String toString() {
        return "Incremental " + numero;
    }
}
