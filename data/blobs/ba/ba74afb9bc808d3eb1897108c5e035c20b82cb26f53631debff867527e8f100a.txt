package com.opolo.orderservice.service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.reactive.function.client.WebClient;

import com.opolo.orderservice.client.PaymentClient;
import com.opolo.orderservice.common.Payment;
import com.opolo.orderservice.common.TransactionRequest;
import com.opolo.orderservice.common.TransactionResponse;
import com.opolo.orderservice.entity.Order;
import com.opolo.orderservice.repository.OrderRepository;

@Service
public class OrderService {

    @Autowired
    private OrderRepository repository;

    @Autowired
    private RestTemplate restTemplate;

    @Autowired
    private WebClient.Builder webClientBuilder;

    @Autowired
    private PaymentClient paymentClient;

    public List<Order> getAllOrders() {
        return repository.findAll();
    }

    public List<Optional<Order>> getOrder(Integer id) {
        List<Optional<Order>> order = Stream.of(id)
                .map(repository::findById)
                .collect(Collectors.toList());

        return order;
    }

    public TransactionResponse saveOrder(TransactionRequest request) {
        
        String paymentStatusResponse = "";
        Payment paymentResponse = new Payment();

        Order order = request.getOrder();
        
        Payment payment = request.getPayment();
        payment.setOrderId(order.getId());
        payment.setAmount(order.getPrice());

        // rest call to Payment microservice
        // paymentResponse =
        // restTemplate.postForObject("http://PAYMENT-SERVICE/payment/savePayment",
        // payment, Payment.class);

        /*paymentResponse = webClientBuilder.build()
                .post()
                .uri("http://PAYMENT-SERVICE/payment/savePayment")
                .header(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .body(Mono.just(payment), Payment.class)
                .retrieve()
                .bodyToMono(Payment.class)
                .block();*/

        paymentResponse = paymentClient.saveOrder(payment);

        paymentStatusResponse = paymentResponse.getPaymentStatus().equals("success")
                ? "payment processing successful and order placed"
                : "failure in paymemt, order added in cart";

        repository.save(order);

        return TransactionResponse.builder()
                .order(order)
                .amount(paymentResponse.getAmount())
                .transactionId(paymentResponse.getTransactionId())
                .message(paymentStatusResponse)
                .build();
    }

}
