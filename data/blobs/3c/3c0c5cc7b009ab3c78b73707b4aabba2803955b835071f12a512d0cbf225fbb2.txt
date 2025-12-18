public class Queue {

    int[] queueElement;
    int rear;
    int front;
    int size;
    int capacity = 5;
    int abc;

    public Queue() {
        queueElement = new int[5];
        this.abc = 3 % 5;
    }

    public int size() {
        return this.size;
    }

    public int front() {
        return queueElement[this.front];
    }

    public int rear() {
        return queueElement[this.rear -1];
    }

    public void enQueue(int data) throws Exception {
        if (this.isQueueFull()) {
            throw new Exception("Size is full");
        }

        size++;
        queueElement[rear] = data;
        rear = ((rear + 1) % capacity);
    }

    public int deQueue() throws Exception {
        if (this.isEmpty()) {
            throw new Exception("Queue us Empty:: Underflow");
        }

        size--;
        int data = queueElement[front % capacity];
        queueElement[front] = Integer.MIN_VALUE;

        front = (front + 1) % capacity;
        return data;

    }

    public boolean isQueueFull() {
        if (this.size == this.capacity) {
            return true;
        }
        return false;
    }

    public boolean isEmpty() {
        if (this.size < 1) {
            return true;
        }
        return false;
    }

    public String show() {
        String result;
        result = "[";

        for (int i = 0; i < size; i++) {
            result += Integer.toString(queueElement[(front + i) % capacity]);
            if (i < (size - 1)) {
                result += ", ";
            }
        }

        result += "]";
        return result;
    }

}
