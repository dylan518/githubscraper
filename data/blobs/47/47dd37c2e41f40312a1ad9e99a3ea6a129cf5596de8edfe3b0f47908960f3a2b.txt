public enum Prioridadee {

    MIN(3),NORMAL(6),MAX(9),SUPER(12),SUPERMAX(15);

    //mas é possível definir os valores das prioridades, usando um construtor
    private int valor;
    Prioridadee(int valuePriority){
        this.valor = valuePriority;
    }

    public int getValor() {
        return valor;
    }
}
