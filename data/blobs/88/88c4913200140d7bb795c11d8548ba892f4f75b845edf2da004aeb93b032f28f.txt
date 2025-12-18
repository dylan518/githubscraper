import java.io.*;
import java.net.Socket;

/**
 * @auther chuyin
 * @date 2023/7/30
 * @project java SE
 */
public class ClientDemo4 {
    public static void main(String[] args) throws IOException {
        Socket s=new Socket("192.168.1.7",10000);
        //封装文本文件的数据
        BufferedReader br=new BufferedReader(new FileReader("D:\\myStream\\InetAddress.java"));
        //封装输出流写数据
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
        String line;
        while((line =br.readLine())!=null)
        {
            bw.write(line);
            bw.newLine();
            bw.flush();
        }
        bw.close();
        s.close();
    }
}
