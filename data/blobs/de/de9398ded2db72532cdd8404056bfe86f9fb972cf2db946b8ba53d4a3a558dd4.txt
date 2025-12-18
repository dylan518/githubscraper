package com.linkshortener;

import java.util.HashMap;
import java.util.Map;

public class LinkShortener {
    private Map<String, String> urlMap;
    private Map<String, String> shortToLongMap;
    private static final String BASE_URL = "http://short.ly/";
    private static final String CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    private static final int SHORT_URL_LENGTH = 6;

    public LinkShortener() {
        urlMap = new HashMap<>();
        shortToLongMap = new HashMap<>();
    }

    public String shortenURL(String longURL) {
        if (urlMap.containsKey(longURL)) {
            return urlMap.get(longURL);
        }

        String shortURL;
        do {
            shortURL = generateShortURL();
        } while (shortToLongMap.containsKey(shortURL));

        urlMap.put(longURL, shortURL);
        shortToLongMap.put(shortURL, longURL);
        return shortURL;
    }

    public String expandURL(String shortURL) {
        return shortToLongMap.getOrDefault(shortURL, "URL not found");
    }

    private String generateShortURL() {
        StringBuilder shortURL = new StringBuilder(BASE_URL);
        for (int i = 0; i < SHORT_URL_LENGTH; i++) {
            int index = (int) (Math.random() * CHARACTERS.length());
            shortURL.append(CHARACTERS.charAt(index));
        }
        return shortURL.toString();
    }
}
