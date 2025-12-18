package com.fcs.bookstore.book;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import com.fcs.bookstore.author.Author;
import com.fcs.bookstore.author.AuthorRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.Optional;

class BookServiceTest {

    private BookRepository repository;
    private AuthorRepository authorRepository;
    private BookService bookService;

    private Book book;
    private Author author;

    @BeforeEach
    void setUp() {
        repository = mock(BookRepository.class);
        authorRepository = mock(AuthorRepository.class);
        bookService = new BookService(repository, authorRepository);

        author = new Author(1L, "Test Author", "test@test.com", "Test Bio");
        book = new Book(1L, "Test Book", author, "1234567890", 2021, 100, null);
    }

    @Test
    void shouldCreateBookSuccessfully() {
        when(authorRepository.existsById(author.getId())).thenReturn(true);
        when(repository.save(book)).thenReturn(book);

        var result = bookService.createBook(book);

        assertNotNull(result);
        assertEquals(book.getId(), result.getId());
    }

    @Test
    void shouldThrowWhenCreateBookAuthorNotFound() {
        when(authorRepository.existsById(author.getId())).thenReturn(false);

        assertThrows(IllegalArgumentException.class, () -> bookService.createBook(book));
    }

    @Test
    void shouldGetBookSuccessfully() {
        when(repository.findById(book.getId())).thenReturn(Optional.of(book));

        var result = bookService.getBook(book.getId());

        assertNotNull(result);
        assertEquals(book.getId(), result.getId());
    }

    @Test
    void shouldThrowWhenGetBookNotFound() {
        when(repository.findById(1L)).thenReturn(Optional.empty());

        assertThrows(IllegalArgumentException.class, () -> bookService.getBook(1L));
    }
}
