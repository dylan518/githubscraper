package com.salesreport.kafkalistener;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.salesreport.dto.OrderCreationPayload;
import com.salesreport.model.OrderReport;
import com.salesreport.repository.OrderReportRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.time.LocalDate;

@Slf4j
@Service
@RequiredArgsConstructor
public class OrderCreatedConsumer {
    private final OrderReportRepository orderReportRepository;
    private final ObjectMapper objectMapper;
    private static final Logger logger = LoggerFactory.getLogger(OrderCreatedConsumer.class);
    @KafkaListener(topics = "${kafka.topic.order-creation}")
    public void consume(ConsumerRecord<String, Object>record) throws IOException {
        Object value = record.value();
        var payload = objectMapper.readValue(objectMapper.writeValueAsString(value), new TypeReference<OrderCreationPayload>() {});
        var orderDate = LocalDate.now();
        var totalOrders = 1L;
        var totalAmount = payload.getTotalUnitPriceAtOrder();

        var optionalOrderReport = orderReportRepository.findByOrderDate(orderDate);
        if (optionalOrderReport.isPresent()) {
            var orderReport = optionalOrderReport.get();
            totalOrders += orderReport.getTotalOrders();
            totalAmount = totalAmount.add(orderReport.getTotalAmount());
            orderReport.setTotalOrders(totalOrders);
            orderReport.setTotalAmount(totalAmount);
            orderReportRepository.save(orderReport);
        } else {
            var orderReport = new OrderReport();
            orderReport.setOrderDate(orderDate);
            orderReport.setTotalOrders(totalOrders);
            orderReport.setTotalAmount(totalAmount);
            orderReportRepository.save(orderReport);
        }

        logger.info("Received Order Created Payload: {}", payload);
    }

}
