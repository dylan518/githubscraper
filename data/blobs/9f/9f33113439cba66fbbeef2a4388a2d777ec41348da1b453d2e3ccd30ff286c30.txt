package ro.uvt.info.sptestciorgoveandiana;
// Strategy pattern
// Visitor pattern
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.net.URL;
import java.util.List;

@Service
public class MessageObjectMapper {
    private final ObjectMapper objectMapper;
    private final DecodingStrategy atreidesStrategy = new Atreides();
    private final DecodingStrategy harkonnenStrategy = new Harkonnen();

    public MessageObjectMapper(ObjectMapper objectMapper) {
        this.objectMapper = objectMapper;
    }

    public List<Message> readMessagesFromFile() throws IOException {
        List<Message> messages = objectMapper.readValue(new URL("file:src/messages.json"), new TypeReference<List<Message>>(){});
        for (Message message : messages) {
            if ("Atreides".equals(message.getHouse())) {
                message.setDecodingStrategy(atreidesStrategy);
            } else if ("Harkonnen".equals(message.getHouse())) {
                message.setDecodingStrategy(harkonnenStrategy);
            }
        }
        for (Message message : messages) {
            message.accept(new DecodeVisitor());
        }

        return messages;
    }
}

