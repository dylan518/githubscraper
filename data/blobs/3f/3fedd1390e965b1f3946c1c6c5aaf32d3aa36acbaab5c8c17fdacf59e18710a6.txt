package com.example.month9onlineshop.services;

import com.example.month9onlineshop.dto.ItemDTO;
import com.example.month9onlineshop.repositories.ItemRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;


@Service
@RequiredArgsConstructor
public class ItemService {
    final private ItemRepository itemRepository;

    public Page<ItemDTO> searchBy(String name, int page) {
        Pageable pageable = PageRequest.of(page, 6);
        return itemRepository.findAllByName(name, pageable).map(ItemDTO::from);
    }



//    public Page<ItemDTO> searchByNameOrDescription(String name, int page) {
//        Pageable pageable = PageRequest.of(page, 2);
//        return itemRepository.searchByNameOrDescription(name, pageable).map(ItemDTO::from);
//    }

//    public Page<Item> searchAndShowItemsByPrice(Long price,Integer pageNum) {
//        int pageSize = 5;
//        Pageable pageable = PageRequest.of(pageNum - 1, pageSize);
//        return itemRepository.findAllByPrice(price, pageable);
//    }

}
