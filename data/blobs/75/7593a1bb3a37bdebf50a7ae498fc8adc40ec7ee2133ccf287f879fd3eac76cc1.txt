package Home_Task_4;

import Practice_4.Coffee;

/**Необходимо взять код из первого дз и переработать его с учетом обобщений
 * т.е избавиться от классов под каждый тип продукта, заменив единым классом - торговым автоматом
 */
public class HomeTaskForth {
    public static void main(String[] args) {
        HotBeverage coffeeLatte = new HotBeverage();
        coffeeLatte.setType("Coffee");
        coffeeLatte.setName("Latte");
        coffeeLatte.setPrice(380.50);
        coffeeLatte.setVolume(300);
        coffeeLatte.setTemperature(90);

        HotBeverage coffeeAmericano = new HotBeverage();
        coffeeAmericano.setType("Coffee");
        coffeeAmericano.setName("Americano");
        coffeeAmericano.setPrice(300.50);
        coffeeAmericano.setVolume(300);
        coffeeAmericano.setTemperature(95);

        HotBeverage coffeeCappuchino = new HotBeverage();
        coffeeCappuchino.setType("Coffee");
        coffeeCappuchino.setName("Cappuchino");
        coffeeCappuchino.setPrice(355.00);
        coffeeCappuchino.setVolume(300);
        coffeeCappuchino.setTemperature(99);

        VendingMachine <Beverage> coffee = new VendingMachine<>();
        coffee.addProducts(coffeeLatte);
        coffee.addProducts(coffeeAmericano);
        coffee.addProducts(coffeeCappuchino);
        System.out.println(coffee.getProducts());
        System.out.println(coffee.getBeverage(2));
        System.out.println();

        System.out.println(coffee.remove(coffeeAmericano));
        System.out.println(coffee.remove(coffeeLatte));
    }
}
