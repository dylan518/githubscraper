package com.example.Hackentine.Controller;

import com.example.Hackentine.Entity.EventEntity;
import com.example.Hackentine.Service.EventService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.Base64;
import java.util.List;
import java.util.Optional;

@RestController
@CrossOrigin(origins = "http://localhost:3000")
@RequestMapping("/events")
public class EventController {

    @Autowired
    private EventService eventService;

    @GetMapping
    public List<EventEntity> getAllEvents() {
        return eventService.getAllEvents();
    }

    @GetMapping("/{id}")
    public ResponseEntity<EventEntity> getEventById(@PathVariable Long id) {
        Optional<EventEntity> event = eventService.getEventById(id);
        return event.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<EventEntity> createEvent(
            @RequestParam("poster") MultipartFile poster, 
            @RequestParam("eventName") String eventName,
            @RequestParam("description") String description,
            @RequestParam("duration") String duration,
            @RequestParam("eventDate") String eventDate,
            @RequestParam("eventType") String eventType,
            @RequestParam("internship") boolean internship,
            @RequestParam("rank1Prize") String rank1Prize,
            @RequestParam("rank2Prize") String rank2Prize,
            @RequestParam("rank3Prize") String rank3Prize,
            @RequestParam("teamSize") int teamSize) throws IOException {

        EventEntity event = new EventEntity();
        event.setEventName(eventName);
        event.setDescription(description);
        event.setDuration(duration);
        event.setEventDate(eventDate);
        event.setEventType(eventType);
        event.setInternship(internship);
        event.setRank1Prize(rank1Prize);
        event.setRank2Prize(rank2Prize);
        event.setRank3Prize(rank3Prize);
        event.setTeamSize(teamSize);

        // Convert poster image to Base64 string
        String base64Poster = Base64.getEncoder().encodeToString(poster.getBytes());
        event.setPoster(base64Poster);

        EventEntity savedEvent = eventService.saveEvent(event);
        return new ResponseEntity<>(savedEvent, HttpStatus.CREATED);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteEvent(@PathVariable Long id) {
        eventService.deleteEvent(id);
        return ResponseEntity.noContent().build();
    }
}
