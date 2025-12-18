// Victor Dos Santos Araujo, 2475553

public class FuncionarioTemporario extends Funcionario implements Pagamento {
    
    private int valorHora; // duração em meses
    private int horasTrabalhadas;
    
    // Met Const 
    public FuncionarioTemporario() {
        valorHora = 0;
        horasTrabalhadas = 0;
    }
    // SobreCarga
    public FuncionarioTemporario ( int valorHora, int horasTrabalhadas) {
            super();
            this.valorHora = valorHora;
            this.horasTrabalhadas = horasTrabalhadas;
    }
    
    public int getValorHora() {
        return valorHora;
    }

    public void setValorHora(int valorHora) {
        this.valorHora = valorHora;
    }
    public int gethorasTrabalhadas() {
        return horasTrabalhadas;
    }

    public void sethorasTrabalhadas(int horasTrabalhadas) {
        this.horasTrabalhadas = horasTrabalhadas;
    }

    @Override
    public void calcularPagamento() {
        double salarioTemporario = valorHora * horasTrabalhadas;
        System.out.println("Salário do Funcionário Temporário: " + salarioTemporario);
    }
    @Override
    public String getTipo() {
        return "Temporario";
    }
    
}
