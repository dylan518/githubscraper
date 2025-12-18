import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.IOException;

public class FileInputOutput {

    public String makeFile(String a){
        try{
            BufferedWriter writer = new BufferedWriter(new FileWriter("E:\\Pro Sigmaka Mandiri - Pelatihan\\Java Fundamental\\Lesson 4 Java Array dan Output\\output.txt"));
            writer.write(a);
            writer.close();
        } catch (IOException e){
            e.printStackTrace();
        }
        return a;
    }

    public void readFile(){
        try{
            BufferedReader reader = new BufferedReader(new FileReader("E:\\Pro Sigmaka Mandiri - Pelatihan\\Java Fundamental\\Lesson 4 Java Array dan Output\\output.txt"));
            String line;
            while((line = reader.readLine()) !=null){
                System.out.println(line);
            }
            reader.close();
        } catch(IOException e){
            e.printStackTrace();
        }
    }

}
