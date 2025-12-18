package com.itsjaypatel.cabbookingapp.dtos;

import com.itsjaypatel.cabbookingapp.entities.PaymentMethod;
import com.itsjaypatel.cabbookingapp.entities.enums.RideStatus;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.locationtech.jts.geom.Point;

import java.time.LocalDateTime;


@Data
@NoArgsConstructor
@AllArgsConstructor
public class RideDto {


    private Long id;

    private RideStatus rideStatus;

    private Point pickupLocation;

    private Point dropOffLocation;

    private RiderDto rider;

    private DriverDto driver;

    private LocalDateTime createdTime;

    private LocalDateTime endTime;

    private Double fare;

    private String otp;


    private PaymentMethod paymentMethod;


    private LocalDateTime startedAt;

    private LocalDateTime endedAt;
}
