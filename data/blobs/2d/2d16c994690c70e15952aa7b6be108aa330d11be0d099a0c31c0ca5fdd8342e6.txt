import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
    public class Driver {
        public static void main(String[] args) {
            String line;
            String splitBy = ",";
            try {
//parsing a CSV file into BufferedReader class constructor
                BufferedReader br = new BufferedReader(new FileReader("src/dutyroster.csv"));
                while ((line = br.readLine()) != null)   //returns a Boolean value
                {
                    String[] employee = line.split(splitBy);    // use comma as separator
                    System.out.println("Employee [First Name=" + employee[0] +
                                       ", Date of Duty=" + employee[1]
                                     + ", Designation=" +employee[2]);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
