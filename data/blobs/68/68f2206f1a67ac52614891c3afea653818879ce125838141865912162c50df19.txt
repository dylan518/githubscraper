import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;

// 클라이언트(소켓)
// 서버 IP : 192.168.0.172
// 서버 PORT : 9999
public class Ex02_TCP_Client {
	public static void main(String[] args) throws IOException{
		Socket socket = new Socket("192.168.0.200", 9999);
		System.out.println("서버와 연결되었츄!");	
		
		// 서버에서 보낸 메시지 받기
		InputStream in = socket.getInputStream();
		DataInputStream dis = new DataInputStream(in);
		String serverMsg = dis.readUTF();
		
		System.out.println("서버에서 보낸 메시지이츄 : " + serverMsg);
		
		dis.close();
		in.close();
		socket.close();
	}
}
