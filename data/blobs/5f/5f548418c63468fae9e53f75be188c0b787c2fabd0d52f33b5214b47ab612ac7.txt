package org.vinit.datastructure.leetcode.leetcode150.bst;

import org.vinit.interviews.TechRound;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Medium_ZigZagTraversal_103 {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int level = 0;
        boolean startFromLeft = true;
        while (!q.isEmpty()) {
            int count = q.size();
            level++;
            LinkedList<Integer> levelRow = new LinkedList<>();
            while (count > 0) {
                TreeNode node = q.poll();
                if (level % 2 != 0) levelRow.add(node.val);
                else levelRow.addFirst(node.val);

                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);

                count--;
            }
            result.add(levelRow);
            startFromLeft = !startFromLeft;
        }
        return result;
    }
}
