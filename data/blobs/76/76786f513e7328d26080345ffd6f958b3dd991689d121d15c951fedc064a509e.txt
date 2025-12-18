package servicio;

import entidades.Electrodomestico;
import entidades.Televisor;
import java.util.Scanner;

public class TelevisorService extends ElectrodomesticosService {
    
    public Televisor crearTelevisor(){
        Scanner leer = new Scanner(System.in).useDelimiter("\n");
        Electrodomestico electro = crearElectrodomestico();
        Televisor tele = new Televisor();
        tele.setPrecio(electro.getPrecio());
        tele.setColor(electro.getColor());
        tele.setConsumo(electro.getConsumo());
        tele.setPeso(electro.getConsumo());
        System.out.println("ingrese la cantidad de pulgadas del televisor");
        tele.setPulgadas(leer.nextInt());
        System.out.println("tiene sincronizador TDT? (si/no)");
        if (leer.next().equalsIgnoreCase("si")) {
            tele.setSincronizadorTDT(true);
        }
        precioFinal(tele);
        return tele;
    }
    
    public void precioFinal(Televisor tele){
        super.comprobarConsumoEnergetico(tele.getConsumo());
        super.comprobarColor(tele.getColor());
        super.precioFinal(tele);
        
        if (tele.getPulgadas() > 40) {
            tele.setPrecio(tele.getPrecio() + (tele.getPrecio()*30/100));
        }
        if (tele.isSincronizadorTDT()) {
            tele.setPrecio(tele.getPrecio() + 500);
        }
        System.out.println("precio final: " + tele.getPrecio());
    }
    
}
