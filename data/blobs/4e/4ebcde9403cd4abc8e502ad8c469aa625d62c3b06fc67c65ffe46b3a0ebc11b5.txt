package com.example.drawingtrees;

public class Tree {
    private TreeNode root;

    public Tree(int startingData) {
        root = new TreeNode();
        root.data = startingData;
    }

    public void insert(int data) {
        insert(root, data);
    }

    private void insert(TreeNode node, int data) {
        if (node == null) return;
        if (node.data == data) return;
        if (data > node.data) {
            if (node.right == null) {
                node.right = new TreeNode();
                node.right.data = data;
            } else {
                insert(node.right, data);
            }
        }
        if (data < node.data) {
            if (node.left == null) {
                node.left = new TreeNode();
                node.left.data = data;
            } else {
                insert(node.left, data);
            }
        }
    }

    public void genTen() {
        for (int i=1; i<=10; i++) {
            this.insert(i);
        }
    }

    private class TreeNode {

        int data;
        TreeNode left;
        TreeNode right;
    }
}
