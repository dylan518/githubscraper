package com.example.servicethanhtoan.controler;


import com.example.servicethanhtoan.dto.request.PaymentOneWay;
import com.example.servicethanhtoan.dto.request.PaymentTwoWay;
import com.example.servicethanhtoan.service.ZaloPayService;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

@RequestMapping("/thanhtoan")
@Controller
@AllArgsConstructor
public class ZaloPayController {
    private ZaloPayService zaloPayService;


    @PostMapping("/zalopay-payment/oneway-trip")
    public ResponseEntity<?> createOrderOneWayTrip(@RequestBody PaymentOneWay paymentOneWay) {
        if (zaloPayService.createOrderOneWayTrip(paymentOneWay)) {
            return ResponseEntity.ok("oke");
        }
        return ResponseEntity.badRequest().build();

    }

    @PostMapping("zalopay-payment/round-trip")
    public ResponseEntity<?> createOrderRoundTrip(@RequestBody PaymentTwoWay paymentTwoWay) {
        if (zaloPayService.createOrderRoundTrip(paymentTwoWay)) {
            return ResponseEntity.ok("oke");
        }
        return ResponseEntity.badRequest().build();
    }


}
