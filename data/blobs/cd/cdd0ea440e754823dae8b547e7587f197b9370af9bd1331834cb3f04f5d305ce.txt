/**
 * Min Stack
 *
 * Design a stack that supports push, pop, top, and retrieving the minimum
 * element in constant time.
 *
 *   - push(x)  -- Push element x onto stack.
 *   - pop()    -- Removes the element on top of the stack.
 *   - top()    -- Get the top element.
 *   - getMin() -- Retrieve the minimum element in the stack.
 *
 * Tags: Stack, Data Structure
 */
package com.example.leetcode.solutions.min_stack;

import java.util.Stack;

class MinStack {
  private Stack<Integer> stack = new Stack<>();
  private Stack<Integer> minStack = new Stack<>();

  public void push(int value) {
    stack.push(value);
    if (minStack.empty() || value <= minStack.peek()) {
      minStack.push(value);
    }
  }

  public void pop() {
    int x = stack.pop();
    if (x == minStack.peek()) {
      minStack.pop();
    }
  }

  public int top() {
    return stack.peek();
  }

  public int getMin() {
    return minStack.peek();
  }
}
