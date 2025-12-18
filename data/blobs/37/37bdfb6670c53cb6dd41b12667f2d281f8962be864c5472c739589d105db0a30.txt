package effective_java.L_serialization_test.examples;

import effective_java.L_serialization.example.SerializableClass;
import org.junit.Test;

import java.io.*;

public class TestSerializableClass {

    public static final String FILE = "src/effective_java/L_serialization_test/examples/file.txt";

    @Test
    public void test() {

        SerializableClass object = new SerializableClass(1, "Implement Serializable with great caution");
        doSerialization(object, FILE);
        try {
            SerializableClass deSerObject = doDeserialization(FILE);
            System.out.println("Object has been deserialized ");
            System.out.println("a = " + deSerObject.a);
            System.out.println("b = " + deSerObject.b);
        } catch (IOException ex) {
            System.out.println("IOException is caught");
        } catch (ClassNotFoundException ex) {
            System.out.println("ClassNotFoundException is caught");
        }

        System.out.println("Test finished");

    }

    private SerializableClass doDeserialization(String filename) throws IOException, ClassNotFoundException {
        // Reading the object from a file
        FileInputStream file = new FileInputStream(filename);
        ObjectInputStream in = new ObjectInputStream(file);
        SerializableClass object1 = (SerializableClass) in.readObject();  // Method for deserialization of object
        in.close();
        file.close();
        return object1;
    }

    private void doSerialization(SerializableClass object, String filename) {
        try {
            //Saving of object in a file
            FileOutputStream file = new FileOutputStream(filename);
            ObjectOutputStream out = new ObjectOutputStream(file);
            // Method for serialization of object
            out.writeObject(object);
            out.close();
            file.close();
            System.out.println("Object has been serialized");
        } catch (IOException ex) {
            System.out.println("IOException is caught");
        }
    }


}
