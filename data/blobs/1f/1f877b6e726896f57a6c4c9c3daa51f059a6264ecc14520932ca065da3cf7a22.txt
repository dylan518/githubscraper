package File;

import java.io.File;

public class FileDirectory {

	public static void main(String[] args) {

		File dir1 = new File("People"); // Creating People folder in project
		File dir = new File("C:/Users/ISMAIL/OneDrive/Desktop/Human");// Creating Human folder in Desktop
		dir.mkdir();
		dir1.mkdir();

		String directoryLocation = dir.getAbsolutePath();
		String directoryLocation1 = dir1.getAbsolutePath();

		System.out.println("Dir 1 Path Location: " + directoryLocation1);
		System.out.println("Dir Path Location: " + directoryLocation);

		System.out.println("Name of dir1: " + dir1.getName());
		System.out.println("Name of dir: " + dir.getName());

		if (dir.delete()) {
			System.out.println(dir.getName() + " folder has been deleted!");
		}

		if (dir1.delete()) {
			System.out.println(dir1.getName() + " folder has been deleted!");
		}

		File dir3 = new File("Student"); // Creating People folder in project
		dir3.mkdir();

		File file4 = new File("C:/Users/ISMAIL/workspace/JavaOOP2023/Student/result.txt");
		File file5 = new File(dir3.getPath() + "/Courses.txt");// path can be accessed using get mehtod
		try {
			file4.createNewFile();
			file5.createNewFile();
			System.out.println("Files are created!");
		} catch (Exception e) {
			System.out.println("Excepiton: " + e);
		}

		if (file4.exists()) {
			System.out.println("File 4 exists!");
		} else {
			System.out.println("File 4 doesn't exists!");
		}

	}

}
