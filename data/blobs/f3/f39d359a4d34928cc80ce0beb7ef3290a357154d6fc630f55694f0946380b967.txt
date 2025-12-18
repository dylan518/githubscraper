package core_java_SerializationDemo;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

// don't know about the order of the class into convert of file

class Elephant implements Serializable{
	String name="----Elephant----";
	int age=40;
	
}

class Hourse implements Serializable{
	String name="----Hourse----";
	int age =20;
}

class Money implements Serializable{
	String name="----Monkey----";
	int age=10;
}


public class MultiSerialEx2 {
	public static void main(String[] args) throws Exception {
		Elephant elephant=new Elephant();
		Hourse hourse= new Hourse();
		Money monkey= new Money();
		
		FileOutputStream fos =new FileOutputStream("Animals.txt");
		ObjectOutputStream oos=new ObjectOutputStream(fos);
		oos.writeObject(elephant);
		oos.writeObject(hourse);
		oos.writeObject(monkey);
		
		FileInputStream fis=new FileInputStream("Animals.txt");
		ObjectInputStream ois=new ObjectInputStream(fis);
		Object obj=ois.readObject();
		
		if(obj instanceof Elephant) {
			Elephant newelephant=(Elephant) obj;
			System.out.println(newelephant.name);
			System.out.println(newelephant.age);
			
		}
	
		
		  else if(obj instanceof Hourse) 
		  {
			  Hourse newhourse=(Hourse) obj;
			  System.out.println(newhourse.name); 
			  System.out.println(newhourse.age);
		  
		  }
		 
		else if(obj instanceof Money) {
			Money newmoney=(Money) obj;
			System.out.println(newmoney.name);
			System.out.println(newmoney.age);
			
		}
		
		
	}

}
