package com.smh.udp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

/**
 * ClassName: UDPSenderB
 * Package: com.smh.udp
 * Description:
 *
 * @Author mh sun
 * @Create 2024/4/16 11:29
 * @Version 1.0
 */
public class UDPSenderB {
    public static void main(String[] args) throws Exception{
        DatagramSocket socket = new DatagramSocket(9998);
        byte data[] = "hello 明天吃火锅".getBytes();
        DatagramPacket packet = new DatagramPacket(data, data.length, InetAddress.getByName("10.60.29.215"), 9999);
        socket.send(packet);
//      接受A回复的消息
        byte buf[] = new byte[1024];
        packet = new DatagramPacket(buf,buf.length);
        socket.receive(packet);
//        packet可以拆包
        int length = packet.getLength();
        data = packet.getData();
        String s = new String(data,0,length);
        System.out.println(s);
        socket.close();

    }
}
