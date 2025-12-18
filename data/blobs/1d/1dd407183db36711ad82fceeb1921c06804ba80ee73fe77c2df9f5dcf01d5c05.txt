package application;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Program {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.println("Enter the file path: ");
		String filePath = sc.nextLine();

		fileProcess(filePath);

		sc.close();
	}

	private static String transformLine(String line) {
		String[] strAux = line.split(",");

		double unitPrice = Double.parseDouble(strAux[1]);
		int quantity = Integer.parseInt(strAux[2]);

		return strAux[0] + "," + (quantity * unitPrice);
	}

	private static void fileProcess(String filePath) {

		try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
			String fileLine = br.readLine();
			String newLine = null;

			// create folder "out"
			createFolder(filePath, "out");

			while (fileLine != null) {
				if (fileLine != null) {
					newLine = transformLine(fileLine);
					writeToFile("/tmp/out/summary.txt", newLine, true);
				}
				fileLine = br.readLine();
			}
		} catch (IOException e) {
			System.out.println("Error: " + e.getMessage());
		}

	}

	private static void createFolder(String strPath, String dirName) {

		File path = new File(strPath);
		boolean success = new File(path.getParent() + "/" + dirName).mkdir();

		if (success) {
			System.out.println("folder out created sucessfully !");
		} else {
			System.out.println("folder out not created");
		}

	}

	private static void writeToFile(String filePath, String lineToWrite, boolean append) {

		/*
		 * FileWriter(String fileName, boolean append) Constructs a FileWriter object
		 * given a file name with a boolean indicating whether or not to append the data
		 * written.
		 */
		try (BufferedWriter bw = new BufferedWriter(new FileWriter(filePath, append))) {

			bw.write(lineToWrite);
			bw.newLine();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
