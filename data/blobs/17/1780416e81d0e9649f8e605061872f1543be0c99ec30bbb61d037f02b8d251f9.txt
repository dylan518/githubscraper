/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Model.DAO;

import java.util.ArrayList;
import Model.*;
/**
 * Classe que simula um banco de dados, porém utilizando apenas ArrayLists
 * Não realiza nenhum salvamento em arquivos externos
 * @author lym
 */
public class BancoDAO {
    public static ArrayList<Cliente> listaCliente = new ArrayList<Cliente>();
    public static ArrayList<Servico> listaServico = new ArrayList<Servico>();
    public static ArrayList<Usuario> listaUsuario = new ArrayList<Usuario>();
    public static ArrayList<Agendamento> listaAgendamento = new ArrayList<Agendamento>();
    public static void inicia(){
        Cliente cliente1 = new Cliente(1,"Matheus",'M',"14/10/2002","012345678","matheus@mail.com","123456789","endereço01","12345678");
        Cliente cliente2 = new Cliente(2,"Juliana",'F',"01/03/2000","123456789","juliana@mail","234567891","endereço02","23456789");
        Cliente cliente3 = new Cliente(3,"Meire",'F',"23/05/1969","234567890","meire@mail.com","345678901","endereço03","34567890");
        Cliente cliente4 = new Cliente(4,"Fulano",'M',"01/01/1929","345678901","fulano@mail.com","456789012","endereço04","45678901");
        Servico cabeloMasculino = new Servico(1,"Corte Masculino",40.00f);
        Servico cabeloFeminino = new Servico(2,"Corte Feminino",80.00f);
        Servico hidratacao = new Servico(3,"Lavagem e hidratação do cabelo",40.00f);
        Servico barba = new Servico(4,"Barba",30.00f);
        Usuario usr1 = new Usuario(1,"teste", "teste");
        Usuario usr2 = new Usuario(2,"barbeiro","barbeiro123");
        Usuario usr3 = new Usuario(3,"cabelereira","cabelereira123");
        Usuario usr4 = new Usuario(4,"","");
        Agendamento ag1 = new Agendamento(1,cliente1,barba,"01/08/2024 15:00");
        Agendamento ag2 = new Agendamento(2,cliente2,hidratacao,"02/08/2024 12:00");
        listaCliente.add(cliente1);
        listaCliente.add(cliente2);
        listaCliente.add(cliente3);
        listaCliente.add(cliente4);
        listaServico.add(barba);
        listaServico.add(cabeloMasculino);
        listaServico.add(cabeloFeminino);        
        listaServico.add(hidratacao);
        listaUsuario.add(usr1);
        listaUsuario.add(usr2);
        listaUsuario.add(usr3);
        listaUsuario.add(usr4);
        listaAgendamento.add(ag1);
        listaAgendamento.add(ag2);
    }
}
