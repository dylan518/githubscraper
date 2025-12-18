package com.Book.spring_data_jpa_book;

import com.Book.spring_data_jpa_book.model.Book;
import com.Book.spring_data_jpa_book.service.BookService;
import jakarta.persistence.criteria.CriteriaBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/book")
public class BookRestController {

    @Autowired
    private BookService service;

    @GetMapping
    public List<Book> getAllBooks(){
        return service.getAllBooks();
    }

    @GetMapping("/id/{id}")
    public List<Book> getBook(@PathVariable("id") int id) {
        return service.getBook(id);

    }
    @GetMapping("/name/{name}")
    public List<Book> getBookName(@PathVariable("name")String name){
        return service.getBookName(name);
    }

    @GetMapping("/author/{author}")
    public List<Book> getAuthor(@PathVariable("author")String author){
        return service.getAuthor(author);
    }

    @GetMapping("author/{author}/{keyword}")
    public List<Book> searchByAuthorPrice(@PathVariable("keyword") Integer keyword){
        return service.search(keyword);
    }

    @GetMapping("/search")
    public List<Book> searchBooks(
            @RequestParam(value = "author", required = false) String author,
            @RequestParam(value = "name", required = false) String name,
            @RequestParam(value = "price", required = false) Integer price) {
        return service.searchBooks(author, name, price);
    }

    @GetMapping("/search/{author}/{name}/{price}")
    public List<Book> searchBoooks(
            @PathVariable("author") String author,
            @PathVariable("name") String name,
            @PathVariable("price") Integer price) {
        return service.searchBooks(author, name, price);
    }
}
