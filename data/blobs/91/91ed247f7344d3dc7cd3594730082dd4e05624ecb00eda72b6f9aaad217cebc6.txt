package com.alas.AlasProject2.controller;


import com.alas.AlasProject2.dto.carts.AddProductsToShoppingCartsRequestDto;
import com.alas.AlasProject2.dto.carts.ShoppingCartsRequestDto;
import com.alas.AlasProject2.dto.carts.ShoppingCartsResponseDto;
import com.alas.AlasProject2.model.ShoppingCarts;
import com.alas.AlasProject2.service.ShoppingCartsService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
@AllArgsConstructor
public class ShoppingController {
    private ShoppingCartsService cartsService;

    @PostMapping("/addProductToCart")
    public ShoppingCarts addProductToCart(@RequestBody AddProductsToShoppingCartsRequestDto dto) {
        return cartsService.addProduct(dto);
    }


    @PostMapping("/createShoppingCart")
    public ShoppingCarts createCart(@RequestBody ShoppingCartsRequestDto cartsRequestDto) {
        return cartsService.createCart(cartsRequestDto);
    }


    @DeleteMapping("/removeProductFromCart")
    public void removeProductFromCart(@RequestParam Integer cartId, @RequestParam List<Integer> productId) {
        cartsService.removeProductFromCart(cartId, productId);
    }


    @GetMapping("/getShoppingCartById")
    public ShoppingCartsResponseDto getShoppingCartById(@RequestParam Integer cartId) {
        return cartsService.getShoppingCartById(cartId);
    }
}
