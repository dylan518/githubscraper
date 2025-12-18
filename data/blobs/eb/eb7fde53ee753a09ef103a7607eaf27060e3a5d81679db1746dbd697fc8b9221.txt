package library.library.integration;


import library.library.client.Book;
import library.library.config.ApplicationProperties;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
public class BookClient {
    @Autowired
    private ApplicationProperties applicationProperties;

    private RestTemplate restTemplate = new RestTemplate();

    public Book getBook(String isbn) {
        Book book = new Book();
        try{
            book = restTemplate.getForObject("http://localhost:8080/books" + "{isbn}", Book.class, isbn);
        } catch (Exception e){
            System.out.println("Can't find a book: "+ e.getMessage());
        }
        return book;
    }
}

