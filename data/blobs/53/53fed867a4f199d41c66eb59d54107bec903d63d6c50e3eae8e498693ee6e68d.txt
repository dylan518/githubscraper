package edu.eci.arep.Apps;





import edu.eci.arep.Cache;
import edu.eci.arep.HttpConection;
import edu.eci.arep.Services.RESTService;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

public class HttpServer {




    /**
     * Método main, inicia un socket recibe la petición get y agrega el nombre t de la película a la URL de la API
     * @param args
     * @throws IOException
     */

    private static HttpServer _instance = new HttpServer(); // la carga el class loader
    private static Map<String, RESTService> services = new HashMap();
    private HttpServer() {};
    static HttpServer getInstance(){return _instance;}

    //
    public  void run(String[] args) throws IOException {
        boolean running = true;
        ServerSocket serverSocket = null;
        String cacheData = "";
        String path = " ";



        try {
            serverSocket = new ServerSocket(35000);
        } catch (IOException e) {
            System.err.println("Could not listen on port: 35000.");
            System.exit(1);
        }

        while (running){
            Socket clientSocket = null;
            try {
                System.out.println("Listo para recibir ...");
                clientSocket = serverSocket.accept();
            } catch (IOException e) {
                System.err.println("Accept failed.");
                System.exit(1);
            }

            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            String inputLine, outputLine;

            boolean firstLine = true;
            while ((inputLine = in.readLine()) != null) {
                if (firstLine){
                    firstLine = false;
                    path = inputLine.split(" ")[1];
                }
                System.out.println("Received: " + inputLine);
                if (!in.ready()) {break;}
            }
            URL urlprincipal = new URL("http://www.localhost:35000" + path);
            String pathForm = urlprincipal.getQuery();
                if (pathForm != null) {
                    if (Cache.containCache(pathForm)){
                        cacheData = Cache.getCache(pathForm);
                    } else {
                        cacheData = HttpConection.HttpConectionExample(pathForm);
                        Cache.saveCache(pathForm, cacheData);
                    }
                }

            System.out.println(cacheData);
            //outputLine = "HTTP/1.1 200 OK\r\n"   + "\r\n" + htmlWithForms(cacheData); // jsonSimple

            if (urlprincipal.getPath().contains("/apps/")) { // localhost:35000/apps/hello
                outputLine = executeService(urlprincipal.getPath().substring(5)); // /apps/hello toma solo hello
            } else {
                outputLine = "HTTP/1.1 200 OK\r\n"   + "\r\n" + htmlWithForms(cacheData);
            }


            out.println(outputLine);

            out.close();
            in.close();
            clientSocket.close();


        }
        serverSocket.close();

    }

    //
    public String executeService(String serviceName) {
        RESTService rs= services.get(serviceName);
        String header = rs.getHeader();
        String body = rs.getResponse(); // lectura de disco al body
        return header + body;
    }

    //
    public void addService(String key, RESTService service){
        services.put(key, service);
    }




    public static String htmlWithForms(String cacheData){

        return "<!DOCTYPE html>\n" +
                "<html>\n" +
                "    <head>\n" +
                "        <title>Form Example</title>\n" +
                "        <meta charset=\"UTF-8\">\n" +
                "        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" +
                "    </head>\n" +
                "    <body style=\"background-color:lightsteelblue;\">\n" +
                "        <h1>Consultar Peliculas </h1>\n" +
                "        <form action=\"localhost:35000\" onsubmit=\"return false\" >\n" +
                "            <label for=\"t\">Name:</label><br>\n" +
                "            <input type=\"text\" id=\"t\" name=\"t\" value=\"pelicula\"><br><br>\n" +
                "            <input type=\"button\" value=\"Submit\" onclick=\"loadGetMsg()\">\n" +
                "        </form> \n" +
                "        <div  id=\"getrespmsg\"> " + cacheData + "</div>\n" +
                "\n" +
                "        <script>\n" +
                "            function loadGetMsg() {\n" +
                "                let nameVar = document.getElementById(\"t\").value;\n" +
                "                const xhttp = new XMLHttpRequest();\n" +
                "                xhttp.onload = function() {\n" +
                "                    document.getElementById(\"getrespmsg\").innerHTML =\n" +
                "                    this.responseText;\n" + "console.log(this.responseText);" +
                "                }\n" +
                "                xhttp.open(\"GET\", \"/?t=\"+nameVar);\n" +
                "                xhttp.send();\n" +
                "            }\n" +
                "        </script>\n" +
                "\n" +
                "    </body>\n" +
                "</html>";

    }

}
