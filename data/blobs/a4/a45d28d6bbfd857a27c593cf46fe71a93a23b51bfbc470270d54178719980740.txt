public class Perro extends Canino {

    public Integer fuerzaMordida;

    public Perro(String habitat, float altura, float largo, float peso, String nombreCientifico,
                 String color, Float tamanoColmillos, Integer fuerzaMordida) {
        super(habitat, altura, largo, peso, nombreCientifico, color, tamanoColmillos);
        this.fuerzaMordida = fuerzaMordida;
    }

    public Integer getFuerzaMordida() {
        return fuerzaMordida;
    }

    public void setFuerzaMordida(Integer fuerzaMordida) {
        this.fuerzaMordida = fuerzaMordida;
    }

    @Override
    public String correr() {
        return "La velocidad de un " + getClass().getName() + " depende de su tamaño y peso." ;
    }

    @Override
    public String comer() {
        return "Es originario de " + this.habitat + ".\nSu fuerza de mordida es de " + this.fuerzaMordida +
                " PSI y puede alcanzar los " + this.peso + " kilos de peso.";
    }

    @Override
    public String comunicarse() {
        return "Se comunica con otros caninos a través del lenguaje corporal, mediante posturas ofensivas y defensivas" +
                ", vocalizaciones y expresiones faciales.";
    }

    @Override
    public String dormir() {
        return "Duerme en cualquier lugar donde se sienta seguro.";
    }
}
