package com.github.devraghav.dp;

import java.util.ArrayList;
import java.util.List;

public class AllConstruct {

    public void getAllCombination(String[] wordBank, String word, String currentWord, List<List<String>> answer, List<String> combination) {
        if (currentWord.equals(word)) {
            answer.add(new ArrayList<>(combination));
            return;
        }
        if (currentWord.length() > word.length() || (!currentWord.equals(word.substring(0, currentWord.length()))))
            return;
        for (int i = 0; i < wordBank.length; i++) {
            combination.add(wordBank[i]);
            getAllCombination(wordBank, word, currentWord + wordBank[i], answer, combination);
            combination.remove(wordBank[i]);
        }
    }

    public List<List<String>> getAllCombination(String[] wordBank, String word) {
        List<List<String>> ans = new ArrayList<>();
        if (word.length() == 0) return ans;
        getAllCombination(wordBank, word, "", ans, new ArrayList<>());
        return ans;
    }

    public static void main(String[] args) {
        AllConstruct allConstruct = new AllConstruct();
        System.out.println(allConstruct.getAllCombination(new String[]{"ab", "abc", "ef", "cd", "def", "abc"}, "abcdef"));
        System.out.println(allConstruct.getAllCombination(new String[]{"a", "p", "ent", "enter", "ot", "o", "t"}, "enterapotentpot"));
        System.out.println(allConstruct.getAllCombination(new String[]{"purp", "p", "le", "ur", "purpl"}, "purple"));
        System.out.println(allConstruct.getAllCombination(new String[]{"ab", "abc", "cd", "def", "abcd", "ef", "c"}, "abcdef"));
        System.out.println(allConstruct.getAllCombination(new String[]{"bo", "rd", "ate", "t", "ska", "sk", "boar"}, "skateboard"));
    }
}
