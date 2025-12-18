package com.alvincabayan.lottosimulation.services;

import com.alvincabayan.lottosimulation.models.Ticket;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.IntStream;

@Service
public class TicketService {
    @Autowired NumberRandomizerService numberRandomizerService;
    private static final Integer LOTTO_SIZE = 6;

    public List<Ticket> buyMultipleTickets(Integer quantity) {
        List<Ticket> tickets = new ArrayList<>();
        while(tickets.size() < quantity) {
            tickets.add(getTicket());
        }
        return tickets;
    }

    public Ticket getTicket() {
        return Ticket.builder().lottoNumbers(generateLotto()).powerball(generatePowerball()).build();
    }

    public Set<Integer> generateLotto() {
        Set<Integer> lotto = new HashSet<>();
        while (lotto.size() < LOTTO_SIZE) {
            lotto.add(numberRandomizerService.randomizer(40));
        }
        return lotto;
    }

    public Integer generatePowerball() {
        Integer powerball = numberRandomizerService.randomizer(10);
        return powerball;
    }
}
