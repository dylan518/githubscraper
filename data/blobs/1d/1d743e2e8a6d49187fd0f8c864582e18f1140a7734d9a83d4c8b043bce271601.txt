package lessons.lesson6.Exercises;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileEncryption extends ReadFileHandler {

    private String destinationFilePath;

    public FileEncryption(String filePath, String destinationFilePath) {
        super(filePath);
        this.destinationFilePath = destinationFilePath;
    }

    public void encryptAndWriteToFile(int key) throws FileNotFoundException, IOException{

        
        try (BufferedReader reader = new BufferedReader(new FileReader(super.getFilePath()));
             BufferedWriter writer = new BufferedWriter(new FileWriter(this.destinationFilePath))) {

            int c;
            while ((c = reader.read()) != -1) {
                // Shift characters by the encryption key
                char encryptedChar = (char) (c + key);

                // Write the encrypted character to the output file
                writer.write(encryptedChar);
            }
        }
        
    }
    
}
