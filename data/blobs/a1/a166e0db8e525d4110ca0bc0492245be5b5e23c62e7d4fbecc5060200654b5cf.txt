public class Main {

	public static void main(String[] args) {
		Cliente gabriela = new Cliente();
		gabriela.setNome("Gabriela");
		
		Conta cc = new ContaCorrente(gabriela);
		Conta poupanca = new ContaPoupanca(gabriela);

		cc.depositar(100);
		cc.transferir(20, poupanca);
		
		cc.imprimirExtrato();
		poupanca.imprimirExtrato();
	}

}