package com.Quantum.quantum;

import java.util.List;

//import com.Quantum.quantum.Book;
//import com.Quantum.quantum.Library;

public class App 
{
    public static void main( String[] args )
    {
    	Library library = new Library();

        // Adding books
        Book book1 = new Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Classic", 1925, "Fiction");
        Book book2 = new Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Fiction", 1960, "Fiction");
        library.addBook(book1);
        library.addBook(book2);

        // Removing a book
        library.removeBook("9780743273565");

        // Finding books by title or author
        List<Book> booksByTitle = library.findBookByTitle("To Kill a Mockingbird");
        List<Book> booksByAuthor = library.findBookByAuthor("Harper Lee");

        // Listing all books and available books
        List<Book> allBooks = library.listAllBooks();
        List<Book> availableBooks = library.listAvailableBooks();

        // Displaying results
        System.out.println("Books by title: " + booksByTitle);
        System.out.println("Books by author: " + booksByAuthor);
        System.out.println("All books: " + allBooks);
        System.out.println("Available books: " + availableBooks);
    }
}
