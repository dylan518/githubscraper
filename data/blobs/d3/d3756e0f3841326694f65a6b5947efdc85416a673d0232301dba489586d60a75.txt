package com.elevator.system.service;

import com.elevator.system.domain.Incident;
import com.elevator.system.repository.IncidentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class IncidentService {
    @Autowired
    private IncidentRepository incidentRepository;

    public List<Incident> getIncidents(){
        List<Incident> data = new ArrayList<>();
        incidentRepository.findAll().forEach(data:: add);
        return data;
    }
    public Incident getIncident(String id){
        List<Incident> data = new ArrayList<>();
        incidentRepository.findAll().forEach(data:: add);
        return data.stream().filter(incident -> incident.getIncidentId().equals(id)).findFirst().get();
    }

}
