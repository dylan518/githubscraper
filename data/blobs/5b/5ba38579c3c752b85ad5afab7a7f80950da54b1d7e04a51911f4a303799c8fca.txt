// ショッピングカートのシステム

package main.java.me.river750.shopping_cart;

public class Main {
    public static void main(String[] args) {
        // 商品を作成
        Item item1 = new Item("りんご", 100, 5);
        Item item2 = new Item("バナナ", 150, 3);
        Item item3 = new Item("オレンジ", 120, 2);

        // ショッピングカートを作成
        ShoppingCart cart = new ShoppingCart();

        // 商品をカートに追加
        cart.addItem(item1);
        cart.addItem(item2);
        cart.addItem(item2);
        cart.addItem(item3);

        // カートの内容を表示
        cart.displayCart();
    }
}