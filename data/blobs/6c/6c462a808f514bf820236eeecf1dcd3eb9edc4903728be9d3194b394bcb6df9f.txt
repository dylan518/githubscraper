package edu.thiago.functional_interface;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

public class PredicateExemplo {
    public static void main(String[] args) {
        // Criamos uma lista de strings por exemplo
        List<String> palavras = Arrays.asList("Java", "C#", "Python", "PHP", "C++", "JavaScript");

        // Usamos Predicate com expressao lambda para filtrar palavras com mais de 5 letras
        Predicate<String> maisDeCincoLetras = p -> p.length() > 5;

        // Usar Stream para filtrar as palavras com mais de 5 caracteres e impimi-las
        palavras.stream().filter(maisDeCincoLetras).forEach(System.out::println);

    }
}
