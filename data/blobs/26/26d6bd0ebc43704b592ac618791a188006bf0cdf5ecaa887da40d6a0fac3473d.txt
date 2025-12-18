package com.codexbox.springboot.app.Veeru.fileoperations;

import java.io.*;
import java.util.Enumeration;

public class InputOutputStreamExample {

   public void fileInputOutputperations() throws IOException {
      Reader reader = null;
      Writer writer = new FileWriter("cbz.txt");
       try {
            reader = new FileReader("abc.txt");
          int ch =  reader.read();
          while (ch != -1) {
              writer.write((char)ch);
              ch = reader.read();
          }

       } catch (FileNotFoundException e) {
           System.out.println("File Not found exception occured please check if your file is present");
       } catch (IOException e) {
           throw new RuntimeException(e);
       } finally {
           if (null != reader && null != writer) {
               reader.close();
               writer.close();
           }
       }
   }

   void testInterviewQuestions() {
       short x = 10;
       x = (short) (x * 5);
       System.out.print(x);
   }
}
