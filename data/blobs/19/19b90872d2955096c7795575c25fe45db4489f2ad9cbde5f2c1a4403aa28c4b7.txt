package collectionsframework.collections.queues.queue.priorityqueue.order;

import java.util.PriorityQueue;
import java.util.Queue;

public class CustomerOrderTest {

    public static void main(String[] args) {
        // создаем три заказа клиентов и добавляем их в очередь приоритетов.
        CustomerOrder c1 = new CustomerOrder(1, 100.0, "customer1");
        CustomerOrder c2 = new CustomerOrder(3, 50.0, "customer3");
        CustomerOrder c3 = new CustomerOrder(2, 300.0, "customer2");

        Queue<CustomerOrder> customerOrders = new PriorityQueue<>();
        customerOrders.add(c1);
        customerOrders.add(c2);
        customerOrders.add(c3);
        while (!customerOrders.isEmpty()) {
            System.out.println(customerOrders.poll());
        }

        CustomerOrder cc1 = new CustomerOrder(1, 100.0, "customer1");
        CustomerOrder cc2 = new CustomerOrder(3, 50.0, "customer3");
        CustomerOrder cc3 = new CustomerOrder(2, 300.0, "customer2");
        Queue<CustomerOrder> customerOrdersComparator = new PriorityQueue<>(new CustomerOrderComparator());
        customerOrdersComparator.add(cc1);
        customerOrdersComparator.add(cc2);
        customerOrdersComparator.add(cc3);
        while (!customerOrdersComparator.isEmpty()) {
            System.out.println(customerOrdersComparator.poll());
        }
    }
}
