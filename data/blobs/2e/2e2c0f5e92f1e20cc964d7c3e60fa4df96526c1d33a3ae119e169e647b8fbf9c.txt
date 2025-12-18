package negocio.aluno;

import dados.IRepositorioAluno;
import dados.aluno.RepositorioAluno;
import negocio.aluno.entidade.Aluno;
import negocio.excecoes.AlunoInexistenteException;

public class ControladorAluno {
  private IRepositorioAluno repositorioAluno;

  public ControladorAluno(){
    this.repositorioAluno = new RepositorioAluno();
  }

  public void inserirNovoAluno(Aluno aluno) {
    //implementar depois...
  }

  public Aluno buscarAlunoPorNome(String nomeAluno) throws AlunoInexistenteException {
    return this.repositorioAluno.buscarAluno(nomeAluno);
  }
}
