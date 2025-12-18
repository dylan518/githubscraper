package BinaryTreeLevelOrderTraversal102;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

public class BinaryTreeLevelOrderTraversal {
    private class Node {
        public int value;
        public Node left;
        public Node right;

        public Node(int value) {
            this.value = value;
        }
    }

    public Node root;

    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> list = new ArrayList<>();
        if (root == null) {
            return list;
        }
        var queue = new ArrayDeque<Node>();
        queue.add(root);
        while (!queue.isEmpty()) {
            var l = new ArrayList<Integer>();
            var qSize = queue.size();
            for (var i = 0; i < qSize; i++) {
                var popped = queue.remove();
                l.add(popped.value);
                var left = popped.left;
                if (left != null) {
                    queue.add(left);
                }
                var right = popped.right;
                if (right != null) {
                    queue.add(right);
                }
            }
            list.add(l);
        }
        return list;
    }
}
