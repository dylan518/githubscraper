package com.academy.kopats.lesson8;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Task3 {
    public static void main(String[] args) {
        printStartEndLetter("Listen to the news from today and read the text at the same time. Listen to the news from today without reading the text.");
        System.out.println(newText(Text.TEXT));
    }
    public static String newText(String s) {
        StringBuilder sb = new StringBuilder(s);
        Pattern pattern = Pattern.compile("\\b(?i:[A-z])\\S{3,}\\b");
        Matcher matcher = pattern.matcher(sb);
        while (matcher.find()) {
            sb.setCharAt(matcher.start(0)+3, '#');
            if (matcher.group().length() >= 7) {
                sb.setCharAt(matcher.start(0)+6,'#');
            }
        }
        return sb.toString();
    }

    public static void printStartEndLetter(String s){
        Pattern pattern = Pattern.compile("\\b(?i:[bcdfghjklmnpqrstvwxz])\\S*(?i:[aeiouy])\\b");
        Matcher matcher = pattern.matcher(s);
        while (matcher.find()){
            System.out.println(matcher.group());
        }
    }

}

