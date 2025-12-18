import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Değişkenlerin tanımlanması
        double kdv;
        double amountWithKDV;
        int amountWithoutKdv;
        double amountKDV;

        // Kullanıcıdan girdi almak için Scanner nesnesinin oluşturulması
        Scanner scanner = new Scanner(System.in);

        // Kullanıcıdan ücretin girilmesi istenir
        System.out.println("KDV tutarını hesaplamak istediğiniz ücreti giriniz.");
        int x = scanner.nextInt();

        // KDV'siz ücret değişkeninin atanması
        amountWithoutKdv = x;

        // Ücrete göre KDV oranının belirlenmesi
        kdv =((x >= 0) && (x <= 1000)) ? 118.0 : 108.0;

        // KDV'li fiyatın hesaplanması
        amountWithKDV = x * (kdv / 100);

        // KDV tutarının hesaplanması
        amountKDV = amountWithKDV - amountWithoutKdv;

        // KDV'siz fiyat, KDV'li fiyat ve KDV tutarının ekrana yazdırılması
        System.out.println("KDV'siz fiyat = " + amountWithoutKdv +
                "\nKDV'li fiyat = " + amountWithKDV + "\nKDV tutarı = " + amountKDV);
    }
}
