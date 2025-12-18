package com.example;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.Socket;

public class MioThread extends Thread {

    Socket s0;

    public MioThread(Socket s0) {
        this.s0 = s0;
    }

    @Override
    public void run() {
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(s0.getInputStream())); // stream dati in
            DataOutputStream out = new DataOutputStream(s0.getOutputStream()); // stream dati out

            String request = in.readLine();

            if(request.split(" ")[0].equals("GET"))
            {
                while(true)
                {
                    String line = in.readLine();
                    if(line.equals(""))
                    {
                        String response = "<html><body>yeah</body></html>";
                        out.writeBytes("HTTP/1.1 404 Not found \r\n");
                        out.writeBytes("Content-Length: " + response.length() + "\r\n");
                        out.writeBytes("Content-Type: text/html \r\n");
                        out.writeBytes("\r\n");
                        out.writeBytes(response);
                        while(true)
                        {
                            Thread.currentThread().sleep(10000);
                            break;
                        }
                        break;
                    }
                    else
                    {
                        System.out.println(line);
                    }
                }
            }
        }catch(Exception e)
        {
        e.printStackTrace();
        }

}

}
