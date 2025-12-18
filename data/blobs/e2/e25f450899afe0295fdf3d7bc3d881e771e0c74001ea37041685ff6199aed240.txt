package filehandling;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

public class Main {
	public static void main(String[] args) {
//		try {
//			FileReader file = new FileReader("E:\\input.txt");
//			int letters = file.read();
//			while (file.ready()) {
//				System.out.print((char) letters);
//				letters = file.read();
//			}
//			System.out.print((char) letters);
//			file.close();
//		} catch (IOException e) {
//			System.out.println(e.getMessage());
//		}
//		try {
//			BufferedReader bufferReader = new BufferedReader(new FileReader("E:\\input.txt"));
//			System.out.println(bufferReader.readLine());
//			bufferReader.close();
//		} catch (Exception e) {
//
//		}
//		/* OutputStreamWriter */
//		try(OutputStreamWriter os=new OutputStreamWriter(System.out)) {
//			os.write("Hello World");
//			os.write(10);
//		} catch (Exception e) {
//
//		}
//		try {
//			BufferedWriter writer = new BufferedWriter(new FileWriter("E:\\input.txt", true));
//			writer.write("\n");
//			writer.write("Hello Zubair");
//			writer.close();
//		} catch (Exception e) {
//
//		}
		// Creating new file
		try {
			File fo = new File("E:\\output.txt");
			fo.createNewFile();
			BufferedWriter writer = new BufferedWriter(new FileWriter("E:\\output.txt", true));
			writer.write("\n");
			writer.write("அகர முதல எழுத்தெல்லாம் ஆதி பகவன் முதற்றே உலகு ...\r\n"
					+ "\r\n"
					+ "Read more at: https://m.dinamalar.com/kural_detail.php?kural_no=1");
			writer.close();
			if(fo.delete()) {
				System.out.println(fo.getName());
			}
			
		} catch (Exception e) {

		}
	}
}
