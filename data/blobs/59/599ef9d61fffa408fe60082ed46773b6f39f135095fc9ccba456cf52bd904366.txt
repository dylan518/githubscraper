package tree;

import java.util.HashMap;
import java.util.Set;
import java.util.Stack;
import java.util.TreeSet;

import static tree.HeightBinaryTree.Node;
//        10
//   20         30
//          40      50

// 20 10 40 30 50
public class IterativeInOrderPreOrderPostOrder {
    public static void main(String args[]) {

        inOrder(new Node(10, new Node(20), new Node(30, new Node(40), new Node(50))));
        System.out.println();
        preOrder(new Node(10, new Node(20), new Node(30, new Node(40), new Node(50))));
        System.out.println();
        inOrder(new Node(10, new Node(20), new Node(30, new Node(40), null)));
        System.out.println();
        inOrder(new Node(10, new Node(20), new Node(30, new Node(40), new Node(50, null, new Node(60)))));
        System.out.println();
        inOrder(new Node(10, new Node(20), new Node(30, new Node(40), new Node(50, new Node(55), null))));

    }

    public static void preOrder(Node node) {
        if (node == null) return;
        Stack<Node> stack = new Stack<>();
        stack.push(node);
        while (!stack.empty()) {
            node = stack.pop();
            System.out.print(node.data + " ");

            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }
    }

    public static void inOrder(Node node) {
        if (node == null) return;
        Stack<Node> stack = new Stack<>();
        stack.push(node);
        while (!stack.empty()) {
            if (node == null || node.left == null) {
                node = stack.pop();
                System.out.print(node.data + " ");
                if (node.right != null) {
                    node = node.right;
                    stack.push(node);
                } else {
                    node = null;
                }
            } else {
                node = node.left;
                stack.push(node);
            }
        }
    }

    public static void inorder1(Node node) {
        if (node == null) return;
        Stack<Object> stack = new Stack<>();
        stack.push(node);
        while (!stack.empty()) {
            if (stack.peek() instanceof Integer) {
                System.out.print(stack.pop() + " ");
            } else {
                node = (Node) stack.pop();
                if (node.left == null && node.right == null) {
                    System.out.print(node.data + " ");
                } else {
                    if (node.right != null)
                        stack.push(node.right);
                    stack.push(node.data);
                    if (node.left != null)
                        stack.push(node.left);
                }
            }
        }
    }

    public static void inorder2(Node node) {
        if (node == null) return;
        Stack<Node> stack = new Stack<>();
        Set<Node> processed = new TreeSet<>();
        stack.push(node);
        while (!stack.empty()) {

            node = stack.pop();
            if (node.left == null && node.right == null) {
                System.out.print(node.data + " ");
            } else if (!processed.contains(node.right)
                    || !processed.contains(node.left)) {
                if (node.right != null) {
                    stack.push(node.right);
                    processed.add(node.right);
                }
                stack.push(node);
                if (node.left != null) {
                    stack.push(node.left);
                    processed.add(node.left);
                }
            } else {
                System.out.print(node.data + " ");
                if (node.right != null) {
                    processed.remove(node.right);
                }
                if (node.left != null) {
                    processed.remove(node.left);
                }
            }

        }
    }
}
