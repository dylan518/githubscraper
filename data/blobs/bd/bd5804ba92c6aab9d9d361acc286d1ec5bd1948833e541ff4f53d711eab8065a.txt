package org.generation.italy.model;

import java.time.LocalDate;
import java.util.Scanner;

public class Recensione {

	private LocalDate data;
	private String nomeUtente;
	private int numeroStelle;
	private String testo;

	public Recensione(LocalDate data, String nomeUtente, int numeroStelle, String testo) {
		super();
		this.data = data;
		this.nomeUtente = nomeUtente;
		setNumeroStelle(numeroStelle, null);
		setTesto(testo, null);
	}

	public LocalDate getData() {
		return data;
	}


	public String getNomeUtente() {
		return nomeUtente;
	}

	public void setNomeUtente(String nomeUtente) {
		Scanner sc = new Scanner(System.in);
		while(nomeUtente.isBlank()) {
		System.out.println("Inserire nomeUtente:");
		nomeUtente=sc.nextLine();
		}
		this.nomeUtente = nomeUtente;
		sc.close();
	}

	public int getNumeroStelle() {
		return numeroStelle;
	}

	public void setNumeroStelle(int numeroStelle,Scanner sc) {
		while (numeroStelle < 1 || numeroStelle > 5) {
			System.out.println("Inserisci un numero da 1 a 5: ");
			numeroStelle = sc.nextInt();
			sc.nextLine();
		}
		this.numeroStelle = numeroStelle;
		
	}

	public String getTesto() {
		return testo;
	}

	public void setTesto(String testo,Scanner sc) {
		while(testo.isBlank()) {
		System.out.println("Inserire commento:");
		testo=sc.nextLine();			
		}
		this.testo = testo;
		
	}

	@Override
	public String toString() {
		return "Recensione [Data=" + data + ", Nome Utente=" + nomeUtente + ", Numero Stelle=" + numeroStelle + ", Commento="
				+ testo + "]";
	}

}
