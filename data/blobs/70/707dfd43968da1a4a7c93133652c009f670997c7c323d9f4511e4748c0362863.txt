public class CodeRunner {
    public static void main(String args[]) {
        LinkedList l= new LinkedList();
        l.insert(10);
        l.insert(12);
        l.insert(20);
        l.insert(24);
        l.insert(25);
        // l.insertAtPos(3, 30);
        // l.deleteAtStart();
        l.deleteAtEnd();
        // l.deleteAtIndex(2);
        l.show();
    }
}