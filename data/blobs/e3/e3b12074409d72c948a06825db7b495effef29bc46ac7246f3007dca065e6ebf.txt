package com.pattern.go.datastructure.sub04queue;

public class LoopQueue<E> implements Queue<E> {

  private E[] data;
  private int front, tail;
  private int size;

  @SuppressWarnings("unchecked")
  public LoopQueue(int capacity) {

    data = (E[]) new Object[capacity + 1];
    front = 0;
    tail = 0;
    size = 0;
  }

  public LoopQueue() {

    this(10);
  }

  public int getCapacity() {

    return data.length - 1;
  }

  @Override
  public int getSize() {

    return size;
  }

  @Override
  public boolean isEmpty() {

    return front == tail;
  }

  @Override
  public void enqueue(E element) {

    if ((tail + 1) % data.length == front) {
      resize(getCapacity() * 2);
    }

    data[tail] = element;
    tail = (tail + 1) % data.length;
    size++;
  }

  @Override
  public E dequeue() {

    if (isEmpty()) {
      throw new IllegalArgumentException("Cannot dequeue from an empty queue.");
    }

    E result = data[front];
    data[front] = null;
    front = (front + 1) % data.length;
    size--;

    if (size == getCapacity() / 4 && getCapacity() / 2 != 0) {
      resize(getCapacity() / 2);
    }

    return result;
  }

  @Override
  public E getFront() {
    if (isEmpty()) {
      throw new IllegalArgumentException("Queue is empty.");
    }

    return data[front];
  }

  private void resize(int newCapacity) {

    @SuppressWarnings("unchecked")
    E[] newData = (E[]) new Object[newCapacity + 1];

    for (int i = 0; i < size; i++) {
      newData[i] = data[(front + i) % data.length];
    }

    data = newData;
    front = 0;
    tail = size;
  }

  @Override
  public String toString() {

    StringBuilder result = new StringBuilder();

    result.append(String.format("Queue: size = %d , capacity = %d\n", size, getCapacity()));
    result.append("front [");
    for (int i = front; i != tail; i = (i + 1) % data.length) {
      result.append(data[i]);
      if ((i + 1) % data.length != tail) {
        result.append(", ");
      }
    }
    result.append("] tail");

    return result.toString();
  }
}
