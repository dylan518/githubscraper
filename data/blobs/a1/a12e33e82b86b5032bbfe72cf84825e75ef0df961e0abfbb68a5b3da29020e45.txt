package com.codefinity.firstrestapibooks.repositroy.impl;

import com.codefinity.firstrestapibooks.model.Book;
import com.codefinity.firstrestapibooks.repositroy.BookRepository;
import org.springframework.stereotype.Repository;


import java.util.*;

@Repository
public class BookRepositoryImpl implements BookRepository {
    private final List<Book> books = Collections.synchronizedList(new ArrayList<>());

    public List<Book> getAllBooks() {
        return books;
    }

    public Book addBook(Book book) {
        String id = UUID.randomUUID().toString();
        book.setId(id);

        books.add(book);
        return book;
    }

    public Book updateBook(String id, Book book) {
        Optional<Book> bookOptional = books.stream()
                .filter(bookStream -> bookStream.getId().equals(id))
                .findFirst();

        Book result = null;
        if(bookOptional.isPresent()) {
            result = bookOptional.get();
            result.setName(book.getName());
            result.setAuthor(book.getAuthor());
            result.setPrice(book.getPrice());
        }

        return result;
    }

    public void deleteBook(String id) {
        Optional<Book> bookOptional = books.stream()
                .filter(bookStream -> bookStream.getId().equals(id))
                .findFirst();

        bookOptional.ifPresent(books::remove);
    }
}
