import desafio.dominio.*;

import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        Curso curso1 = new Curso();
        Mentoria mentoria1 = new Mentoria();
        Conteudo conteudo1 = new Curso();

        curso1.setTitulo ("Curso java");
        curso1.setDescricao ("Curso java muito bom");
        curso1.setCargaHoraria (40);



        mentoria1.setTitulo ("Mentoria de JAva");
        mentoria1.setDescricao ("Mentoria JavaScript");
        mentoria1.setData(LocalDate.now());


        //System.out.println(curso1);
        //System.out.println(mentoria1);

        BootCamp bootCamp1 = new BootCamp();
        bootCamp1.setNome("BootCamp Java");
        bootCamp1.setDescricao ("Bootcamp Java muito legal.");
        bootCamp1.getConteudos().add(curso1);
        bootCamp1.getConteudos().add(mentoria1);

        Dev devLeandro = new Dev();

        devLeandro.setNome("Leandro Gerolim");
        devLeandro.inscreverBootcamp(bootCamp1);
        System.out.println("Conteudos Inscritos" + devLeandro.getConteudoInscritos());
        devLeandro.progredir();

        System.out.println("Conteudos Concluidos" + devLeandro.getConteudoConcluidos());

        System.out.println("----------------------------------------------------------------");
        Dev devJoao = new Dev();

        devJoao.setNome("Joao");
        devJoao.inscreverBootcamp(bootCamp1);
        System.out.println("Conteudos Inscritos" + devJoao.getConteudoInscritos());
        devJoao.progredir();

        System.out.println("Conteudos Concluidos" + devJoao.getConteudoConcluidos());


    }
}