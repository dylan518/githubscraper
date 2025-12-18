import java.util.List;
import java.util.Scanner;

import library.Author;
import library.Book;
import library.Library;
import library.Patron;

public class Main {
    public static void main(String[] args) {
        // Create a library
        Library library = new Library();

        // Create authors
        Author author1 = new Author("John Doe", "1980-01-01");
        Author author2 = new Author("Jane Smith", "1975-05-15");

        // Create books
        Book book1 = new Book("Book 1", author1, "ISBN-1", "Publisher A", 5);
        Book book2 = new Book("Book 2", author1, "ISBN-2", "Publisher B", 3);
        Book book3 = new Book("Book 3", author2, "ISBN-3", "Publisher C", 7);

        // Add books to the library
        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);

        // Create patrons
        Patron patron1 = new Patron("Alice", "123 Main St", "555-1234");
        Patron patron2 = new Patron("Bob", "456 Elm St", "555-5678");

        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Main menu loop
        while (true) {
            System.out.println("Library Management System");
            System.out.println("1. Add book");
            System.out.println("2. Borrow book");
            System.out.println("3. Return book");
            System.out.println("4. Edit book");
            System.out.println("5. Delete book");
            System.out.println("6. Add author");
            System.out.println("7. Edit author");
            System.out.println("8. Delete author");
            System.out.println("9. List books by author");
            System.out.println("10. Add Patron");
            System.out.println("11. Edit Patron");
            System.out.println("12. Delete Patron");
            System.out.println("13. Search Books by Patron");
            System.out.println("14. Exit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline character

            switch (choice) {
                case 1:
                    addBook(library, scanner);
                    break;
                case 2:
                    borrowBook(library, scanner);
                    break;
                case 3:
                    returnBook(library, scanner);
                    break;
                case 4:
                    editBook(library, scanner);
                    break;
                case 5:
                    deleteBook(library, scanner);
                break;
                    case 6:
                    addAuthor(library, scanner);
                    break;
                case 7:
                    editAuthor(library, scanner);
                    break;
                case 8:
                    deleteAuthor(library, scanner);
                    break;
                case 9:
                    searchBooksByAuthor(library, scanner);
                    break;
                case 10:
                    addPatron(library, scanner);
                    break;
                case 11:
                    editPatron(library, scanner);
                    break;
                case 12:
                    deletePatron(library, scanner);
                    break;
                case 13:
                    searchBooksByPatron(library, scanner);
                    break;
                case 14:
                    System.out.println("Exiting...");
                    scanner.close(); // Close the Scanner object
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }


    // Method to delete a patron from the library
    private static void deletePatron(Library library, Scanner scanner) {
        // Prompt for patron name
        System.out.print("Enter the name of the patron you want to delete: ");
        String name = scanner.nextLine();

        // Search for the patron
        Patron patron = library.searchPatronByName(name);
        if (patron != null) {
            // Delete the patron from the library
            library.deletePatron(patron);

            System.out.println("Patron deleted successfully!");
        } else {
            System.out.println("Patron not found. Please check the patron name and try again.");
        }
    }

    // Method to edit a patron in the library
    private static void editPatron(Library library, Scanner scanner) {
        // Prompt for old patron name
        System.out.print("Enter the name of the patron you want to edit: ");
        String oldName = scanner.nextLine();

        // Search for the old patron
        Patron oldPatron = library.searchPatronByName(oldName);
        if (oldPatron != null) {
            // Prompt for new patron information
            System.out.print("Enter new patron name: ");
            String newName = scanner.nextLine();
            System.out.print("Enter new patron address: ");
            String newAddress = scanner.nextLine();
            System.out.print("Enter new patron phone number: ");
            String newPhoneNumber = scanner.nextLine();

            // Create a new patron object with updated information
            Patron newPatron = new Patron(newName, newAddress, newPhoneNumber);

            // Edit the patron in the library
            library.editPatron(oldPatron, newPatron);

            System.out.println("Patron edited successfully!");
        } else {
            System.out.println("Patron not found. Please check the patron name and try again.");
        }
    }

    // Method to add a patron to the library
    private static void addPatron(Library library, Scanner scanner) {
        // Prompt for patron information
        System.out.print("Enter patron name: ");
        String name = scanner.nextLine();
        System.out.print("Enter patron address: ");
        String address = scanner.nextLine();
        System.out.print("Enter patron phone number: ");
        String phoneNumber = scanner.nextLine();

        // Create a new patron object
        Patron patron = new Patron(name, address, phoneNumber);

        // Add the patron to the library
        library.addPatron(patron);

        System.out.println("Patron added successfully!");
    }


    private static void deleteAuthor(Library library, Scanner scanner) {
        System.out.print("Enter author name to delete: ");
        String authorName = scanner.nextLine();

        // Call the method to delete the author
        boolean success = library.deleteAuthor(authorName);

        if (success) {
            System.out.println("Author deleted successfully!");
        } else {
            System.out.println("Failed to delete author. Author not found.");
        }
    }

    private static void editAuthor(Library library, Scanner scanner) {
        System.out.print("Enter author name: ");
        String authorName = scanner.nextLine();

        System.out.print("Enter new date of birth: ");
        String newDateOfBirth = scanner.nextLine();

        // Call the method to edit the author's information
        boolean success = library.editAuthor(authorName, newDateOfBirth);

        if (success) {
            System.out.println("Author information updated successfully!");
        } else {
            System.out.println("Failed to update author information. Author not found.");
        }
    }

    private static void addAuthor(Library library, Scanner scanner) {
        System.out.print("Enter author name: ");
        String authorName = scanner.nextLine();

        System.out.print("Enter date of birth: ");
        String dateOfBirth = scanner.nextLine();

        // Call the method to add the author
        boolean success = library.addAuthor(authorName, dateOfBirth);

        if (success) {
            System.out.println("Author added successfully!");
        } else {
            System.out.println("Failed to add author. Author already exists.");
        }
    }


    // Method to search books by author
    private static void searchBooksByAuthor(Library library, Scanner scanner) {
        // Prompt user for author name
        System.out.print("Enter author name: ");
        String authorName = scanner.nextLine();

        // Search for books by author
        List<Book> books = library.searchBooksByAuthor(authorName);

        // Display search results
        if (books.isEmpty()) {
            System.out.println("No books found for author: " + authorName);
        } else {
            System.out.println("Books by author " + authorName + ":");
            for (Book book : books) {
                System.out.println(book.getTitle());
            }
        }
    }


    // Method to add a book to the library
    private static void addBook(Library library, Scanner scanner) {
        System.out.print("Enter book title: ");
        String title = scanner.nextLine();
    
        System.out.print("Enter author name: ");
        String authorName = scanner.nextLine();
    
        System.out.print("Enter ISBN: ");
        String ISBN = scanner.nextLine();
    
        System.out.print("Enter publisher: ");
        String publisher = scanner.nextLine();
    
        System.out.print("Enter number of copies: ");
        int numberOfCopies = scanner.nextInt();
        scanner.nextLine(); // Consume newline character
    
        // Create the author object
        Author author = new Author(authorName, publisher);
    
        // Create the book object
        Book book = new Book(title, author, ISBN, publisher, numberOfCopies);
    
        // Add the book to the library
        library.addBook(book);
    
        System.out.println("Book added successfully!");
    }

    // Method to borrow a book from the library
    private static void borrowBook(Library library, Scanner scanner) {
        System.out.print("Enter book title: ");
        String title = scanner.nextLine();

        System.out.print("Enter patron name: ");
        String patronName = scanner.nextLine();

        System.out.print("Enter number of copies to borrow: ");
        int numberOfCopies = scanner.nextInt();
        scanner.nextLine(); // Consume newline character

        // Search for the book in the library
        List<Book> books = library.searchBooksByTitle(title);

        if (books != null && !books.isEmpty()) {
            // Display search results
            System.out.println("Found " + books.size() + " book(s) with the title '" + title + "':");
            for (int i = 0; i < books.size(); i++) {
                System.out.println((i + 1) + ". " + books.get(i));
            }

            // Prompt user to select a book
            System.out.print("Enter the number of the book you want to borrow: ");
            int bookIndex = scanner.nextInt();
            scanner.nextLine(); // Consume newline character

            if (bookIndex >= 1 && bookIndex <= books.size()) {
                Book selectedBook = books.get(bookIndex - 1);

                // Search for the patron in the library
                Patron patron = library.searchPatronByName(patronName);

                if (patron != null) {
                    // Borrow the book
                    boolean success = library.borrowBook(selectedBook, patron, numberOfCopies);
                    if (success) {
                        System.out.println("Book borrowed successfully!");
                    } else {
                        System.out.println("Failed to borrow the book. Please try again.");
                    }
                } else {
                    System.out.println("Patron not found. Please check the patron name and try again.");
                }
            } else {
                System.out.println("Invalid book number. Please enter a valid number.");
            }
        } else {
            System.out.println("Book not found. Please check the book title and try again.");
    }
}

    private static void returnBook(Library library, Scanner scanner) {
        // Prompt for book title
        System.out.print("Enter the title of the book you want to return: ");
        String title = scanner.nextLine();

        // Prompt for patron name
        System.out.print("Enter the name of the patron who borrowed the book: ");
        String patronName = scanner.nextLine();

        // Prompt for number of copies to return
        System.out.print("Enter the number of copies to return: ");
        int numberOfCopies = scanner.nextInt();
        scanner.nextLine(); // Consume newline character

            // Search for the book in the library
            List<Book> books = library.searchBooksByTitle(title);

            if (books != null && !books.isEmpty()) {
                // Display search results
                System.out.println("Found " + books.size() + " book(s) with the title '" + title + "':");
                for (int i = 0; i < books.size(); i++) {
                    System.out.println((i + 1) + ". " + books.get(i));
                }

                // Prompt user to select a book
                System.out.print("Enter the number of the book you want to return: ");
                int bookIndex = scanner.nextInt();
                scanner.nextLine(); // Consume newline character

                if (bookIndex >= 1 && bookIndex <= books.size()) {
                    Book returnedBook = books.get(bookIndex - 1);

                    // Search for the patron in the library
                    Patron patron = library.searchPatronByName(patronName);

                    if (patron != null) {
                        // Return the book
                        library.returnBook(returnedBook, patron, numberOfCopies);
                        System.out.println("Book returned successfully!");
                    } else {
                        System.out.println("Patron not found. Please check the patron name and try again.");
                    }
                } else {
                    System.out.println("Invalid book number. Please enter a valid number.");
                }
            } else {
                System.out.println("Book not found. Please check the book title and try again.");
            }
        }

    // Method to edit an existing book in the library
    private static void editBook(Library library, Scanner scanner) {
    // Prompt for the title of the book to edit
    System.out.print("Enter the title of the book to edit: ");
    String title = scanner.nextLine();

    // Search for the book in the library
    List<Book> books = library.searchBooksByTitle(title);

    if (books != null && !books.isEmpty()) {
        // Display search results
        System.out.println("Found " + books.size() + " book(s) with the title '" + title + "':");
        for (int i = 0; i < books.size(); i++) {
            System.out.println((i + 1) + ". " + books.get(i));
        }

        // Prompt user to select a book to edit
        System.out.print("Enter the number of the book you want to edit: ");
        int bookIndex = scanner.nextInt();
        scanner.nextLine(); // Consume newline character

        if (bookIndex >= 1 && bookIndex <= books.size()) {
            Book bookToEdit = books.get(bookIndex - 1);

            // Prompt user to enter new information for the book
            System.out.println("Enter new information for the book:");

            System.out.print("New title: ");
            String newTitle = scanner.nextLine();
            bookToEdit.setTitle(newTitle);

            // Update the book in the library
            library.updateBook(bookToEdit);
            System.out.println("Book updated successfully!");
        } else {
            System.out.println("Invalid book number. Please enter a valid number.");
        }
    } else {
        System.out.println("Book not found. Please check the book title and try again.");
    }
    }

    // Method to delete an existing book from the library
    private static void deleteBook(Library library, Scanner scanner) {
    // Prompt for the title of the book to delete
    System.out.print("Enter the title of the book to delete: ");
    String title = scanner.nextLine();

    // Search for the book in the library
    List<Book> books = library.searchBooksByTitle(title);

    if (books != null && !books.isEmpty()) {
        // Display search results
        System.out.println("Found " + books.size() + " book(s) with the title '" + title + "':");
        for (int i = 0; i < books.size(); i++) {
            System.out.println((i + 1) + ". " + books.get(i));
        }

        // Prompt user to select a book to delete
        System.out.print("Enter the number of the book you want to delete: ");
        int bookIndex = scanner.nextInt();
        scanner.nextLine(); // Consume newline character

        if (bookIndex >= 1 && bookIndex <= books.size()) {
            Book bookToDelete = books.get(bookIndex - 1);

            // Delete the book from the library
            library.deleteBook(bookToDelete);
            System.out.println("Book deleted successfully!");
        } else {
            System.out.println("Invalid book number. Please enter a valid number.");
        }
    } else {
        System.out.println("Book not found. Please check the book title and try again.");
    }
    }

    // Method to search for books borrowed by a patron
    private static void searchBooksByPatron(Library library, Scanner scanner) {
        // Prompt for patron name
        System.out.print("Enter the name of the patron: ");
        String patronName = scanner.nextLine();

        // Search for the patron
        Patron patron = library.searchPatronByName(patronName);
        if (patron != null) {
            // Search for books borrowed by the patron
            List<Book> borrowedBooks = library.searchBooksByPatron(patron);
            if (!borrowedBooks.isEmpty()) {
                System.out.println("Books borrowed by " + patronName + ":");
                for (Book book : borrowedBooks) {
                    System.out.println(book);
                }
            } else {
                System.out.println(patronName + " has not borrowed any books.");
            }
        } else {
            System.out.println("Patron not found. Please check the patron name and try again.");
        }
    }
}