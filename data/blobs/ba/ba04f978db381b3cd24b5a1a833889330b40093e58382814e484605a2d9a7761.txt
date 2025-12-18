package com.birdnest.application;

import com.birdnest.application.data.*;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;

@Service
public class Monitor {

    private BirdnestClient client;
    private ConcurrentMap<String, Violator> violators;
    private final LocalDateTime moniteringStartTime;
    LocalDateTime captureTime;
    private Pilot noPilot;
    private final Integer birdPositionX;
    private final Integer birdPositionY;
    private final Integer expireViolatorAfterMS;
    private final Integer inNDZ;
    private Log log = LogFactory.getLog(Monitor.class);


    public Monitor(BirdnestClient client) {
        this.client = client;
        this.violators = new ConcurrentHashMap<String, Violator>();
        this.moniteringStartTime = LocalDateTime.now(ZoneId.of("UTC"));
        this.noPilot = new Pilot("Not Available", "Not Available", "Not Available",
                "Not Available", "Not Available", "Not Available");
        this.birdPositionX = 250000;
        this.birdPositionY = 250000;
        this.expireViolatorAfterMS = 600000;
        this.inNDZ = 100000;
    }

    public boolean isDroneInNDZ(double distance) {
        if (distance > inNDZ)
            return false;
        return true;
    }

    public double calculateDistance(Float positionX, Float positionY) {
        var distance = Math.sqrt(((positionX - birdPositionX) * (positionX - birdPositionX))
                + ((positionY - birdPositionY) * (positionY - birdPositionY)));
        return distance;
    }

    public void removeExpired(ConcurrentMap<String, Violator> violators) {
        for (Map.Entry<String, Violator> entry : violators.entrySet()) {
            entry.getValue().setInterval();
            if (entry.getValue().getInterval() >= expireViolatorAfterMS)
                violators.remove(entry.getKey());
        }
    }


    /**
     * Add new pilot
     */
    public void addNewViolator(Drone drone, Capture capture, double distance) throws Exception {
        Violator violator;
        var pilot = client.getPilot(drone.serialNumber());
        if (pilot == null) {
            pilot = this.noPilot;
            this.log.warn("Cannot get pilot information for " + drone.serialNumber());
        }
        violator = new Violator(pilot, drone, capture, distance);
        this.violators.put(drone.serialNumber(), violator);
    }

    /**
     * when violator has been added
     * 1.Update time
     * 2.Update distance when the new distance is closer than before
     */
    public void updateViolator(Drone drone, Capture capture, double distance) {
        Violator violator;
        violator = this.violators.get(drone.serialNumber());
        violator.updateTime(capture);
        if (isDroneInNDZ(distance))
            if (violator.getDistance() > distance)
                violator.updateDrone(drone, distance);
    }

    public void addViolator(Capture capture) throws Exception {
        for (Drone drone : capture.drones()) {
            double distance = calculateDistance(drone.positionX(), drone.positionY());
            if (this.violators.containsKey(drone.serialNumber()))
                updateViolator(drone, capture, distance);
            else if (isDroneInNDZ(distance))
                addNewViolator(drone, capture, distance);
        }
    }

    @Scheduled(fixedRate = 2000)
    public void updateViolators() throws Exception {
        try {
            var report = this.client.getReport();
            this.log.info("Received report: " + report);
            addViolator(report.capture());
            this.captureTime = report.capture().snapshotTimestamp();
        } catch (Exception ex) {
            this.log.error("getReport request faild", ex);
        }
        removeExpired(this.violators);
    }

    public void printViolators() {
        for (Map.Entry<String, Violator> entry : violators.entrySet()) {
            System.out.println(entry.getValue().toString());
        }
    }

    public ViolatorReport getViolatorReport() {
        var array = this.violators.values().toArray(new Violator[this.violators.size()]);
        var violatorReport = new ViolatorReport(array, this.captureTime, moniteringStartTime);
        return (violatorReport);
    }
}
