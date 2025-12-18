package leetcode_111;

public class Solution {
    public int minDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        int minLeft = minDepth(root.left);
        int minRight = minDepth(root.right);
        if(minLeft == 0){
            return 1 + minRight;
        }
        if (minRight == 0) {
            return 1 + minLeft;
        }
        return 1 + Math.min(minLeft, minRight);

    }

}
