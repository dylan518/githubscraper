package io.github.unlp_oo.ejercicio20;

import java.time.LocalDate;
import java.util.*;

public class Empleado {
	private String nombre;
	private String apellido;
	private String CUIL;
	private LocalDate fechaDeNacimiento;
	private boolean hijosAcargo;
	private boolean conyuge;
	private List<Contrato> contratos;
	
	
	
	public Empleado(String nombre, String apellido, String cUIL, LocalDate fechaDeNacimiento, boolean hijosAcargo,boolean con) {
		this.nombre = nombre;
		this.conyuge = con;
		this.apellido = apellido;
		this.CUIL = cUIL;
		this.fechaDeNacimiento = fechaDeNacimiento;
		this.hijosAcargo = hijosAcargo;
		this.contratos = new ArrayList<Contrato>();
	}
	
	
	private boolean puedoAgregar(Contrato c) {
		return this.contratos.stream().noneMatch(contrato -> contrato.isVigente(c.getFechaInicio()));
	}
	
	public void agregarContrato(Contrato c) {
		if (this.puedoAgregar(c)) {
			this.contratos.add(c);
		}
	}
	
	public Contrato getContratoVigente() {
		LocalDate hoy = LocalDate.now();
		return this.contratos.stream()
				.filter(contrato -> contrato.isVigente(hoy))
				.findFirst()
				.orElse(null);
	}
	
	
	public int getAntiguedad(LocalDate hoy) {
		return this.contratos.stream().mapToInt(contrato -> contrato.getAntiguedad(hoy)).sum();
	}
	
	public String generarReciboDeSueldo() {
		LocalDate hoy = LocalDate.now();
		return "Recibo de sueldo" + this.nombre 
				+ this.apellido + this.CUIL 
				+ this.getAntiguedad(hoy) + hoy 
				+ (this.getContratoVigente().calcularMonto() * this.getBonificacionPorAntiguedad(hoy));
	}
	
	public double getBonificacionPorAntiguedad(LocalDate hoy) {
		if (this.getAntiguedad(hoy)/365 >= 20) {
			return 2;
		} else if (this.getAntiguedad(hoy) >= 15) {
			return 1.7;
		} else if (this.getAntiguedad(hoy) >= 10) {
			return 1.5;
		} else if (this.getAntiguedad(hoy) >= 5) {
			return 1.3;
		}
		return 1;
	}
	
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getApellido() {
		return apellido;
	}
	public void setApellido(String apellido) {
		this.apellido = apellido;
	}
	public String getCUIL() {
		return CUIL;
	}
	public void setCUIL(String cUIL) {
		CUIL = cUIL;
	}
	public LocalDate getFechaDeNacimiento() {
		return fechaDeNacimiento;
	}
	public void setFechaDeNacimiento(LocalDate fechaDeNacimiento) {
		this.fechaDeNacimiento = fechaDeNacimiento;
	}
	public boolean isHijosAcargo() {
		return hijosAcargo;
	}
	public void setHijosAcargo(boolean hijosAcargo) {
		this.hijosAcargo = hijosAcargo;
	}


	public boolean isConyuge() {
		return conyuge;
	}


	public void setConyuge(boolean conyuge) {
		this.conyuge = conyuge;
	}


	public List<Contrato> getContratos() {
		return contratos;
	}

	

}
