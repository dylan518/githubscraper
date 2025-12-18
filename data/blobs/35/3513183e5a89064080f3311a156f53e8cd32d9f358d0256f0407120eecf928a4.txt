import java.util.Objects;

public class ChainedList {
    private Node Head;
    public ChainedList() {
        this.Head = null;
    }

    public void Insert(Object a) {
        Node x = new Node();
        x.setInformation(a);
        if(this.Head == null) {
            this.Head = x;
        }
        else {
            Node last = this.findLast(this.Head);
            x.setPrevious(last);
            last.setNext(x);
        }
    }

    public void Delete(Object value) {
        Node x = this.Find(value);
        this._Delete(x);
    }

    private void _Delete(Node x) {
        if(x == null) return;

        Node p = x.getPrevious();
        Node n = x.getNext();

        if(Objects.equals(x, this.Head)) {
            if(n != null) {
                this.Head = n;
                n.setPrevious(null);
            } else this.Head = null;
//            x = null;
//            return;
        }

        if(n != null && p != null) {
            p.setNext(n);
            n.setPrevious(p);
        }

        if(Objects.equals(x, this.findLast(x))) {
            p.setNext(null);
        }

        x.setPrevious(null);
        x.setNext(null);
        x = null;
    }

    public Node Find(Object value) {
        return this.findRecursively(this.Head, value);
    }

    public void Update(Object oldValue, Object newValue) {
        Node x = this.Find(oldValue);
        if(x == null) return;
        x.setInformation(newValue);
    }

    private Node findByIndex(Node from, int index) {
        return new Node();
    }

    private Node findRecursively(Node from, Object value) {
        if(from.getNext() != null) {
            if(Objects.equals(value, from.getInformation())) {
                return from;
            }
            else {
                return findRecursively(from.getNext(), value);
            }
        }
        else {
            if(Objects.equals(value, from.getInformation())) {
                return from;
            }
        }
        return null;
    }

    private Node findLast(Node n) {
        if(n.getNext() != null) {
            return findLast(n.getNext());
        }
        else {
            return n;
        }
    }

    public void printAll() {
        this._printAll(this.Head);
    }

    private void _printAll(Node n) {
        if(n == null) return;
        System.out.println(n.getInformation());
        if(n.getNext() != null) {
            _printAll(n.getNext());
        }
    }

}
