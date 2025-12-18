/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package atp;

/**
 *
 * @author steph
 */
public class FuncionarioTemporario extends Funcionario{
       
    public int meses;
    private int qtdDependentesdIdadeLimite;

    public FuncionarioTemporario(int funCod, double funSalarioBase, int meses) {
        this.funCod = funCod;
        this.funSalarioBase = funSalarioBase;
        this.meses = meses;
    }
    
    public double valorMensalRecebido() {
        return this.funSalarioBase + (15 * this.meses);
    }
    
    public int valorAdicionalPelosDependentes(){
        return this.qtdDependentesdIdadeLimite(18);
    }
    
    public void dadosFuncionario() {
        
        System.out.println("___Funcionário Temporário___");
    
        super.dadosFuncionario();
        
        System.out.println("Salário Mensal: " + ( this.funSalarioBase + (15 * this.meses) + (100 * this.qtdDependentesdIdadeLimite)));
    }

    
}