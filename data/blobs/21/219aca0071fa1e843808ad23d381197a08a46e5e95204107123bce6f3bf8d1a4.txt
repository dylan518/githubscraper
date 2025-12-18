package br.com.alura;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Curso {

	private String nome;
	private String instrutor;
	private List<Aula> aulas = new ArrayList<Aula>();
	private Set<Aluno> alunos = new HashSet();
	private Map<Integer, Aluno> matriculaParaAluno = new HashMap<>();

	// Construtor
	public Curso(String nome, String instrutor) {
		this.nome = nome;
		this.instrutor = instrutor;
	}

	// Getters
	public String getNome() {
		return nome;
	}

	public String getInstrutor() {
		return instrutor;
	}

	public List<Aula> getAulas() {
		return Collections.unmodifiableList(aulas);
	}

	public void adiciona(Aula aula) {
		this.aulas.add(aula);
	}

	public int getTempoTotal() {
		return aulas.stream().mapToInt(Aula::getDuracao).sum();
	}

	@Override
	public String toString() {
		return "[Curso: " + this.nome + " , tempo total: " + this.getTempoTotal() + ",\n" + this.aulas + "\n"
				+ this.alunos + "]";
	}

	public void matricula(Aluno aluno) {
		this.alunos.add(aluno);
		this.matriculaParaAluno.put(aluno.getNumeroMatricula(), aluno); // Foi adicionado no Map de "matriculaParaAluno"
																		// o objeto(!) aluno (ao objeto, não apenas ao
																		// objeto.nome, que seria uma String),
																		// associando a uma CHAVE, que nesse caso é o
																		// numero de matricula dele .
	}

	public Set<Aluno> getAlunos() {
		return Collections.unmodifiableSet(alunos);
	}

	public boolean estaMatriculado(Aluno aluno) {
		return alunos.contains(aluno);
	}

	public Aluno buscaMatriculado(int chave) {
		return matriculaParaAluno.get(chave);
	}
}
