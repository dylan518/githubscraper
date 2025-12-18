package com.quangminh.searchviaspecifications.service;

import com.quangminh.searchviaspecifications.builder.SpecificationBuilder;
import com.quangminh.searchviaspecifications.entity.Author;
import com.quangminh.searchviaspecifications.entity.Book;
import com.quangminh.searchviaspecifications.repository.AuthorRepository;
import com.quangminh.searchviaspecifications.repository.BookRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.stereotype.Service;

import java.util.List;

import static com.quangminh.searchviaspecifications.builder.Condition.LogicalOperatorType.AND;
import static com.quangminh.searchviaspecifications.builder.Condition.LogicalOperatorType.END;
import static com.quangminh.searchviaspecifications.builder.Condition.OperationType.*;

@Service
public class BookstoreService {

    private final AuthorRepository authorRepository;
    private final BookRepository bookRepository;

    public BookstoreService(AuthorRepository authorRepository, BookRepository bookRepository) {
        this.authorRepository = authorRepository;
        this.bookRepository = bookRepository;
    }

    public List<Author> fetchAuthors(int age,String genre) {
        SpecificationBuilder<Author> specBuilder = new SpecificationBuilder();

        Specification<Author> specAuthor = specBuilder
                .with("age", String.valueOf(age), GREATER_THAN, AND)
                .with("genre", genre, EQUAL, END)
                .build();

        List<Author> authors = authorRepository.findAll(specAuthor);

        System.out.println(authors);
        return authors;
    }

    public Page<Book> fetchBooksPage(int page, int size) {
        SpecificationBuilder<Book> specBuilder = new SpecificationBuilder();

        Specification<Book> specBook = specBuilder
                .with("price", "60", LESS_THAN, END)
                .build();

        Pageable pageable = PageRequest.of(page, size,
                Sort.by(Sort.Direction.ASC, "title"));

        Page<Book> books = bookRepository.findAll(specBook, pageable);

        System.out.println(books);
        books.forEach(System.out::println);
        return books;
    }
}
