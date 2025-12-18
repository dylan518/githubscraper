package principal;

import java.util.ArrayList;
import java.util.Scanner;

public class Notas {

	public static void main(String[] args) {
		//El programa nos solicita la introducción de una nota y la guardará,
		//después se le pregunta al usuario si quiere introducir nueva nota,
		//si dice que si, se vuleve a solicitar otra nota, así sucesivamente
		//hasta que diga que no.
		//Tras introducir todas las notas, el programa nos muestra 
		//la nota media, el total de aprobados y todas las notas introducidas
		Scanner sc=new Scanner(System.in);
		ArrayList<Double> notas=new ArrayList<>();
		double nota;
		double media=0;
		int aprobados=0;
		String opcion;
		do {
			//pedir nota y guardar
			System.out.println("Introduce nota");
			nota=Double.parseDouble(sc.nextLine());
			notas.add(nota); //Autoboxing
			media+=nota;
			if(nota>=5) {
				aprobados++;
			}
			
			//pregutar si seguimos
			System.out.println("Desea introducir otra nota (s/n)?");
			opcion=sc.nextLine();
		}while(opcion.equalsIgnoreCase("s"));
		//las notas ya se han introducido
		media/=notas.size();
		//mostrar información
		System.out.println("Media: "+media);
		System.out.println("Aprobados: "+aprobados);
		for(Double n:notas) {
			System.out.println(n);
		}
		/*System.out.println(notas);
		int [] datos=new int[5];
		System.out.println(datos);*/
	}

}
