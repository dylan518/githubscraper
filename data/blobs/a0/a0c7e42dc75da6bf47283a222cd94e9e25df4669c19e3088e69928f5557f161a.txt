public class VehiculoCarga extends Vehiculo {
    private int capacidadCarga;

    
    public VehiculoCarga(String marca, String modelo, int año, int kilometraje, int capacidadCarga) {
        super(marca, modelo, año, kilometraje);
        this.capacidadCarga = capacidadCarga;

    }

    
    public int getCapacidadCarga() {
        return capacidadCarga;
    }

    public void SetCapacidadCarga(int capacidadCarga) {
        this.capacidadCarga = capacidadCarga;

    }

    
    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Capacidad de Carga: " + capacidadCarga + " kg");
    }
    

    


}
