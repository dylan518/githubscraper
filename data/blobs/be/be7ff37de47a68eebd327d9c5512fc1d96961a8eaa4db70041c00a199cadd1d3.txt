package ntforma.exercicio4;


//4 -  Uma pessoa possui { nome cpf, rg, idade}
//        Um funcionário, alem de possuir as mesmas informações de uma pessoa, possui também { cargo, salário}
//        Um Motorista, alem de possuir as mesmas informações de um funcionário, possui também { cnh, placaCarro}
//        Monte a estrutura de classes, instancie 2 Motoristas e imprima no console { nome, cargo e placaCarro } de cada motorista

public class Funcionario extends Pessoa {
    private String cargo;

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    private double salario;

    public Funcionario(String nome, String cpf, String rg, int idade, String cargo, double salario) {
        super(nome, cpf, rg, idade);
        this.cargo = cargo;
        this. salario = salario;
    }

}
