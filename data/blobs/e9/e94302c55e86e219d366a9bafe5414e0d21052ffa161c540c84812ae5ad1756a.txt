import java.util.Arrays;
import java.util.List;

public class Main {
  public static void main(String[] args) {
    Aluno maria = new Aluno("Maria", "maria@gmail.com");
    Aluno joao = new Aluno("Joao", "joao@gmail.com");
    Aluno paulo = new Aluno("Paulo", "paulo@gmail.com");
    Aluno pedro = new Aluno("Pedro", "pedro@gmail.com");

    List<Aluno> alunos = Arrays.asList(maria, joao, paulo, pedro);
    alunos.sort((a1, a2)-> a1.getNome().compareTo(a2.getNome()));
    alunos.subList(0, 2).forEach(System.out::println);
  }
}