package com.example.flightservice.service;

import com.example.flightservice.dto.FlightBookingAcknowledgment;
import com.example.flightservice.dto.FlightBookingRequest;
import com.example.flightservice.entity.PassengerInfo;
import com.example.flightservice.entity.PaymentInfo;
import com.example.flightservice.repository.PassengerRepository;
import com.example.flightservice.repository.PaymentRepository;
import com.example.flightservice.utils.PaymentUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.io.SyncFailedException;
import java.util.UUID;

@Service
public class FlightBookingService {

    @Autowired
    private PassengerRepository passengerRepository;
    @Autowired
    private PaymentRepository paymentRepository;

    @Transactional
    public FlightBookingAcknowledgment flightBookingAcknowledgment(FlightBookingRequest flightBookingRequest){

        PassengerInfo passengerInfo = flightBookingRequest.getPassengerInfo();
        passengerInfo = passengerRepository.save(passengerInfo);
        PaymentInfo paymentInfo = flightBookingRequest.getPaymentInfo();
//        paymentInfo = paymentRepository.save(paymentInfo);
        System.out.println(paymentInfo.getAccountNo());
        System.out.println(passengerInfo.getFare());
        PaymentUtils.validateCreditLimit(paymentInfo.getAccountNo(), passengerInfo.getFare());
        paymentInfo.setPassengerId(passengerInfo.getPId());
        paymentInfo.setAmount(passengerInfo.getFare());
        paymentRepository.save(paymentInfo);
        return new FlightBookingAcknowledgment("SUCCESS",passengerInfo.getFare(), UUID.randomUUID().toString().split("-")[0],passengerInfo);

    }
}
