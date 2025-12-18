import java.io.IOException;

public class ClaseRuntime {

    public static void main(String[] args) {
        // Ejemplo usando java.lang.Runtime

        // Obtener la instancia del objeto Runtime
        Runtime runtime = Runtime.getRuntime();

        // Obtener la cantidad total de memoria del JVM
        long totalMemory = runtime.totalMemory();
        System.out.println("Memoria total (bytes): " + totalMemory);

        // Obtener la cantidad de memoria libre del JVM
        long freeMemory = runtime.freeMemory();
        System.out.println("Memoria libre (bytes): " + freeMemory);

        // Obtener el número de procesadores disponibles
        int availableProcessors = runtime.availableProcessors();
        System.out.println("Número de procesadores disponibles: " + availableProcessors);

        // Ejecutar un comando del sistema para abrir el Bloc de notas
        openNotepad();

        // Solicitar la recolección de basura
        runtime.gc();
        System.out.println("Se ha solicitado la recolección de basura.");
    }

    private static void openNotepad() {
        try {
            String os = System.getProperty("os.name").toLowerCase();
            Process process;

            if (os.contains("win")) {
                // Windows
                process = Runtime.getRuntime().exec("notepad");
            } else if (os.contains("nix") || os.contains("nux") || os.contains("mac")) {
                // Linux / macOS
                process = Runtime.getRuntime().exec(new String[]{"xdg-open", "/path/to/your/textfile.txt"});
                // Para macOS usa el siguiente comando en lugar de xdg-open
                // process = Runtime.getRuntime().exec(new String[]{"open", "/path/to/your/textfile.txt"});
            } else {
                System.out.println("Sistema operativo no soportado para abrir el Bloc de notas.");
                return;
            }

            process.waitFor();
            System.out.println("Bloc de notas abierto exitosamente.");
        } catch (IOException | InterruptedException e) {
            System.out.println("Error al abrir el Bloc de notas: " + e.getMessage());
        }
    }
}
