package com.aap.splitbill.strategy;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import static org.mockito.Mockito.*;

class BankServiceTest {
    @Mock
    StrategyFactory strategyFactory;
    @InjectMocks
    BankService bankService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void testGetUrlBank() {
        when(strategyFactory.findStrategy(any())).thenReturn(new Nubank());

        String result = bankService.getUrlBank(StrategyNameEnum.NUBANK);
        Assertions.assertEquals("https://nubank.com.br/pagar/customer/", result);
    }
}
