package br.edu.ifpe.apoo.negocio;

import br.edu.ifpe.apoo.entidades.Aluno;
import br.edu.ifpe.apoo.excecoes.ExcecaoAlunoInvalido;


public class ControladorAluno {

    private PersistenciaFacade persistenciaFacade;

    public ControladorAluno() {
        this.persistenciaFacade = FacadeFactory.getInstanciaPersistenciaFacade(); 
    }

    public void inserir(Aluno aluno) throws ExcecaoAlunoInvalido {
    	if (aluno == null) {
            throw new ExcecaoAlunoInvalido("Aluno inválido");
        }
        persistenciaFacade.inserirAluno(aluno);
    }

    public void atualizar(Aluno aluno) throws ExcecaoAlunoInvalido {
    	if (aluno == null) {
            throw new ExcecaoAlunoInvalido("Aluno inválido");
        }
        persistenciaFacade.atualizarAluno(aluno);
    }

    public boolean remover(long id) throws ExcecaoAlunoInvalido {
    	 if (id == 0) {
             throw new ExcecaoAlunoInvalido("ID de Aluno inválido");
         }

        return persistenciaFacade.removerAluno(id);
    }

    public Aluno get(long id) throws ExcecaoAlunoInvalido {
    	if (id == 0) {
            throw new ExcecaoAlunoInvalido("ID de Aluno inválido");
        }
        return persistenciaFacade.consultarAluno(id);
    }
    
    public boolean validarCPF(String CPF) {
        return persistenciaFacade.validarCPF(CPF);
    }
}

