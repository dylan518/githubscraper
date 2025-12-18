package app.ivalley.kakatutorial.kafka;


import app.ivalley.kakatutorial.model.UserDetails;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaJsonConsumer {

    private static final Logger LOGGER = LoggerFactory.getLogger(KafkaProducer.class);
    @KafkaListener(topics = "topic-2",groupId = "myGroup")
    public void consume(UserDetails message ){
        LOGGER.info(String.format(" message received   : %s", message.toString()));
    }
}
