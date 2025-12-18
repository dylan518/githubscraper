/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package communication;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

/**
 *
 * @author x
 */
public class CommunicationHelper {
    //pomocna klasa za otvaranje in i out streama i salje i prima podatke preko soketa
    
    private Socket socket;
    private ObjectOutputStream out;
    private ObjectInputStream in;
    
     public CommunicationHelper(Socket socket) throws IOException {
        this.socket = socket;
        out = new ObjectOutputStream(socket.getOutputStream());
        in = new ObjectInputStream(socket.getInputStream());
    }
    //slanje
    public void send(Object obj) throws IOException {
        out.writeObject(obj);
    }
    //prihvatanje
    public Object receive() throws IOException, ClassNotFoundException {
        return in.readObject();
    }
}
