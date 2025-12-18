/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Frunze
 */
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
//import java.time.LocalTime;
import java.util.Scanner;



public class Main {
    
    //private long[] a;
    //LocalTime[][] a;
    int N;
    private int elems;
    public Main(int N){    //конструктор класса
      //  a = new LocalTime[N][2];
        this.N = N;
        this.elems = N;
    }
    public void setN(int N) {
       this.N = N;
   }

   public int getN() {
       return N;
   }
   //LocalTime[][] a(){return a;}
   //LocalTime getA(int i, int j){return a[i][j];}
    public void bubbleSorter(){     //МЕТОД ПУЗЫРЬКОВОЙ СОРТИРОВКИ
        for (int out = elems - 1; out >= 1; out--){  //Внешний цикл
            
            for (int in = 0; in < out; in++){       //Внутренний цикл
                                
                //if(a[in][0].compareTo(a[in + 1][0]) > 0)               //Если порядок элементов нарушен
                    //toSwap(in, in + 1);             //вызвать метод, меняющий местами
            }
        }
    }
   /* private void toSwap(int first, int second){ //метод меняет местами пару чисел массива
        LocalTime[] dummy = new LocalTime[2];
        dummy[0] = a[first][0];
        dummy[1] = a[first][1];
        a[first][0] = a[second][0];       //на место первого ставим второй элемент
        a[first][1] = a[second][1];
        a[second][0] = dummy[0];         //вместо второго элемента пишем первый из временной памяти
        a[second][1] = dummy[1];         //вместо второго элемента пишем первый из временной памяти
    }*/
    
    public void into(Scanner sc){
      String Line;
      String[] partsSp;
      String[] partsDl;
      String[] partsDl_2;    
      sc.nextLine();
      for(int i = 0; i < N; i++){
            while (sc.hasNextLine()) {
                Line = sc.nextLine();
                partsSp = Line.split(" ");
                
                partsDl = partsSp[0].split(":");
               // a[i][0] = LocalTime.of(Integer.parseInt(partsDl[0]),Integer.parseInt(partsDl[1]));
                
                partsDl_2 = partsSp[1].split(":");
                //a[i][1] = LocalTime.of(Integer.parseInt(partsDl_2[0]),Integer.parseInt(partsDl_2[1]));
                break;
        }
    }
    }
    
    public void printer(){
        for(int i = 0; i < N; i++){
        for (int j = 0; j < 2; j++){
            //System.out.print(a[i][j] + " ");
        }
        System.out.println();
    }
    }
    public int compare(int i, int j/*, LocalTime b*/){
      
      //  if(this.a[i][j].compareTo(b) > 0)
            return 1;
        //else if(this.a[i][j].compareTo(b) < 0)
        /*return -1;
        else
            return 0;*/
    }

    public static void main(String[] args) throws FileNotFoundException, IOException{
    String path = "INPUT.TXT";
    File file = new File(path);
    Scanner sc = new Scanner(file);    
    int M = sc.nextInt();
    Main array = new Main(M);
    M = array.getN();

    array.into(sc);
    array.printer();
    array.bubbleSorter(); 
    System.out.println("");
    array.printer();
    int[] ch = new int[M];
    
                System.out.println("");    
    int count = 0;
    for (int i = 0; i < M; i++){
        for (int j = 0; j < M; j++){
        if (i == j) continue;
        //if (i == M-1) break;
        /*if(((matrixA[i][0].compareTo(matrixA[j][0]) <= 0) && 
                (matrixA[j][1].compareTo(matrixA[i][1]) <= 0) &&
                (matrixA[j][0].compareTo(matrixA[i][1]) <= 0)) ||
                ((matrixA[i][0].compareTo(matrixA[j][0]) <= 0) && 
                (matrixA[i][1].compareTo(matrixA[j][1]) <= 0) && 
                (matrixA[j][0].compareTo(matrixA[i][1]) <= 0)))*/
        /*if(array.compare(i, 1, array.getA(j, 0)) >= 0 &&
                array.compare(i, 0, array.getA(j, 0)) <= 0)
        {
            System.out.println(array.getA(i, 0) + "И" + array.getA(i, 1) + "____" + array.getA(j, 0) + "И" + array.getA(j, 1));;
            ch[i]++;
            ch[j]++;
                    
        }*/
        
        }
    }
    
    for(int i = 0; i < M; i++) System.out.println(i + ": " + ch[i]);
    int max = ch[0];
    for(int i = 0; i < M; i++) if (max < ch[i]) max = ch[i];;
    System.out.println(max);
    
    String str = Integer.toString(max);
    String fileName = "OUTPUT.TXT";
    BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, true));
    //writer.append(' ');
    writer.append(str);
     
    writer.close();
  }
}