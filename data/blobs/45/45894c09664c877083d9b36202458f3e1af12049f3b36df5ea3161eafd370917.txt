package exemplo.view;

import exemplo.model.Customer;
import exemplo.model.Order;
import exemplo.model.OrderItem;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import exemplo.service.OrderService;

import javax.faces.view.ViewScoped;
import java.util.ArrayList;
import java.util.List;

@Component
public class OrderView {
    private final OrderService orderService;
    private Order order;
    private Customer customer;
    private OrderItem item;
    private List<OrderItem> items;

    public OrderView(OrderService orderService) {
        this.orderService = orderService;
    }

    @Autowired
    public void init() {
        order = new Order();
        customer = new Customer();
        item = new OrderItem();
        items = new ArrayList<>();
    }

    public Order save() {
        order.setCustomer(customer);
        order.setItems(items);
        orderService.save(order);

        order = new Order();
        items = new ArrayList<>();
        customer = new Customer();

        return order;
    }

    public void delete(Long id) {
        orderService.delete(id);
    }

    public List<Order> findAll() {
        return orderService.findAll();
    }

    public void update(Long id, Order newOrder) {
        orderService.update(id, newOrder);
    }

    public void addItem() {
        items.add(item);

        item = new OrderItem();
    }

    public void resetItem() {
        item = new OrderItem();
        items = new ArrayList<>();
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

    public OrderItem getItem() {
        return item;
    }

    public void setItem(OrderItem item) {
        this.item = item;
    }

    public List<OrderItem> getItems() {
        return items;
    }

    public void setItems(List<OrderItem> items) {
        this.items = items;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}
