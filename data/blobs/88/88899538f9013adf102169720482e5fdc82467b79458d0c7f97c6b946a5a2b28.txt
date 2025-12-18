package binaeryTree.traversals;

import java.util.*;

public class BinaryTreePostOrderTraversal {
    //constructor to initialise tree class
    public BinaryTreePostOrderTraversal(){}

    //node structure
    private static class Node{
        int val;
        Node left;
        Node right;

        //constructor to initialise every node
        public Node(int val){
            this.val = val;
        }
    }

    //declaring a root node object reference
    private Node root;

    //populating the tree
    public void populate(Scanner s){
        System.out.println("Enter value for root node : ");
        int value = s.nextInt();
        root = new Node(value);
        populate(s, root);
    }

    private void populate(Scanner s, Node node) {
        //left node
        System.out.println("Wanna go left of "+node.val+" ?");
        boolean left = s.nextBoolean();
        if(left){
            System.out.print("Enter value for node : ");
            int val = s.nextInt();
            node.left = new Node(val);     //defining new node at previous node's left
            populate(s, node.left);
        }

        //right node
        System.out.println("Wanna go right of "+node.val+" ?");
        boolean right = s.nextBoolean();
        if(right){
            System.out.print("Enter value for node : ");
            int val = s.nextInt();
            node.right = new Node(val);
            populate(s, node.right);
        }
    }

    //displaying the tree in post-order
    public List<Integer> display(){
        List<Integer> out = new ArrayList<>();
        return postOrder(root, out);
    }
    private List<Integer> postOrder(Node root, List out){
        if (root == null){
            return out;
        }
        postOrder(root.left, out);
        postOrder(root.right, out);
        out.add(root.val);
        return out;
    }

    //main method
    public static void main(String[] args) {
        BinaryTreePostOrderTraversal tree = new BinaryTreePostOrderTraversal();
        Scanner s = new Scanner(System.in);
        tree.populate(s);

        System.out.println("Post-Order Traversal : ");
        System.out.println(tree.display());
    }
}
