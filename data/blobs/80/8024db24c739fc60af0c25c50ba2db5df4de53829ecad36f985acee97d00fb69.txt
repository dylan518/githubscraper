package com.upe.atividades.pessoa;

public class Nota {
	
	private Double nota;
	private Double peso;
	
	public Nota(Double nota, Double peso) {
		this.nota = nota;
		this.peso = peso;
	}
	
	public Double getNota() {
		return nota;
	}
	
	public void setNota(Double nota) {
		this.nota = nota;
	}
	
	public Double getPeso() {
		return peso;
	}
	
	public void setPeso(Double peso) {
		this.peso = peso;
	}

	@Override
	public String toString() {
		return "Nota [nota=" + nota + ", peso=" + peso + "]";
	}
	
}
