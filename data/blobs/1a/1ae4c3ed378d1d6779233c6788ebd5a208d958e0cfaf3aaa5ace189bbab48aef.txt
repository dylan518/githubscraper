package br.com.fiap.Challengesprint3.models;

import java.io.Serializable;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.Table;
import javax.persistence.ManyToOne;

@Entity
@Table(name = "T_CLG_ENDERECO")
public class Endereco implements Serializable{

	private static final long serialVersionUID = 1L;

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;

	private Integer cep;
	
	private String nomeRua; 

	private Integer numeroRua;

	private String complemento;

	//Relacao de muitos para um de endereco para Bairro
	@ManyToOne(cascade = CascadeType.ALL, fetch = FetchType.EAGER)
	@JoinColumn()
	private Bairro bairro;

	public Endereco() {

	}

	public Endereco(Integer cep, String nomeRua, Integer numeroRua, String complemento, Bairro bairro) {
		super();
		this.cep = cep;
		this.nomeRua = nomeRua;
		this.numeroRua = numeroRua;
		this.complemento = complemento;
		this.bairro = bairro;
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}
	
	public Integer getCep() {
		return cep;
	}
	
	public void setCep(Integer cep) {
		this.cep = cep;
	}
	
	public String getNomeRua() {
		return nomeRua;
	}
	
	public void setNomeRua(String nomeRua) {
		this.nomeRua = nomeRua;
	}
	
	public Integer getNumeroRua() {
		return numeroRua;
	}
	
	public void setNumeroRua(Integer numeroRua) {
		this.numeroRua = numeroRua;
	}
	
	public String getComplemento() {
		return complemento;
	}
	
	public void setComplemento(String complemento) {
		this.complemento = complemento;
	}

	public Bairro getBairro() {
		return bairro;
	}

	public void setBairro(Bairro bairro) {
		this.bairro = bairro;
	}

	@Override
	public String toString() {
		return "Endereco [cep=" + cep + ", complementob " + complemento + "nomeRua" + nomeRua + ", numeroRua=" + numeroRua + ", bairro=" + bairro +"]";
	}

}
