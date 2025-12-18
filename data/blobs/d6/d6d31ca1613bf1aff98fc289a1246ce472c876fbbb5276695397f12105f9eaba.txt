//Condicional simples
public class CaixaEletronico {

    public static void main(String[] args) {
        //Variáveis
        double saldo = 25.0;
        double valorSolicitado = 17.0;

        //Controle de fluxo condicional
        if(valorSolicitado < saldo){
            saldo = saldo - valorSolicitado;
            //Imprime o novo saldo
            System.out.println("Novo saldo: " + saldo);
        
        }/*//Parte condicional composta
        else
            System.out.println("Saldo insuficiente!");*/

    }
}
 