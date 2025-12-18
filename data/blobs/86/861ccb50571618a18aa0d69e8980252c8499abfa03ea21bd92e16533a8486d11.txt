package tda.darkarmy.ordermanagementservice.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import tda.darkarmy.ordermanagementservice.dto.OrderDto;
import tda.darkarmy.ordermanagementservice.service.OrderService;

import static org.springframework.http.ResponseEntity.status;

@RestController
@RequestMapping("/orders")
public class OrderController {
    @Autowired
    private OrderService orderService;

    @GetMapping("/")
    public ResponseEntity<?> getAll(){
        return status(200).body(orderService.getAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getById(@PathVariable("id") Long id){
        return status(200).body(orderService.getById(id));
    }

    @PostMapping("/")
    public ResponseEntity<?> create(@RequestBody OrderDto orderDto){
        return status(200).body(orderService.create(orderDto));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> cancelOrder(@PathVariable("id") Long id){
        return status(200).body(orderService.cancelOrder(id));
    }
}
