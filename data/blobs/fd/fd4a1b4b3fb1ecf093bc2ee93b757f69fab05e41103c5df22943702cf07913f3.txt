public class Carro extends Veiculo {
    private boolean temArCondicionado;
    private boolean temRadio;

    public Carro(boolean motor, boolean volante, int qtdPassageiros, int qtdPortas,
                 int qtdRodas, boolean eDeCarga, double capacidadeCarga, Combustivel combustivel,
                 boolean temArCondicionado, boolean temRadio) {
        super(motor, volante, qtdPassageiros, qtdPortas, qtdRodas, eDeCarga, capacidadeCarga, combustivel);
        this.temArCondicionado = temArCondicionado;
        this.temRadio = temRadio;
    }

    public Carro() {}

    public String info() {
        String information = "\nCarro "
                + this.constructInfo()
                + ",\n\tar condicionado: " + verificador(isTemArCondicionado())
                + ",\n\ttem radio: " + verificador(isTemRadio())
                + "\n}";
        return information;
    }

    public String som() {
        return "\nSom do carro: Ggrrooo ggrrooo ggrrooo";
    }

    public boolean isTemArCondicionado() {
        return temArCondicionado;
    }

    public void setTemArCondicionado(boolean temArCondicionado) {
        this.temArCondicionado = temArCondicionado;
    }

    public boolean isTemRadio() {
        return temRadio;
    }

    public void setTemRadio(boolean temRadio) {
        this.temRadio = temRadio;
    }
}
