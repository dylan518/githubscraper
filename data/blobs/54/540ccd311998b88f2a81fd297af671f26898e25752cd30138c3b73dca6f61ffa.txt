package buffer;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;

public class FileWriting {

	public static void main(String[] args) {
		
		try(FileOutputStream fileOutput = new FileOutputStream("example2.txt")) {
			
			FileChannel channel = fileOutput.getChannel();
			
			// Create a buffer
			ByteBuffer byteBuffer = ByteBuffer.allocate(100);
			
			String text = "This is my third buffer, trying to write it into a file";
			
			//Puting the String into the buffer
			byteBuffer.put(text.getBytes());
			
			byteBuffer.flip();
			
			channel.write(byteBuffer);
			
		} catch(IOException e) {
			System.out.println(e);
		}

	}

}
