/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package exemplo02;

/**
 *
 * @author Danilo Medeiros Eler (FCT-UNESP) - https://daniloeler.github.io/
 */
public class Aluno {
    private String nome;
    private float nota1;
    private float nota2;

    public Aluno() {
    }

    public Aluno(String nome, float nota1, float nota2) {        
        this.nome = nome;
        this.nota1 = nota1;
        this.nota2 = nota2;
    }
    
    public void exibir(){        
        System.out.println("Nome: "+nome);;
        System.out.println("Nota 1: "+nota1);
        System.out.println("Nota 2: "+nota2);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public float getNota1() {
        return nota1;
    }

    public void setNota1(float nota1) {
        this.nota1 = nota1;
    }

    public float getNota2() {
        return nota2;
    }

    public void setNota2(float nota2) {
        this.nota2 = nota2;
    }
    
}
