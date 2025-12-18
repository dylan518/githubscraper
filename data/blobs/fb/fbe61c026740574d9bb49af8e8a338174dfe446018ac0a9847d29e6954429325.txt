/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.de6;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

/**
 *
 * @author sonki
 */
public class Dictionary {
 
    public ArrayList<Word> getDic() {
        return dic;
    }

    public void setDic(ArrayList<Word> dic) {
        this.dic = dic;
    }
       // Sắp xếp từ điển theo tiếng Anh
    public void sortByEnglish() {
        Collections.sort(dic, Comparator.comparing(Word::getEn, String.CASE_INSENSITIVE_ORDER));
    }
    public String search_bin(String tukhoa ){
        sortByEnglish();
        int l=0;
        int r = dic.size()-1;
        while(l<=r){
            int m= l+(r-l)/2;
            String mid=dic.get(m).getEn();
            if(mid.compareToIgnoreCase(tukhoa)==0){
                return getDic().get(m).getVn();
            }
            if(mid.compareToIgnoreCase(tukhoa)>0){//mid>tukhoa
                r=m-1;
            }else{
                l=m+1;
            }
        }
        return null;
    }
    public void addWord(Word word) { // Generate a new ID
        dic.add(word);
        sortByEnglish(); // Sort the dictionary after adding a new word
    }
     public void saveToFile(String fileName) {
        try (PrintWriter writer = new PrintWriter(new File(fileName))) {
            for (Word word : dic) {
                writer.println(word.getId() + ":" + word.getEn() + ":" + word.getVn());
            }
        } catch (IOException e) {
             e.printStackTrace();
        }
    }
     public void loadFromFile(String fileName) {
        dic.clear();
        try (Scanner scanner = new Scanner(new File(fileName))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(":");
                int id = Integer.parseInt(parts[0]);
                String en = parts[1];
                String vn = parts[2];
                Word word = new Word(id,en, vn);
                dic.add(word);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    private ArrayList<Word> dic= new ArrayList<>();
    
}
