package com.feidian.dome1;

import javax.xml.transform.Source;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;

public class ChronoUnitDome1 {
    public static void main(String[] args) {
        LocalDateTime ldt1=LocalDateTime.of(2025,1,1,0,0,0);
        LocalDateTime ldt2=LocalDateTime.now();
        System.out.println(ChronoUnit.WEEKS.between(ldt2,ldt1));

    }
}
