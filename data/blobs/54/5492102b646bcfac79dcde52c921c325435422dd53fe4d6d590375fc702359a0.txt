package org.example.third.simple;

import org.example.third.Street;
import org.example.third.StreetImpl;

public class SimpleCrossroad {

    private Street first;
    private StreetImpl second;

    public SimpleCrossroad(Street first, StreetImpl second) {
        this.first = first;
        this.second = second;
    }

    public String getNames() {
        return "First street name '" + first.getName() + "', second street name: '" + second.getName() + "'";
    }
}
