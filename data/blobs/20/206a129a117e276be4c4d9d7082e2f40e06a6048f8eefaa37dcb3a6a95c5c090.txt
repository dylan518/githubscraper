package day18_multiDimensionalArray;

public class C05_MultiDimensionalArray {
    public static void main(String[] args) {


        int[][] arr={{3,5,7},{1,2,3,4},{1,2},{7}};

        // toplam element sayısı kaçtır

        int elementSayisi=0;
        for (int i = 0; i <arr.length ; i++) {
            elementSayisi+=arr[i].length;
        }
        System.out.println(elementSayisi); // 10

        // tüm elementlerin toplamını bulun
        // MDA Array'lerde her bir elemti elden geçirme istiyorsak
        // katsayısı kadar nested for-loop kullanırız

        int elemntToplami=0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                elemntToplami+=arr[i][j];
            }
        }
        System.out.println(elemntToplami); // 35
    }
}
