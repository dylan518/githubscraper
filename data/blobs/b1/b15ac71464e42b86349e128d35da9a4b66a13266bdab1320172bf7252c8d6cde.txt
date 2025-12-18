package io.javabrains.springbootstarter.topic;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

/*
 * Instead of creating a new List that is converted to JSON everytime "/endpoint" is requested, 
 * we use a spring business service that will be persistant and we can just add or remove from it.
 * 
 * When application starts up, all service classes have an instance created
 * 
 * @Service annotation lets Spring know our class is a business service
 * 
 */

@Service
public class TopicService {
	private List<Topic> topics = new ArrayList<>(Arrays.asList(
			new Topic("spring", "Spring Framework", "Spring Framework Description"),
			new Topic("java", "Core Java", "Core Java Description"),
			new Topic("javascript","Javascript", "Javascript Description")
			));
	
	// this is our method that will get all topics from the business service
	// the only reason for this service in this case is persistance
	public List<Topic> getAllTopics(){
		return topics;
	}
	
	public Topic getTopic(String id) {
		return topics.stream().filter(t -> t.getId().equals(id)).findFirst().get();
	}
	
	public void addTopic(Topic topic) {
		topics.add(topic);		
	}
	
	public void updateTopic(Topic topic, String id) {
		for (int i = 0; i < topics.size(); i++) {
			Topic t = topics.get(i);
			if(t.getId().equals(id)) {				
				topics.set(i, topic);
				return;
			}
		}
	}
	
	public void deleteTopic(String id) {
		topics.removeIf(t -> t.getId().equals(id));
	}
}
