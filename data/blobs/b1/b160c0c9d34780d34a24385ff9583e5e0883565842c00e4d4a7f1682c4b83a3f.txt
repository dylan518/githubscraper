package models;

import java.util.ArrayList;

public class Library {
    String bookName2;
    public int bookQty2;

    public Library(String bookName2, int bookQty2) {
        this.bookName2 = bookName2;
        this.bookQty2 = bookQty2;
    }

    public String getBookName2() {
        return bookName2;
    }

    public int getBookQty2() {
        return bookQty2;
    }

    @Override
    public String toString() {
        return "Library{" +
                "bookName2='" + bookName2 + '\'' +
                ", bookQty2=" + bookQty2 +
                '}';
    }
}
