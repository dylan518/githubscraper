package lesson_12.game;

import lesson_12.game.entities.DeckOfCardsImpl;
import lesson_12.game.entities.PlayerImpl;
import lesson_12.game.interfaces.DeckOfCards;
import lesson_12.game.interfaces.Player;

public class Main {
    public static void main(String[] args) {
        DeckOfCards deckOfCards = new DeckOfCardsImpl();
        deckOfCards.getRandomCard().printCard();

        Player player1 = new PlayerImpl();
        player1.takeCard(deckOfCards.getRandomCard());
        player1.takeCard(deckOfCards.getRandomCard());
        player1.takeCard(deckOfCards.getRandomCard());

        System.out.println(player1.countValuesAllCardsOnHand());
        player1.showCardsOnHand();


    }
}
