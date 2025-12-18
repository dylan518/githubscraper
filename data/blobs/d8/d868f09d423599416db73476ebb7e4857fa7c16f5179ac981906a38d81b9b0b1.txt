package fgs.ffgs.cadastrounico.pessoa;

import java.io.Serializable;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Objects;
import java.util.UUID;

import fgs.ffgs.cadastrounico.documentacao.Documentacao;
import fgs.ffgs.cadastrounico.endereco.Endereco;
import fgs.ffgs.cadastrounico.pasta.Pasta;
import fgs.ffgs.cadastrounico.usuario.Usuario;
import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "Pessoa_pxj")
public class Pessoa implements Serializable{
	
	
	private static final long serialVersionUID = 1L;
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private UUID idPessoa;
	
	@Column(length=120, nullable = false, unique =false)
	private String nomePessoa;
	
	@Column(length=120, nullable = false, unique =false)
	private String nomeMae;
	 
	@Column(length=16, nullable = false, unique =true)
	private String telefone;
	
	@Column(length=200, nullable = true, unique =false)
	private String observacao;
	
	@Column(nullable = false, unique = false)
	private LocalDate dataNascimento;
	
	@Column(nullable = false, unique = false)
	private LocalDateTime dataCriacaoNoSistema; 
	
	@Column(nullable = false, unique = false)
	private LocalDateTime dataAtualizacao;
	
	@ManyToOne
	@JoinColumn(name = "usuario_id")
	private Usuario usuario;
	
	@ManyToOne
	@JoinColumn(name = "pasta_id")
	private Pasta Pasta;
	
	
	@OneToOne(mappedBy = "pessoa", cascade = CascadeType.ALL) // ATENÇÃO COM O CASCADE
	private Endereco endereco;
	
	@OneToOne(mappedBy = "pessoa", cascade = CascadeType.ALL)
	private Documentacao Documentacao;
	
	public Pessoa() {}

	public Pessoa(String nomePessoa, String nomeMae, String telefone, String observacao, LocalDate dataNascimento,
			 Usuario usuario, Pasta pasta, Endereco endereco, Documentacao documentacao) {
		
		this.nomePessoa = nomePessoa;
		this.nomeMae = nomeMae;
		this.telefone = telefone;
		this.observacao = observacao;
		this.dataNascimento = dataNascimento;
		this.dataCriacaoNoSistema = LocalDateTime.now();
		this.dataAtualizacao = LocalDateTime.now();
		this.usuario = usuario;
		Pasta = pasta;
		this.endereco = endereco;
		Documentacao = documentacao;
	}

	public UUID getIdPessoa() {
		return idPessoa;
	}

	protected void setIdPessoa(UUID idPessoa) {
		this.idPessoa = idPessoa;
	}

	public String getNomePessoa() {
		return nomePessoa;
	}

	public void setNomePessoa(String nomePessoa) {
		this.nomePessoa = nomePessoa;
	}

	public String getNomeMae() {
		return nomeMae;
	}

	public void setNomeMae(String nomeMae) {
		this.nomeMae = nomeMae;
	}

	public String getTelefone() {
		return telefone;
	}

	public void setTelefone(String telefone) {
		this.telefone = telefone;
	}

	public String getObservacao() {
		return observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public LocalDate getDataNascimento() {
		return dataNascimento;
	}

	public void setDataNascimento(LocalDate dataNascimento) {
		this.dataNascimento = dataNascimento;
	}

	public LocalDateTime getDataCriacaoNoSistema() {
		return dataCriacaoNoSistema;
	}

	
	public LocalDateTime getDataAtualizacao() {
		return dataAtualizacao;
	}

	public void setDataAtualizacao(LocalDateTime dataAtualizacao) {
		this.dataAtualizacao = dataAtualizacao;
	}

	public Usuario getUsuario() {
		return usuario;
	}

	public void setUsuario(Usuario usuario) {
		this.usuario = usuario;
	}

	public Pasta getPasta() {
		return Pasta;
	}

	public void setPasta(Pasta pasta) {
		Pasta = pasta;
	}

	public Endereco getEndereco() {
		return endereco;
	}

	public void setEndereco(Endereco endereco) {
		this.endereco = endereco;
	}

	public Documentacao getDocumentacao() {
		return Documentacao;
	}

	public void setDocumentacao(Documentacao documentacao) {
		Documentacao = documentacao;
	}

	@Override
	public int hashCode() {
		return Objects.hash(idPessoa);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Pessoa other = (Pessoa) obj;
		return Objects.equals(idPessoa, other.idPessoa);
	}
	
	
	
	
}
