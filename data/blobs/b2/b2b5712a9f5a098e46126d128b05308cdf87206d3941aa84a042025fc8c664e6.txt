package com.coffeeshop.orderservice.service;

import com.coffeeshop.orderservice.common.OrderStatus;
import com.coffeeshop.orderservice.model.*;
import com.coffeeshop.orderservice.repository.OrderRepository;
import com.coffeeshop.orderservice.repository.QueueRepository;
import com.coffeeshop.orderservice.repository.QueueStatusRepository;
import com.coffeeshop.orderservice.repository.UserRepository;
import com.coffeeshop.orderservice.request.ItemRequest;
import com.coffeeshop.orderservice.request.OrderRequest;
import com.coffeeshop.orderservice.response.OrderResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.util.CollectionUtils;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;


@Service
@RequiredArgsConstructor
@Slf4j
public class OrderServiceImpl implements OrderService{

    private final OrderRepository orderRepository;
    private final QueueRepository queueRepository;

    private final UserRepository userRepository;

    private final QueueStatusRepository queueStatusRepository;

    @Override
    public OrderResponse placeOrder(OrderRequest orderRequest) {

        try{

            Order order = new Order();
            Queue queue;
            User user ;
            //check user to see if user is registered
            Optional<User> userOptional = userRepository.findById(orderRequest.getUserId());

            //finding available queue from shop
            List<Queue>  queues = queueRepository.findByShopIdOrderByQueueNumber(orderRequest.getShopId());


            if (CollectionUtils.isEmpty(queues) || !userOptional.isPresent()){
                if (CollectionUtils.isEmpty(queues) ){
                    return new OrderResponse(false,"UNAVAILABLE_SHOP","Shop queues is full");
                }else {
                    return new OrderResponse(false,"USER_NOT_FOUND","User not found");
                }
            }

            if (queues.stream().findFirst().isPresent()){
                queue = queues.stream().findFirst().get();
                queue.setQueueNumber(queue.getQueueNumber() +1);
                if (queue.getQueueNumber().equals(queue.getMaxQueueSize())){
                    queue.setCurrentStatus(false);
                }
                //save Queue to DB
                queueRepository.save(queue);
                user = userOptional.get();

                order.setUser(user);
                LocalDateTime currentTime = LocalDateTime.now();
                order.setOrderTime(currentTime);
                Set<Item> items = orderRequest.getItemRequests().stream()
                        .map(this::mapToItemDto)
                        .collect(Collectors.toSet());
                order.setItems(items);
                order.setStatus(OrderStatus.PLACED.toString());
                //save Order to DB
                orderRepository.save(order);

                //check Queue at previous position

                QueueStatus queueStatus = new QueueStatus();
                queueStatus.setQueue(queue);
                queueStatus.setUserUser(user);
                queueStatus.setPosition(queue.getQueueNumber());
                //average service time per a customer = 20 minutes, if the queue is having 3 waiting customers, current customer will have to wait 20 *4 =80 minutes
                queueStatus.setEstimatedPickupTime(currentTime.plusMinutes(20L *queue.getQueueNumber()));
                //save QueueStatus to DB
                queueStatusRepository.save(queueStatus);
            }

        }catch (Exception exception){
            log.error(exception.getMessage());
            return new OrderResponse(false,"INTERNAL_SERVER_ERROR","Unable to place the order");
        }
        return new OrderResponse(true,"CREATED","Order Placed Successfully");

    }

    private Item mapToItemDto(ItemRequest itemRequest){
        Item item = new Item();
        item.setItemName(itemRequest.getItemName());
        item.setDescription(itemRequest.getDescription());
        item.setQuantity(itemRequest.getQuantity());
        item.setPrice(itemRequest.getPrice());
        return item;
    }
}
