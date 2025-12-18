package com.cloudnative.demo.controller;

import com.cloudnative.demo.domain.Order;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;


@RestController
public class OrderController {

    @GetMapping("/v1/orders")
    public ResponseEntity<List<Order>> healthCheck(){
        List<Order> orders = List.of(Order.builder().id(1).quantity(2).user("ABC").location("BLR").build(),
                Order.builder().id(2).quantity(5).user("DEF").location("KOL").build());
        return ResponseEntity.ok(orders);
    }
}
