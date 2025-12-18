// https://www.geeksforgeeks.org/problems/construct-binary-tree-from-parent-array/1
class Node
{
    int data;
    Node left, right;
    Node(int key)
    {
        data = key;
        left = right = null;
    }
}
public class POTD_ConstructBinaryTreeFromParentArray {
    // Function to construct binary tree from parent array.
    public Node createTree(int parent[]) {
        // Your code here
        HashMap<Integer, Node> hm = new HashMap<>();
        Node root = null;
        for (int i = 0; i < parent.length; i++) {
            if (parent[i] == -1) {
                root = new Node(i);
                hm.put(i, root);
            } else {
                hm.put(i, new Node(i));
            }
        }
        for (int i = 0; i < parent.length; i++) {
            if (parent[i] == -1) {
                continue;
            } else {
                Node temp = hm.get(parent[i]);
                if (temp.left == null) {
                    temp.left = hm.get(i);
                } else{
                    temp.right = hm.get(i);
                }
            }
        }
        return root;
    }
}
