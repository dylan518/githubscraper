package com.shoppingprod.shoppingprod.services;


import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.shoppingprod.shoppingprod.entities.CartStatus;
import com.shoppingprod.shoppingprod.entities.cart;
import com.shoppingprod.shoppingprod.repository.CartItemsRepository;


@Service
public class cartServiceImpl implements cartService {
	
	@Autowired
	CartItemsRepository cartRepository;
	

	public  void deleteproduct(int userId,long parseLong){
      cart item=cartRepository.findById(parseLong,userId);
      cartRepository.delete(item);
 
	}
	
	public cart updateproducts(final cart product,int userId){
		cart item=cartRepository.findById(product.getId(),userId);
	    item.setQuantity(product.getQuantity());
	    return cartRepository.save(item);
	        
	}
	
	public void checkout(cart Item,int userId){
		    
		    cart cartItem=cartRepository.findById(Item.getId(),userId);
		    cartItem.setStatus(CartStatus.CHECKED_OUT.toString());
		    cartRepository.save(cartItem);
		}

	
//    @Override
//	public List<cart> updateStatus(long id) {
//		List<cart> cartItems = new ArrayList<>();
//		cartItems = cartRepository.updateStatus(id);
//		for(cart i:cartItems) {
//			i.setStatus(CartStatus.CHECKED_OUT.toString());
//		}
//		return cartRepository.saveAll(cartItems);
//	}

//	@Override
//	public List<cart> getCartByUserId(int userid) {
//		return cartRepository.getCartByUserId(userid);
//	}

}
