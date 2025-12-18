/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        maxPathHelper(root);
        return max;
        
    }
    private int maxPathHelper(TreeNode root) {
        if(root == null){
            return 0;
        }
        int left = Math.max(0,maxPathHelper(root.left));
        int right = Math.max(0,maxPathHelper(root.right));
        int path = root.val + left + right;
        max = Math.max(max,path);
        return Math.max(left,right)+ root.val;
    }
    
}