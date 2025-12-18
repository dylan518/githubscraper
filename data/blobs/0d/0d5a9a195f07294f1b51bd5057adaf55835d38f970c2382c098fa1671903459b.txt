import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String userName, pass, reset, newPass;

        System.out.print("Kullanıcı Adınızı Giriniz: ");
        userName = input.nextLine();

        System.out.print("Şifrenizi Giriniz: ");
        pass = input.nextLine();

        if (userName.equals("İsa") && pass.equals("deneme123")) {
            System.out.print("Başarılı bir şekilde giriş yaptınız.");

        } else {
            System.out.print("Hatalı giriş yaptınız. Şifrenizi sıfırlamak istermesiniz?");
            System.out.print("Şifreyi sıfırlamak için e \ntekrar giriş yapmak için h tuşuna basınız: ");
            reset = input.nextLine();
            if (reset.equals("e")) {
                System.out.print("Yeni şifrenizi giriniz: ");
                newPass = input.nextLine();
                if(newPass.equals("deneme123")){
                    System.out.println("Şifreniz eski şifrenizle aynı olmamalıdır.");
                    System.out.print("Eski şifrenizdem farklı bir şifre giriniz: ");
                    newPass = input.nextLine();
                    if (!newPass.equals("deneme123")){
                        System.out.println("Yeni şifre oluşturuldu.");
                    }
                }else System.out.println("Şifreniz başarıyla değiştirilmiştir.");

            } else if (reset.equals("h")) {
                System.out.print("Yeniden giriş yapınız.");

            } else System.out.println("Hatalı seçim yaptınız.");

        }
        ;
    }

}
