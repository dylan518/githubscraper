package model;

import java.util.ArrayList;

public class Curso {
	private String nome;
            private String descricao;
	private String id;
	private String preco;
	private ArrayList<Inscricao> inscricoes;
	private Instrutor instrutor;
	
	public Curso(String nome, String descricao, String id, String preco, Instrutor instrutor) {
		this.nome = nome;
                        this.descricao = descricao;
		this.id = id;
		this.preco = preco;
                        this.inscricoes = new ArrayList<>();
                        this.instrutor = instrutor;
	}

    @Override
    public boolean equals(Object obj) {
            if(obj instanceof Curso && ((Curso)obj).getId().equals(this.id)){
                  return true;
            }
            return false;
    }
	// Getters and Setters
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
        
            public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	
	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getPreco() {
		return preco;
	}
	public void setPreco(String preco) {
		this.preco = preco;
	}
            
            public String getCpf() {
                        return this.instrutor.getCpf();
            }
        
            public void adicionarInscricao(Inscricao inscricao){
                if(this.inscricoes.indexOf(inscricao) == -1)
                    this.inscricoes.add(inscricao);
            }
        
	public void removerInscricao(Estudante estudante){
                /*if(this.inscricoes.indexOf(inscricao) != -1)
                    this.inscricoes.remove(inscricao);*/
                this.inscricoes.removeIf(inscricao -> (inscricao.getEstudante().equals(estudante)));
                
                /*
                funcao (Inscricao inscricao) {
                    return inscricao.getEstudante().equals(estudante)
                }
                */
            }
            
            public ArrayList<Estudante>getEstudantesCurso() {
                ArrayList<Estudante> listaEstudantes = new ArrayList<>();
                for(Inscricao inscricao : inscricoes) {
                    listaEstudantes.add(inscricao.getEstudante());
                }
                return listaEstudantes;
            }
        
}
