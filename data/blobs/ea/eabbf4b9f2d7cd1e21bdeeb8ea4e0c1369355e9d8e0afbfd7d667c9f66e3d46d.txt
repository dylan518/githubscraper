/* 
Class: SWEN-601 [Software Construction]
Name: Raga Lagudua Ganesan
Email: rl1158@g.rit.edu
Assignment: HW15
The purpose of this assignment is to help us understand the concepts of Binary Tree and Binary Search Tree and implement them.
*/
package homework;

public class BinaryNodePerfect {
    /**
     * Main method to test the isPerfect() method in BinaryNode.java
     * @param args
     */
    public static void main(String[] args) {
    // Imperfect tree
    BinaryNode root = new BinaryNode(2);
    root.BinaryInsert(3);
    root.BinaryInsert(7);
    root.BinaryInsert(9);
    root.BinaryInsert(4);
    root.BinaryInsert(1);
    root.BinaryInsert(6);

    // Perfect tree
    BinaryNode root2 = new BinaryNode(5);
    root2.BinaryInsert(2);
    root2.BinaryInsert(1);
    root2.BinaryInsert(3);
    root2.BinaryInsert(7);
    root2.BinaryInsert(6);
    root2.BinaryInsert(9);

    BinaryNode root3 = new BinaryNode(5);
    root3.BinaryInsert(2);
    root3.BinaryInsert(1);
    root3.BinaryInsert(3);
    root3.BinaryInsert(7);
    root3.BinaryInsert(6);
    root3.BinaryInsert(9);

    System.out.println("Is Tree 1 is perfect: " + root.isPerfect());
    System.out.println("Is Tree 2 is perfect: " + root2.isPerfect());
    //Testing equals method
    System.out.println("Are Tree 1 and Tree 2 equal:" + root.equals(root2));
    System.out.println("Are Tree 2 and Tree 3 equal:" + root2.equals(root3));
    }
}
// end of class BinaryNodePerfect
