package oia_armandoMoviles;

import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class RegistroColgantes {

	private String name;

	public RegistroColgantes(String name) {
		this.name = name;
	}

	public ArrayList<Colgante> leerRegistro() {

		File pf = null;
		Scanner scan = null;
		ArrayList<Colgante> colgantes = new ArrayList<Colgante>();

		try {

			pf = new File("casosDePrueba/" + "in/" + this.name + ".in");
			scan = new Scanner(pf);

			int C = scan.nextInt();
			double peso;
			for (int i = 0; i < C; i++) {
				peso = scan.nextDouble();
				colgantes.add(new Colgante(peso));
			}

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if (scan != null)
				scan.close();
		}

		return colgantes;
	}

	public void escribirRegistro(Fabrica fabrica) {

		FileWriter archivo = null;
		PrintWriter printWr = null;

		double pesoTotal = fabrica.getPesoTotal();
		int nroVarillas = fabrica.getNumeroVarillas();
		int nroMoviles = fabrica.getNumeroMoviles();
		try {
			archivo = new FileWriter("casosDePrueba/" + "out_obtenido/" + this.name + ".out");
			printWr = new PrintWriter(archivo);

			if (nroMoviles != 0)
				printWr.print(String.format("%.0f %d", pesoTotal, nroVarillas));
			else
				printWr.print("no se puede");
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			printWr.close();
		}
	}

}
