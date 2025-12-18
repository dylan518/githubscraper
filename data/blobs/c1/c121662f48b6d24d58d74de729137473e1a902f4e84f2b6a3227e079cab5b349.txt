package Tree;

public class SymmetricTree {

    static class TreeNode{
        int value;
        TreeNode left;
        TreeNode right;

        TreeNode(int value){
            this.value = value;
            this.left = null;
            this.right = null;
        }

    }

    boolean isSymmentric(TreeNode root){
        return isMirror(root, root);
    }

    private boolean isMirror(TreeNode t1, TreeNode t2){
        if (t1 == null && t2 == null){
            return true;
        }

        if (t1 == null || t2 == null){
            return false;
        }

        return (t1.value == t2.value) && isMirror(t1.left,t2.right) && isMirror(t1.right,t2.left);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(3);

        SymmetricTree tree = new SymmetricTree();
        boolean symmentric = tree.isSymmentric(root);
        System.out.println(symmentric ? "Tree is a Symmetric" : "Tree is not a Symmetric");

    }
}
