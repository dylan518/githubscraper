public class transfprime {
    public static boolean EsPrim(Integer n) {
        Integer divisor = 2;
        while (divisor<n) {
            if (n%divisor==0) {
                return false;
            }
            divisor++;
        }
        return true;
    }

    public static int minimumNumber(int[] numbers) {
        Integer n_total = 0;
        Integer n_añadir = 0;
        for (int n : numbers) {
            n_total+=n; // voy sumando cada numero de lista a mi total
        }

        if (EsPrim(n_total)) {
            return 0; // ya es primo
        } else {
            while (EsPrim(n_total)==false) {
                n_añadir+=1;
                n_total+=1;
            }
            return n_añadir; // devuelvo números añadidos
        }
    }

    public static void main(String[] args) {
        System.out.println(minimumNumber(new int[]{50,39,49,6,17,28}));
    }
}
