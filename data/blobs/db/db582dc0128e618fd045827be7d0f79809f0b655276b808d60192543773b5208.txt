public class FlappyBird<E extends Comparable<E>> {
    public FlappyNode<E> root;
    public FlappyBird() {
        root = null;
    }
    
    public void insert(E data) {
        if (root == null) {
            root = new FlappyNode<E>(data); 
        } else {
            root.insert(data); 
        }
    }
    
    public void search(E value) {
        E hasil = searchBSTHelper(root, value);
        if (hasil != null) {
            System.out.println(hasil + " telah dimasukkan.");
        } else
            System.out.println(value + " tidak ditemukan, belum dimasukkan.");
    }
        
    public E searchBSTHelper(FlappyNode<E> node, E value) {
        E result = null;
            if (node != null) {
                if (value.equals(node.getData()))
                    result = node.getData();
                else if (value.compareTo(node.getData()) < 0)
                    result = searchBSTHelper(node.getLeftNode(), value);
                else
                    result = searchBSTHelper(node.getRightNode(), value);
            }
            return result;
    }

    public boolean BSTsearch(E value) {
        return search(root, value);
    }

    private boolean search(FlappyNode r, E value) {
        if (r.getData() == value) 
            return true;
        if (r.getLeftNode() != null)
            if (search(r.getLeftNode(), value))
                return true;
        if (r.getRightNode() != null) 
            if (search(r.getRightNode(), value))
                return true;
        return false;
    }

    public void inorder() {
        inorder(root);
    }
    private void inorder(FlappyNode r){
        if (r != null)
        {
            inorder(r.getLeftNode());
            System.out.print(r.getData() + " ");
            inorder(r.getRightNode());
        }
    }

    public void preorder() {
        preorder(root);
    }
    private void preorder(FlappyNode r) {
        if (r != null) {
            System.out.print(r.getData() + " ");
            preorder(r.getLeftNode());
            preorder(r.getRightNode());
        }
    }

    public void postorder() {
        postorder(root);
    }
    private void postorder(FlappyNode r) {
        if (r != null) {
            postorder(r.getLeftNode());
            postorder(r.getRightNode());
            System.out.print(r.getData() + " ");
        }
    }
}