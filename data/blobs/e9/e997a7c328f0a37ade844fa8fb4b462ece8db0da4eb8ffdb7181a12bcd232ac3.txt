public class Stack {
	int[] container;
	int top;

	// new()
	Stack(int size) {
		container = new int[size];
		top = -1;
	}

	// clear
	void clear() {
		top = -1;
	}

	// check if stack is empty
	boolean isEmpty() {
		if (top == -1) {
			return true;
		} else {
			return false;
		}
	}

	// check if stack is full
	boolean isFull() {
		if (top == container.length - 1) {
			return true;
		} else {
			return false;
		}
	}

	// pushing

	void push(int item) {
		top++;
		container[top] = item;
	}

	// popping an item from the stack
	int pop() {
		int temp = container[top];
		top--;
		return temp;
	}

	// peek
	int peek() {
		return container[top];
	}
}
