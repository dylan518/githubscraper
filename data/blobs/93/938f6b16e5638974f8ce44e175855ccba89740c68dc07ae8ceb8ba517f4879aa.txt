/******************************************************************************
 *  Nafn    : Gunnar Björn Þrastarson
 *  T-póstur: gbt6@hi.is
 *
 *  Lýsing  : Athugar hvort að miðjan sé minst eða ekki.
 *
 *
 *****************************************************************************/

public class MinnstaMidja {
    public static void main(String[] args) {

        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
         boolean midja = (b < a) && (b < c);

         System.out.print("miðjustakið af " + a + ","+ b +","+ c + " er minnst:" + midja);




    }

    /******************************************************************************
     *  Nafn    : Gunnar Björn Þrastarson
     *  T-póstur: gbt6@hi.is
     *
     *  Lýsing  : Reyknar út vaxtagreiðslu út frá höfuðstól, nafnavöxtum og árum.
     *
     *
     *****************************************************************************/

    public static class Vaxtavextir {
        public static void main(String[] args) {

            double p = Double.parseDouble(args[0]); // Höfuðstóll
            double i = Double.parseDouble(args[1]); //nafnavextir
            int n = Integer.parseInt(args[2]); // ár

            double r = i / 100; // breyti i í tugabrot
            double g = 1 + r;  // reikna inn í sviga
            double h = Math.pow(g , n); //set svigan í veldi
            double t = h - 1; // mínusa svigan í veldi við 1


            double vaxtagreidsla = (p * t); // margfalda h0fuðstól við restina

            System.out.print("Vaxtagreiðslan er:" + vaxtagreidsla);
            }



        }
}
