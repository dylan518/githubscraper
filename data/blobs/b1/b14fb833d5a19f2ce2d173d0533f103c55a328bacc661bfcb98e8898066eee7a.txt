package offer;

public class IsSubStructure {

    public static class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
   }

    public static boolean isSubStructure(TreeNode A, TreeNode B) {
        if (A == null || B == null) {
            return false;
        }
        return recur(A, B) || isSubStructure(A.left, B) || isSubStructure(A.right, B);
    }

    private static boolean recur(TreeNode A, TreeNode B) {
        if (B == null) {
            return true;
        }
        if (A == null || A.val != B.val) {
            return false;
        }
        return recur(A.left, B.left) && recur(A.right, B.right);
    }

    public static void main(String[] args) {
        TreeNode A = new TreeNode(3);
        TreeNode ALeft = new TreeNode(4);
        TreeNode ARight = new TreeNode(4);
        A.left = ALeft;
        A.right = ARight;
        TreeNode ALeftLeft = new TreeNode(1);
        TreeNode ALeftRight = new TreeNode(2);
        ALeft.left = ALeftLeft;
        ALeft.right = ALeftRight;
        TreeNode B = new TreeNode(4);
        B.left = new TreeNode(1);
        System.out.println(isSubStructure(A, B));
    }
}
