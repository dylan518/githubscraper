package tree.depth.first.search;

public class DiameterOfBinaryTree {

    static int diameter = 0;

    public static void main(String[] args) {
        TreeNode<Integer> left = new TreeNode<>(2);
        TreeNode<Integer> right = new TreeNode<>(17);
        TreeNode<Integer> root = new TreeNode<>(3);
        root.right = right;
        root.left = left;

        TreeNode<Integer> node1 = new TreeNode<>(1);
        TreeNode<Integer> node2 = new TreeNode<>(4);

        left.left = node1;
        left.right = node2;

        System.out.println(diameterOfBinaryTree(root));
    }

    public static int diameterOfBinaryTree(TreeNode<Integer> root) {

        dfs(root);
        return diameter;
    }

    private static int dfs(TreeNode<Integer> node) {
        if (node == null) return -1;

        int leftHeight = dfs(node.left);

        int rightHeight = dfs(node.right);

        diameter = Math.max(diameter, leftHeight + rightHeight + 2);

        return 1 + Math.max(leftHeight, rightHeight);

    }
}
