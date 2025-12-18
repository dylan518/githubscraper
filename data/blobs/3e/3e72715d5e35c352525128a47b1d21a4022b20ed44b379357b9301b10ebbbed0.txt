package com.example.demo.implem;

import com.example.demo.jpa.BookOrder;
import com.example.demo.repository.BookOrderRepository;
import com.example.demo.service.BookOrderService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.Date;

@Service
public class BookOrderServiceImplem implements BookOrderService {

    @Autowired
    private BookOrderRepository bookOrderRepository;

    @Override
    public Collection<BookOrder> findAllObjects() {
        return bookOrderRepository.findAll();
    }

    @Override
    public BookOrder getObjectById(Integer id) {
        return bookOrderRepository.getOne(id);
    }

    @Override
    public boolean existsObjectById(Integer id) {
        return bookOrderRepository.existsById(id);
    }

    @Override
    public BookOrder saveObject(BookOrder bookOrder) {
        return  bookOrderRepository.save(bookOrder);
    }

    @Override
    public void deleteObjectById(Integer id) {
        bookOrderRepository.deleteById(id);
    }

   /* @Override
    public Collection<BookOrder> getObjectByDat(Date orderdat) {
        return bookOrderRepository.getObjectByDat(orderdat);
    }
*/

}
