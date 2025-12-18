package java_0718_ProductMgmt.src.com.example;

import java.util.List;

public class Calc {
    private List<Product> list;

    public Calc(List<Product> list) {
        this.list = list;
    }

    public void calc() {
        for(Product p : this.list){ // 그냥 list와 this.list의 차이
            int sellMoney = p.getQuantity() * p.getSellPrice();
            int buyMoney = p.getQuantity() * p.getBuyPrice();
            int benefit = sellMoney - (buyMoney + p.getTransport());
            double rate = (double) benefit / buyMoney * 100;
            p.setBenefit(benefit);
            p.setRate(rate);
        }
    }
}
