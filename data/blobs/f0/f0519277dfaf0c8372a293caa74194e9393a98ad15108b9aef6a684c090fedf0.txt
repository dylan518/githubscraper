package com.fastfoward.cardsapi.repository.impl;
import com.fastfoward.cardsapi.model.Card;
import com.fastfoward.cardsapi.repository.CardRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Repository
public class CardRepositoryImpl implements CardRepository {

    private final List<Card> cards;

    public CardRepositoryImpl() {

        var card = new Card();

        cards = new ArrayList<>();

        card.setId(1);
        card.setName("Iron Man");
        card.setDescription("Tony Stark");
        card.setImageUrl("ironManImageUrl");
        card.setStrength(5);
        card.setSpeed(6);
        card.setGear(5);
        card.setIntellect(5);
        card.setSkill(5);
        card.setCreatedAt(LocalDateTime.now());
        card.setUpdatedAt(LocalDateTime.now());

        cards.add(card);
    }


    @Override
    public Optional<Card> findById(int id) {
        return cards.stream().filter(card -> card.getId() == id).findFirst();
    }
}
