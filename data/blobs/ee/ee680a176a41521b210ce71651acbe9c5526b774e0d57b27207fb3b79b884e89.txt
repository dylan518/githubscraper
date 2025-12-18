package org.example.Functional_java.Collections.Pick_an_Element;

import java.util.List;
import java.util.Objects;

public class PickAnElement {
    public static void pickName(
            final List<String> names, final String startingLetter) {
        String foundName = null;
        for (String name : names) {
            if (name.startsWith(startingLetter)) {
                foundName = name;
                break;
            }
        }

        System.out.printf("A name starting with %s: ", startingLetter);
        System.out.println(Objects.requireNonNullElse(foundName, "No name found"));
    }

    public static void main(String[] args) {


    }
}
