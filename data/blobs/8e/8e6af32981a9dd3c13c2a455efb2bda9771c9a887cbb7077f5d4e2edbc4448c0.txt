package home_work.seminar4_test;

public class ArrayStack {
    private Object[] stack;
    private int size;
    private int position = -1;


    // конструктор по умолчанию
    // создаёт стэк размером на 16 элементов
    public ArrayStack() {
        size = 16;
        stack = new Object[size];
    }


    // альтернативный конструктор
    // создаёт стэк заданного размера
    public ArrayStack(int size) {
        if (size > 0) {
            this.size = size;
            stack = new Object[size];
        }
        else {
            throw new IllegalArgumentException("size must be greater than 0");
        }
    }

    public void push(Object obj) {
        position += 1;
        if (position == size) {
            extendStack();
        }
        stack[position] = obj;
    }

    public Object pop() {
        if (isEmpty()) {
            return null;
        }
        position -= 1;
        return stack[position + 1];
    }

    public Object peek() {
        if (isEmpty()) {
            return null;
        }
        return stack[position];
    }

    public boolean isEmpty() {
        if (position < 0) {
            return true;
        }
        return false;
    }

    public int size() {
        return position + 1;
    }

    public int internalSize() {
        return size;
    }

    private void extendStack() {
        int newSize = size * 2;
        Object[] newStack = new Object[newSize];
        int i;
        for (i = 0; i < size; i++) {
            newStack[i] = stack[i];
        }
        stack = newStack;
        size = newSize;
    }

    // метод довольно плохой, но для проверки или демонстрации сгодится
    // по сути стеку вообще не нужен этот метод
    public void show() {
        for (int i = 0; i < stack.length; i++) {
            System.out.print(stack[i] + " ");
        }
    System.out.println();
    }
}