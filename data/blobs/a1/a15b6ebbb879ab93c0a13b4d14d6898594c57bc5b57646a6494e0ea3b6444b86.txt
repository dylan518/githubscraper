import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Queue {
    Node front, rear;

    Queue() {
        this.front = this.rear = null;
    }

    void enqueue(int data) {
        Node newNode = new Node(data);

        if (this.rear == null) {
            this.front = this.rear = newNode;
            return;
        }

        this.rear.next = newNode;
        this.rear = newNode;
    }

    int dequeue() {
        if (this.front == null) {
            System.out.println("Queue is empty");
            return -1;
        }

        int data = this.front.data;
        this.front = this.front.next;

        if (this.front == null) {
            this.rear = null;
        }

        return data;
    }

    void display() {
        if (this.front == null) {
            System.out.println("Queue is empty");
            return;
        }

        Node temp = this.front;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
}

public class SimpleQueue {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Queue queue = new Queue();
        int choice, data;

        do {
            System.out.println("\nQueue Operations:");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Display");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter data to enqueue: ");
                    data = scanner.nextInt();
                    queue.enqueue(data);
                    break;
                case 2:
                    data = queue.dequeue();
                    if (data != -1) {
                        System.out.println("Dequeued element: " + data);
                    }
                    break;
                case 3:
                    System.out.println("Queue elements:");
                    queue.display();
                    break;
                case 4:
                    System.out.println("Exiting program");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 4);
        scanner.close();
    }
}

