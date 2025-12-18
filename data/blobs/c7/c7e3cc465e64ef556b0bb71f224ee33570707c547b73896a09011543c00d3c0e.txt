import java.util.Random;

public class Gameplay {

    public static void main(String[] args) throws Exception {

        Messi pMessi = new Messi("Messias");
        Fede pFede = new Fede("Roldan");

        Random aleatorio = new Random();
        Integer turno = aleatorio.nextInt(2);
        Integer contador = 0; 

        while (pMessi.getVida()> 0 && pFede.getVida() > 0){
            contador = contador + 1;
            System.out.println("   -------------       Turno" + contador + ":");
            if (turno == 1) {
                pFede.recibirDanio(pMessi.atacar());
                System.out.println(pMessi.getNombre()+" HA ATACADO A "+ pFede.getNombre());
            } else{
                pMessi.recibirDanio(pFede.atacar());
                System.out.println(pFede.getNombre()+" HA ATACADO A "+ pMessi.getNombre());
            }
            turno = aleatorio.nextInt(2);
            System.out.println("Nivel de vida de "+ pMessi.getNombre() + ": " + pMessi.getVida());
            System.out.println("Nivel de vida de "+ pFede.getNombre() + ": " + pFede.getVida());
        }
        if (pMessi.getVida() > pFede.getVida()){
            System.out.println("El ganador es: " + pMessi.getNombre());
        } else{
            System.out.println("La webona es: " + pFede.getNombre());
        }
    }
}
