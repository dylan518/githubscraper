package org.baraniecka.week3.exercise_4;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.baraniecka.week3.exercise_4_sales_by_match.SalesByMatch;
import org.junit.jupiter.api.Test;

import java.util.List;

public class SalesByMatchTest {

    @Test
    void count_socks_pairs() {
        //given
        int socks = 5;
        List<Integer> colors = List.of(1, 2, 1, 3, 2);

        //then
        assertEquals(2, SalesByMatch.sockMerchant(socks, colors));
    }

    @Test
    void count_socks_pairs_WHERE_same_color_AND_even_pairs(){
        //given
        int socks = 10;
        List<Integer> colors = List.of(1, 1, 1, 1, 1, 1, 1, 1, 1, 1);

        //then
        assertEquals(5, SalesByMatch.sockMerchant(socks, colors));

    }

    @Test
    void count_socks_pairs_WHERE_same_color_AND_odd_pairs(){
        int socks = 9;
        List<Integer> colors = List.of(1, 1, 1, 1, 1, 1, 1, 1, 1 );

        //then
        assertEquals(4, SalesByMatch.sockMerchant(socks, colors));
    }
}
