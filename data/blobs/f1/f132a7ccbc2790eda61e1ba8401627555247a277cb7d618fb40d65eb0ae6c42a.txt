public class CalisanKopekDemo
{

    public static void main(String[] args)
    {

        CalisanKopek calisankopek1 = new CalisanKopek();
        CalisanKopek calisankopek2 = new CalisanKopek();

        calisankopek1.setAd("Bekçi Köpeee");
        //System.out.println(calisankopek1.getAd());
        calisankopek1.setEgitimSaati(30);

        calisankopek2.setAd("Polis Köpeği");
        calisankopek2.setEgitimSaati(400);


        System.out.println("birinci çalışan köpek");
        calisankopek1.ses();
        calisankopek1.calis();
        
        
        System.out.println("ikinci çalışan köpek");
        calisankopek2.ses();
        calisankopek2.calis();


    }
}