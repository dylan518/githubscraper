package com.teamrocket.service;

import com.teamrocket.proto.CustomerServiceGrpc.CustomerServiceImplBase;
import com.teamrocket.proto.DeliveryData;
import com.teamrocket.proto.SystemOrderId;
import io.grpc.stub.StreamObserver;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

@Service
public class CustomerService extends CustomerServiceImplBase {
    private static final Logger LOGGER = LoggerFactory.getLogger(CustomerService.class);


    @Override
    public void getDeliveryData(SystemOrderId request, StreamObserver<DeliveryData> responseObserver) {
        LOGGER.info("GET DELIVERY DATA FIRED");

        DeliveryData response = DeliveryData
                .newBuilder()
                .setCustomerName("Magdalena Wawrzak")
                .setCustomerPhone("+45 87979887")
                .setDropOfAddressId(784)
                .build();
        responseObserver.onNext(response);

        responseObserver.onCompleted();

        LOGGER.info("Response {}",response);
    }
}
