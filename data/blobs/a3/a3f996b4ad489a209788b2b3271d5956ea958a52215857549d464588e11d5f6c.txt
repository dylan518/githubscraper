package com.epam.rd.autocode.factory.plot.plot;

import com.epam.rd.autocode.factory.plot.Character;
import com.epam.rd.autocode.factory.plot.EpicCrisis;
import com.epam.rd.autocode.factory.plot.Plot;

public class MarvelPlot implements Plot {
    private final Character[] heroes;
    private final EpicCrisis epicCrisis;
    private final Character villain;

    public MarvelPlot(Character[] heroes, EpicCrisis epicCrisis, Character villain) {
        this.heroes = heroes;
        this.epicCrisis = epicCrisis;
        this.villain = villain;
    }

    @Override
    public String asText() {
        StringBuilder builder = new StringBuilder();
        builder.append(epicCrisis.name()).append(actOne());
        for (int i = 0; i < heroes.length; i++) {
            if (heroes.length > 1 && i < heroes.length - 1 && i > 0) {
                builder.append(", the brave ");
            } else if (heroes.length > 1 && i == heroes.length - 1) {
                builder.append(" and the brave ");
            }
            builder.append(heroes[i].name());
            if (heroes.length > 1 && i == heroes.length - 1) {
                builder.append(" are on guard. ");
            } else if (heroes.length == 1) {
                builder.append(" is on guard. ");
            }
        }
        builder.append(actTwo())
                .append(villain.name());
        if (heroes.length == 1) {
            builder.append(actFour());
        } else {
            builder.append(actThree());
        }
        return builder.toString();
    }

    private String actOne() {
        return " threatens the world. But the brave ";
    }

    private String actTwo() {
        return "So, no way that intrigues of ";
    }

    private String actThree() {
        return " will bend the willpower of inflexible heroes.";
    }

    private String actFour() {
        return " will bend the willpower of the inflexible hero.";
    }
}
