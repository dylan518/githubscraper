package org.exampl;

import java.io.*;
import java.net.Socket;

import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try (Socket client = new Socket("localhost", 8081);
             BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
             BufferedWriter out = new BufferedWriter(new OutputStreamWriter(client.getOutputStream()))) {

            System.out.println(in.readLine());

            String message;
            while (!client.isClosed()) {
                message = scanner.next();

                out.write(message + "\n");
                out.flush();

                System.out.println(in.readLine());

            }
            scanner.close();


        } catch (IOException e) {
            e.printStackTrace();
        }


    }
}
