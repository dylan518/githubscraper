import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
 
public class Server {
	public static void main(String[] args) throws IOException {
		ServerSocket servidor = new ServerSocket(12345);
		System.out.println("Porta 12345 aberta!");
    
		Socket cliente = servidor.accept();
		System.out.println("Nova conexao com o cliente " + 
		cliente.getInetAddress().getHostAddress());
    
		servidor.close();
	}
 }