package com.ecommerce.customer.soa.CardRequest;

import org.springframework.stereotype.Service;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

@Service
public class CreditCardApplicationClient {

    public ApplicationOutput submitApplication(ApplicationInput input) {
        ApplicationOutput output = new ApplicationOutput();

        try {
            // Example URL of the OSB service
            URL url = new URL("http://your-osb-service-url/submitCardApplication");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            // Set up the connection properties
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/xml; utf-8");
            connection.setDoOutput(true);

            // Create the XML payload
            String xmlInputString = String.format(
                    "<Application>" +
                            "<customerID>%s</customerID>" +
                            "<cardType>%s</cardType>" +
                            "<limit>%d</limit>" +
                            "<documentType>%s</documentType>" +
                            "<filePath>%s</filePath>" +
                            "</Application>",
                    input.getCustomerID(), input.getCardType(), input.getLimit(), input.getDocumentType(), input.getFilePath()
            );

            // Write the XML payload to the output stream
            try (OutputStream os = connection.getOutputStream()) {
                byte[] inputBytes = xmlInputString.getBytes(StandardCharsets.UTF_8);
                os.write(inputBytes, 0, inputBytes.length);
            }

            // Get the response code from the server
            int responseCode = connection.getResponseCode();
            if (responseCode == 200) {
                output.setStatus("Success");
                output.setMessage("Application submitted successfully.");
            } else {
                output.setStatus("Failure");
                output.setMessage("Failed to submit application. Response code: " + responseCode);
            }

        } catch (Exception e) {
            output.setStatus("Failure");
            output.setMessage("Exception occurred: " + e.getMessage());
        }

        return output;
    }
}
