package br.com.fecaf.encapsulamento;

import java.time.LocalDate;

public class Aluno {
	//Atributos da classe (sempre para ser acessado precisa do this)
	private int id;
	private String ra;
	private String nome;
	private String sobreNome;
	private String nomeCompleto;
	private String sexo;
	private String descricaoSexo;
	private String dataNascimento;
	private int idade;
	private String tipoCurso;
	
	//Construtor
	//Obs: Todo construtor sempre ter� o nome da sua classe
	public Aluno (String tipoCurso) {
		System.out.println("Construtor com tipo do Curso");
		if(tipoCurso.toUpperCase().equals("G"))
			this.tipoCurso = "Gradua��o";
		else if (tipoCurso.toUpperCase().equals("P"))
			this.tipoCurso = "P�s-Gradua��o";
	}
	//Sobrecarga de Construtores
	public Aluno () {
		System.out.println("Construtor padr�o");
		this.tipoCurso = "Gradua��o";
	}
	//Sobrecarga de Construtores
	public Aluno(String tipoCurso, int periodo) {
		System.out.println("Construtor com dois argumentos");
	}
	

	
	
	//Getters e Setters
	
	//Get id
	public int getId() {
		return this.id;
	}
	
	//Get ra
	public String getRa() {
		return this.ra;
	}
	
	//Set ra
	public void setRa(String ra) {
		this.ra = ra;
	}
	
	//Get nome
	public String getNome() {
		return this.nome;
	}
	
	//Set nome
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	//Get sobreNome
	public String getSobreNome() {
		return this.sobreNome;
	}
	
	//Set sobreNome
	public void setSobreNome(String sobreNome) {
		this.sobreNome = sobreNome;
		if (!this.nome.equals(null) && !this.sobreNome.equals(null))
			this.nomeCompleto = this.nome + " " + this.sobreNome;
		else
			System.out.println("Nome ou sobreNome n�o pode ser vazio!");
	}
	
	//Get nomeConpleto (Jun��o do nome e do sobreNome)
	public String getNomeCompleto() {
		return this.nomeCompleto;
	}
	
	//Get sexo
	public String getSexo() {
		return this.sexo;
	}
	
	//Set sexo
	public void setSexo(String sexo) {
		this.sexo = sexo.toUpperCase(); //Padroniza para MAIUSCULO a letra
		if (this.sexo.equals("M"))
			this.descricaoSexo = "Masculino";
		else if (this.sexo.equals("F"))
			this.descricaoSexo = "Feminino";
		else if(this.sexo.equals("") || this.sexo.equals(null))
			System.out.println("O sexo precisa ser informado corretamente");
			
	}
	
	//Get descricaoSexo (Esse item ser� criado no momento de gravar 
	//a letra correspondente ao sexo do aluno [M/F])
	public String getDescricaoSexo() {
		return this.descricaoSexo;
	}
	
	//Get dataNascimento
	public String getDataNascimento() {
		return this.dataNascimento;
	}
	
	//Set dataNascimento
	public void setDataNascimento(String dataNascimento) {
		this.dataNascimento = dataNascimento;
		
		
		//Retorna apenas a parte referente ao ano da data de nascimento do aluno
		int anoNascimento = Integer.parseInt(this.dataNascimento.substring(6,10));
		
		//Retorna a data atual
		LocalDate dataAtual = LocalDate.now();
		
		//Retorna somente o ano da data atual
		int anoAtual = dataAtual.getYear();
		
		//Guarda a idade atualizada do aluno
		this.idade = anoAtual - anoNascimento;
	
	}
	
	//Get idade (Ser� o calculado conforme o ano corrente e 
	//a data de nascimento do aluno)
	public int getIdade() {
		return this.idade;
	}
	
	//Retorna o tipo do curso
	public String getTipoCurso () {
		return this.tipoCurso;
	}
	
	//Guarda o tipo do curso
	//protected - significa que somente a pr�pria classe e 
	//as classes filhas (processo de heran�a entre classes) poder�o ter acesso
	protected void setTipoCurso(String tipoCurso) {
		this.tipoCurso = tipoCurso;
	}
	
	//Metodos da classe
	
	//Retorna o print de todos os dados referente a um aluno
	public void getDadosAluno () {
		System.out.println(" ################ Relat�rio de dados do aluno ##################");
		System.out.println("RA: " + this.getRa());
		System.out.println("Nome: " + this.getNomeCompleto());
		System.out.println("Sexo: [" + this.getSexo() + "]-" + this.getDescricaoSexo());
		System.out.println("Data de Nascimento: " + this.getDataNascimento());
		System.out.println("O aluno " + this.getNome() + " tem " + this.getIdade() + " anos.");
		System.out.println("Tipo do Curso: " + this.getTipoCurso());
		
	}
}
