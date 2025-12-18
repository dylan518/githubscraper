package springboot.one.topic;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
// import java.util.stream.Stream;
import org.springframework.stereotype.Service;

@Service
public class TopicService {

    private List<Topic> topics = new ArrayList<>(
        Arrays.asList(
            new Topic("1", "Math", "Elemental & theoretical wizardry"),
            new Topic("2", "HTML", "Conjuration"),
            new Topic("3", "JavaScript", "Telekinesis")
        )
    );

    public List<Topic> getAllTopics() {
        return topics;
    }

    public Topic getTopic(String id) {
        // Stream<Topic> stream = topics.stream();
        // Topic result = stream.filter(ele -> ele.getId() == id).findFirst().get();
        // return result;
        return topics
            .stream()
            .filter(item -> {
                // System.out.println(item.getId());
                // System.out.println(id);
                // System.out.println(item.getId() == id);
                // System.out.println(item.getId().equals(id));
                return item.getId().equals(id);
            })
            .findFirst()
            .get();
        // return topics.get(0);
    }

    public void addTopic(Topic topic) {
        topics.add(topic);
    }

    public void updateTopic(String id, Topic topic) {
        for (int i = 0; i < topics.size(); i++) {
            System.out.println(topics.get(i));
            if (topics.get(i).getId().equals(id)) {
                topics.set(i, topic);
                return;
            }
        }
    }

    public void deleteTopic(String id, Topic topic) {
        topics.removeIf(oldTopic -> oldTopic.getId().equals(id));
    }
}
