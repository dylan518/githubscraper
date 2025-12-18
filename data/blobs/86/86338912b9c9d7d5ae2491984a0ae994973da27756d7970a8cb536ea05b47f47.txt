package Printable;

public class Magazine {
    public String title;

    public Magazine(String title) {
        this.title = title;
    }

    public String getTitle() {
        return this.title;
    }
    public void print(){
        System.out.println("One of the magazines is");
    }
    @Override

    public String toString() {
        return ("Name of this magazine is " + this.title);
    }

}
