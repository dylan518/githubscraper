package learn_oop_2.library_readers;

class Reader {

    protected String fullName;
    protected int ticketID;
    protected String faculty;
    protected String dateOfBirth;
    protected int phoneNumber;
    protected int amountOfBooks;

    public Reader(String fullName) {
        this.fullName = fullName;
    }

    void takeBook(int amountOfBooks) {
        System.out.println(fullName + " took " + amountOfBooks + " books");
    }

    void takeBook(String ... bookTitles) {
        System.out.println(fullName + "took the next books: ");
        for (String title : bookTitles) {
            System.out.printf("%s \t", title);
        }
    }

    void takeBook(Book ... books) {
        System.out.println(fullName + "took the next books: ");
        for (Book book : books) {
            System.out.printf("%s \t", book.getTitle());
        }
    }

    void returnBook(int amountOfBooks) {
        System.out.println(fullName + " returned " + amountOfBooks + " books");
    }

    void returnBook(Book book) {
        System.out.printf("%s", fullName + " returned the next book: " + book.getTitle());
    }

    void returnBook(Book ... books) {
        System.out.println(fullName + " returned next books: ");
        for (Book  book : books) {
            System.out.printf("%s \t", book.getTitle());
        }
    }
}
