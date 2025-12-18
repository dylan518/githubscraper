package ai.groundup.anomalert.service;

import ai.groundup.anomalert.model.Alert;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class AlertService {
    private AlertRepo alertRepo;

    @Autowired
    public AlertService(AlertRepo alertRepo) {
        this.alertRepo = alertRepo;
    }

    public List<Alert> allAlert() {
        return this.alertRepo.findAll();
    }

    public List<Alert> alertByMachine(String machine) {
        try {
            return this.alertRepo.findByMachine(machine);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Long totalAlert() {
        return this.alertRepo.count();
    }

    public int uncheckedAlert() {
        int unchecked = this.alertRepo.findByIsChecked(false).size();
        return unchecked;
    }

    public Optional<Alert> alertById(Long id) {
        return this.alertRepo.findById(id);
    }
}
