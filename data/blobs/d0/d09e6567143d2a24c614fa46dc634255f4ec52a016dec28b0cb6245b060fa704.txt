package InputOutputSample;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class InputTest {
    public static void main(String[] args) throws IOException  {
        //we can either use absolute path OR relative path of where this program is running
        //in this case we are running from the  java-practice folder
        //so we must access the inner folder by doing the following
        FileInputStream stream = null;
        try {
            stream = new FileInputStream("./com/test/data/text.txt");
            System.out.println("hello");
            //it is important to close the stream because others can't access it 
            
        } catch ( FileNotFoundException e) {
            throw new RuntimeException(e);
        } finally {
            //finally would always run either sucessfully or with error
            if(stream != null){
                stream.close();
            }
           
        }
        
    }
}
