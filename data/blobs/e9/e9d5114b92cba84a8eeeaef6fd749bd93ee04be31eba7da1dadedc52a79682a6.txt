/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package View;

import Service.TodolistService;
import Util.InputUtil;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;
import static todolist.Todolist.input;

/**
 *
 * @author WIN 10
 */
public class ViewTodolist {
    private TodolistService todoListService;
    private Locale local = new Locale("id","ID");
    private SimpleDateFormat simpleDateFormat = new SimpleDateFormat("dd-MM-YYYY HH:mm:ss");

    public ViewTodolist(TodolistService todoListService) {
        this.todoListService = todoListService;
    }
    
    public void lihat(){
        boolean kondisi = true;
        while(kondisi){
            todoListService.lihat();
            System.out.println("Menu");
            System.out.println("1. Tambah");
            System.out.println("2. Hapus");
            System.out.println("3. Keluar");
            
            String inputdata = InputUtil.input("Pilih aksi ");
            switch(inputdata.toLowerCase()){
                case "1","tambah"-> tambah();
                case "2","hapus"-> hapus();
                case "3","keluar"-> kondisi=false;
                default -> System.err.println("Maaf pilihan yang anda masukan tidak ada dimenu");
            }
            
        }
    }
    public void tambah(){
        DateTimeFormatter format = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss",Locale.forLanguageTag("id-ID"));
        String todo;
        String input;
        System.out.println("Menambah todolist");
        todo = InputUtil.input("todo(x jika batal)");
        
        if(todo.equalsIgnoreCase("x")||todo.equalsIgnoreCase("batal")){
            return;
        }else{
            System.out.println("Tanggal dan waktu : ");
            input = InputUtil.input("todo (x jika batal : )");
            if(todo.equalsIgnoreCase("x")||todo.equalsIgnoreCase("batal")){
                return;
            }
            try {
                LocalDateTime dateTime = LocalDateTime.parse(input, format);
                todoListService.tambah(todo, dateTime);
                System.out.println("Berhasil ditambahkan");
            } catch (Exception ex) {
                System.out.println("Invalid date format");
            }
            
        }
    }
    public void hapus(){
        System.out.println("View Hapus todolist");
        String nmr = InputUtil.input("nomor yang dihapus(x jika batal)");
        if(nmr.equals("x")){
            
        }else{
            todoListService.hapus(Integer.valueOf(nmr));
        }
    }
}
