/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public TreeNode reverseOddLevels(TreeNode root) {
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        boolean oddLevel = false;

        while (!q.isEmpty()) {

            int level = q.size();
            List<TreeNode> list = new ArrayList<>();

            for (int i = 0; i < level; i++) {
                TreeNode node = q.poll();
                TreeNode left = node.left;
                TreeNode right = node.right;

                list.add(node);
                if (left != null)
                    q.offer(left);
                if (right != null)
                    q.offer(right);
            }
            if (oddLevel) {
                int i = 0, j = list.size() - 1;
                while (i < j) {
                    TreeNode front = list.get(i);
                    TreeNode back = list.get(j);
                    int temp = front.val;
                    front.val = back.val;
                    back.val = temp;
                    i++;
                    j--;
                }
            }
            oddLevel = !oddLevel;

        }
        return root;
    }
}