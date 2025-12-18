import java.util.Arrays;
public class HeapSort {
    public static void main(String[] args) {
        int arr[] = { 1, 12, 9, 5, 6, 10 };
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }

    public static void sort(int arr[]) {
        int i, n = arr.length;

        for (i = n / 2 - 1; i >= 0; i--) {
            pivote(arr, n, i);
        }

        for (i = n - 1; i >= 0; i--) {
            intercambiar(arr, 0, i);
            pivote(arr, i, 0);
        }
    }

    public static void pivote(int arr[], int n, int i) {
        //Buscamos el mas grande en el arbol binario
        int masGrande = i;
        int izquierda = 2 * i + 1;
        int derecha = 2 * i + 2;

        if (izquierda < n && arr[izquierda] > arr[masGrande])
            masGrande = izquierda;

        if (derecha < n && arr[derecha] > arr[masGrande])
            masGrande = derecha;

        // Cambiamos y seguimos buscando si no se encuentra el mas grande
        if (masGrande != i) {
            intercambiar(arr, i, masGrande);
            pivote(arr, n, masGrande);
        }
    }

    public static void intercambiar(int[] arr, int p1, int p2) {
        int aux;
        aux = arr[p1];
        arr[p1] = arr[p2];
        arr[p2] = aux;
    }
}
