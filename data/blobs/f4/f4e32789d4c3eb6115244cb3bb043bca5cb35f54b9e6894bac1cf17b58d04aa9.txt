package laboratorio4;

public class Administrador extends Funcionario {

    private double salario;

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public Administrador(String nome, String sobrenome, double salario) {
        super(nome, sobrenome);
        this.salario = salario;
    }

    public Administrador(double salario) {
        this.salario = salario;
    }

    @Override
    public String toString() {
        return "Administrador [salario=" + salario + "]" + super.toString();
    }

    @Override
    public double calcularGanhos() {
        return salario;
    }

    
    
}
