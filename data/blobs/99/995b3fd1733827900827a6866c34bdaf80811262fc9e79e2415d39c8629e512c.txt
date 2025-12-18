package CompareObjects;

public class Comparing implements Comparable<Comparing>{
    int rNo;
    int marks;

    public Comparing(int rNo, int marks) {
        this.rNo = rNo;
        this.marks = marks;
    }

    @Override
    public String toString() {
        return  marks + " ";
    }

    @Override
    public int compareTo(Comparing o) {
        return this.marks - o.marks;
    }
}
