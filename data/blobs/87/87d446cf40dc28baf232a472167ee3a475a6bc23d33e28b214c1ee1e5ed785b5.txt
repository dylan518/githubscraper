import org.junit.Before;
import org.junit.Test;
import org.junit.jupiter.api.BeforeEach;

import static org.junit.jupiter.api.Assertions.*;

public class RecepcaoTest {
    FuncionarioDoutorado funcionarioDoutorado;
    FuncionarioProfessor funcionarioProfessor;
    FuncionarioMestrado funcionarioMestrado;

    @BeforeEach
    void setUp(){
        funcionarioDoutorado = new FuncionarioDoutorado(funcionarioDoutorado);
        funcionarioProfessor = new FuncionarioProfessor(funcionarioProfessor);
        funcionarioMestrado = new FuncionarioMestrado(null);
    }

    @Test
    void deveRetornarProfessorDoutorado(){
        assertEquals("Aula dada pelo professor padrao",
                funcionarioDoutorado.executarFuncao(new Recepcao(Doutorado.getInstance())));
    }

    @Test
    void deveRetornarProfessorProfessor(){
        Recepcao recepcao = new Recepcao(Professor.getInstance());
        assertEquals("Aula dada pelo professor simples", funcionarioProfessor.executarFuncao(recepcao));
    }


    @Test
    void deveRetornarProfessorMestrado(){
        Recepcao recepcao = new Recepcao(Mestrado.getInstance());
        assertEquals("Professor Mestrado", funcionarioMestrado.executarFuncao(recepcao));
    }

    @Test
    void deveRetornarProfessorIndisponivel(){
        Recepcao recepcao = new Recepcao(Mestrado.getInstance());
        funcionarioMestrado.atendimentoFuncionario.remove(0);
        assertEquals("O serviço desejado está indisponivel", funcionarioMestrado.executarFuncao(recepcao));
    }


}
