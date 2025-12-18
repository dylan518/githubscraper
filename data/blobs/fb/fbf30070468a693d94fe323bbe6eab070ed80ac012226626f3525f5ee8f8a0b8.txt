package ActividadObligatoriaTrenTuristico;

public class ControlTren extends Thread {
    public TrenTuristico tren;

    public ControlTren(TrenTuristico tren) {
        this.tren = tren;
    }

    public void run() {
        boolean flag = false;
        //al menos debe salir una vez el tren
        while (!flag) {
            if (tren.capacidad == 0) {
                tren.comenzarRecorrido();
                System.out.println("\n _____ El tren esta lleno puede iniciar recorrido \n");
                try {
                    tren.viajar();
                    sleep(5000);
                } catch (Exception e) {
                    e.getStackTrace();
                }
                System.out.println("\n _____ El recorrido ha finalizado, pueden bajarse \n");
                tren.bajarPasajeros();
                flag = true;
            }
        }
    }
}
