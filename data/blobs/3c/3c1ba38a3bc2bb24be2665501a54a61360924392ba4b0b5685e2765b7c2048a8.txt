package src.ListaHerancaPolimorfismo.Questao11;

public class Supervisor extends Funcionario {
    private static final double comissaoSupervisor = 600.00;

    public Supervisor(String nome, int codigoFuncional, double salarioBase) {
        super(nome, codigoFuncional, salarioBase, comissaoSupervisor);
    }

    @Override
    public String toString() {
        return super.toString() + " Supervisor";
    }
}
