import java.time.LocalDate;

public abstract class Propiedad {

    //Attributes
    private LocalDate fechaAlquilada;
    private Double precioUsd;
    private String direccion;
    private Boolean estaHipotecada;
    private Duenio duenio;


    //Constructor
    public Propiedad(LocalDate fechaAlquilada, Double precioUsd, String direccion, Boolean estaHipotecada, Duenio duenio) {
        this.fechaAlquilada = fechaAlquilada;
        this.precioUsd = precioUsd;
        this.direccion = direccion;
        this.estaHipotecada = estaHipotecada;
        this.duenio = duenio;
    }

    //GETTERS


    public Boolean getEstaHipotecada() {
        return estaHipotecada;
    }


    //Method
    public abstract Boolean sePuedeVender();
}
