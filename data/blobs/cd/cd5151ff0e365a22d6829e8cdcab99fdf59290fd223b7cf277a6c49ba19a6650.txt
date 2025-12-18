package BackendEngineering.src.SocketProgramming;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class Server
{
    public static void main(String[] args) throws IOException {
        System.out.println("server started");
        ServerSocket ss = new ServerSocket(9999);
        System.out.println("server waiting for client");
        Socket s=ss.accept();
        System.out.println("client connected");
        BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
        String str = br.readLine();
        System.out.println("client data: "+str );
    }
}
