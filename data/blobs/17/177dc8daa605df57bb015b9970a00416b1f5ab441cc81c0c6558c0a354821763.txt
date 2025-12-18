package com.cs.foodhubuserservice.service;

import com.cs.foodhubuserservice.entity.Orders;
import com.cs.foodhubuserservice.entity.User;
import com.cs.foodhubuserservice.repository.OrderRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class OrderServiceImpl implements IOrderService{

    @Autowired
    private OrderRepository orderRepository;



    @Override
    public Orders addOrder(Orders order) {
        return orderRepository.save(order);
    }

    @Override
    public List<Orders> getAllOrders() {
        return orderRepository.findAll();
    }

    @Override
    public Optional<Orders> getOrderById(Integer orderId) {
        return orderRepository.findById(orderId);
    }


}
