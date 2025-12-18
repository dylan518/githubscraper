package org.paulo;

import java.net.URI;
import java.net.http.*;

import com.google.gson.*;

public class Cotacao {

    public String cotarMoeda(String moeda) {
        HttpClient cliente = HttpClient.newHttpClient();
        URI uri = URI.create("https://v6.exchangerate-api.com/v6/88cabc95b2ae188023004b3e/latest/" + moeda);

        HttpRequest request = HttpRequest.newBuilder(uri).GET().build();

        HttpResponse<String> response = null;

        try {
            response = cliente.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }

        if (response == null || response.body() == null) {
            System.out.println("Erro: resposta HTTP vazia");
            return null;
        }

        JsonParser jp = new JsonParser();
        JsonElement root = jp.parse(response.body());
        JsonObject jsonobj = root.getAsJsonObject();

        String req_result = jsonobj.get("result").getAsString();
        if (!"success".equals(req_result)) {
            System.out.println("Erro na requisição: " + req_result);
            return null;
        }

        return jsonobj.toString();
    }
}
