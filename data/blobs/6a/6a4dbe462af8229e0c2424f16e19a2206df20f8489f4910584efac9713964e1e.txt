
package scramblies;

public class Scramblies {

    public static void main(String[] args) {
        String str1 = "helloworld"; // try other values
        String str2 = "door"; // try other values
        boolean result = scramble(str1, str2);
        System.out.println("Cadena 1 ingresada: " + str1);
        System.out.println("Cadena 2 ingresada: " + str2);
        System.out.print("Cadena 2 esta dentro de cadena 1 (aunque sea desordenada): ");
        String resultPrint = result ? "SI" : "NO";
        System.out.println(resultPrint);
    }
    
    public static boolean scramble(String str1, String str2) {
        for (int i = 0; i < str1.length(); i++) {
            String letra1 = str1.substring(i, i + 1);
            int posLetra2 = str2.indexOf(letra1);
            str2 = (posLetra2 == -1) ? str2 : str2.substring(0, posLetra2) + str2.substring(posLetra2 + 1);
            if (str2.equals("")) {
                return true;
            }
        }
        return false;
    }
    
}
