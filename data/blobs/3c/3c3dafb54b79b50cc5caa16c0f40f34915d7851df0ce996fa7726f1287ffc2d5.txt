import java.lang.reflect.Array;
import java.util.Random;
import java.util.Stack;

public class SkipList<E extends Comparable<E>> implements AmhSortedSet<E> {

    private Node<E> head;
    private int height;
    private int numElts = 0;
    private Random rand;
    private double p;

    private int countOps = 0;

    public boolean add(E x) {
        // find the predecessor nodes on each level of the list
        Stack<Node<E>> preds = findAllPreds(x);
        Node<E> pred0 = preds.peek();
        //set new node to node after head]
        if(preds.isEmpty()){
            preds.push(head);
            pred0 = preds.peek();
        }
        if(pred0.nextNodes[0] != null && pred0.nextNodes[0].data.equals(x)) {
            return false; // elt x was already present
        }
        //create a new node for elt x, and generate its height
        Node<E> newNode = new Node<E>(x, chooseHeight());
        int newHeight = newNode.getHeight();

        // increase the height of the head node, if needed
        if (newHeight > height) {
            if (newHeight > head.nextNodes.length-1) {
                Node<E>[] temp =  (Node<E>[]) Array.newInstance(Node.class, newHeight+1);
                for(int i = 0; i < head.nextNodes.length; i++) {
                    temp[i] = head.nextNodes[i];
                }
                head.nextNodes = temp;
            }
            for(int i = newHeight; i > height; i--) {
                head.nextNodes[i] = newNode;
            }
            height = newHeight;
        }

        // add x after its predecessor on each level within x's height
        // YOU FILL IN THIS PART
        
        /*add x by swapping using temp
        add the value after its predecessor, 
        that'll mean you'll peek() on the stack to get its node,
        then nextNode[]
        if we're at the end, the nextNode[] should point to null
        */

        for(int i = 0; i<newNode.getHeight(); i++){
            if(preds.isEmpty()){
            Node<E> temp = preds.peek().nextNodes[i];
            preds.peek().nextNodes[i] = newNode;
            newNode.nextNodes[i] = temp;
            preds.pop();
            }
            else{
                newNode.nextNodes[i] = null;
            }  
        }
        numElts++; 
        //System.out.println("Added:" + x);
        return true;
    }

    public E remove(E x) {
        // find the predecessor nodes on each level of the list
        Stack<Node<E>> preds = findAllPreds(x);

        // if the element wasn't present, nothing to return
        Node<E> pred0 = preds.peek();
        if(pred0.nextNodes[0] == null) return null; // empty list
        if(pred0.nextNodes[0] != null && !pred0.nextNodes[0].data.equals(x)) return null; // non-empty list, elt x wasn't present

        // if the elment was present, now we need to remove it from each level on which it appears
        // YOU FILL IN THIS PART

        /*remove on each level
         * start at the heighest level, keep going down.
         * on each level x is on, replace the nextNode
         */

        Node<E> u = head; 
        int r = height; 
        int comp = 0; 
        while (r >= 0) { 
            while (u.nextNodes[r] != null && (comp = compare(u.nextNodes[r].data, x)) < 0) { 
                u = u.nextNodes[r]; 
            } 
            if (u.nextNodes[r] != null && comp == 0) { 
                u.nextNodes[r] = u.nextNodes[r].nextNodes[r]; 
                if (u == head && u.nextNodes[r] == null) 
                height--; 
            } 
            r--; 
        } 
        numElts--; 
        //System.out.println("Removed:" + x);
        return x;
    }

    public E find(E x) {
        // find the predecessor nodes on each level of the list
        Stack<Node<E>> preds = findAllPreds(x);
        Node<E> level0 = preds.pop(); // the top of the stack is the predecessor on level 0
        if (level0.nextNodes[0] == null) {
            System.out.println("Not found");
            return null;
        }
        else {
            System.out.println("Found: " + x + " = " + level0.nextNodes[0].data);
            return level0.nextNodes[0].data;
        }
        
    }

    public int size() {
        return numElts;
    }

    protected Stack<Node<E>> findAllPreds(E x) {
        // this method should return a stack containing the predecessor nodes of element x on each level,
        // with the predecessor on level 0 at the top of the stack and the predecessor at the highest
        // level on the bottom of the stack
        // YOU FILL IN THIS PART

        /*start on highest level, check if each node is less than 'x'
        if it is greater than x, stop and go to the lower level.
        store that in the stack
        */

        countOps = 0;
        Node<E> currNode = head;
        Stack<Node<E>> stackOfPreds = new Stack<Node<E>>();
        if(stackOfPreds.isEmpty()){
            stackOfPreds.push(head);
        }

        int level = height;
        while (level >= 0) {
            while (currNode.nextNodes[level] != null && compare(currNode.nextNodes[level].data,x) < 0){
                stackOfPreds.push((Node <E>) currNode); //add node to stack
                currNode = currNode.nextNodes[level]; //move to the right
                countOps++;
            }
            countOps++;
            level--;// move to a lover level
        }
        //System.out.println("Stack of preds:" + stackOfPreds);
        return stackOfPreds;
    }
    

    private int compare(Object data, E x) {
        if (data == null){
            return 0;
        }
        int intObj1 = (Integer)data;
        int intObj2 = (Integer)x;
 
        // Get the difference
        int difference = intObj1 - intObj2;
 
        if (difference == 0) {// Both are equal
            return 0;
        }
        else if (difference < 0) {// obj1 < obj2
            return -1;
        }
        else {// obj1 > obj2
            return 1;
        }
    }

    public void print() {
        for(int i = 0; i <= height; i++) {
            Node<E> y = head;
            while(y.nextNodes[i] != null) {
                y = y.nextNodes[i];
                System.out.print(y.data + " ");
            }
            System.out.println();
        }
    }


    public int getOps() {
        //System.out.println("Count Ops: " + countOps);
        return countOps;
       
    }

    private int chooseHeight() {
        int level = 0;
        double flip = rand.nextDouble();
        while(flip < p) {
            level++;
            flip = rand.nextDouble();
        }
        return level;
    }

    public SkipList() {
        head = new Node<E>(null, 0);
        height = 0;
        p = 0.5;
        rand = new Random();
    }

    public SkipList(int seed) {
        head = new Node<E>(null, 0);
        height = 0;
        p = 0.5;
        rand = new Random(seed);
    }

    public SkipList(double prob) {
        head = new Node<E>(null,0);
        height = 0;
        p = prob;
        rand = new Random();
    }

    public SkipList(double prob, int seed) {
        head = new Node<E>(null,0);
        height = 0;
        p = prob;
        rand = new Random(seed);
    }

}
