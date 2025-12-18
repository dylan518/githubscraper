package com.charter.rewards.web.controllers;

import com.charter.rewards.service.PurchaseOrderService;
import com.charter.rewards.service.domain.PurchaseOrderHeader;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequestMapping("/api/v1/po/")
@RestController
public class PurchaseOrderController {
    private final PurchaseOrderService purchaseOrderService;

    public PurchaseOrderController(PurchaseOrderService purchaseOrderService) {
        this.purchaseOrderService = purchaseOrderService;
    }

    @GetMapping("transactionid/{transactionId}")
    public PurchaseOrderHeader
      getRewardTransactionById(@PathVariable("transactionId") long transactionId){
        return purchaseOrderService.getPoById(transactionId);
    }

    @GetMapping("getallpos")
    public List<PurchaseOrderHeader>
    getAllPurchaseOrders(){
        return purchaseOrderService.getAllPoHeaders();
    }

    @GetMapping("getallposbycustomer/customerid/{customerid}")
    public List<PurchaseOrderHeader>
    getAllPurchaseOrders(@PathVariable("customerid") long customerId){
        return purchaseOrderService.getAllPoHeadersByCustomer(customerId);
    }
}
