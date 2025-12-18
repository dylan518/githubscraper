import java.util.List;

import javax.swing.JOptionPane;

public class Agenda {
	
    private ContatoServicos cs;

    public Agenda() {
        super();
        this.cs = new ContatoServicos();
    }

    public void adicionar(Contato ctt) {
        this.cs.addContato(ctt);
        JOptionPane.showMessageDialog(null, "Contato Adicionado Com Sucesso!");
    }

    public void atualizar(Contato ctt) {
        this.cs.attContato(ctt);
        JOptionPane.showMessageDialog(null, "Contato Atualizado Com Sucesso!");
    }

    public void consultaTudo() {
        List<Contato> lista = cs.getALL();

        System.out.println("Todos os Contatos da Agenda:"
                + "\nID : Nome : Telefone : Email");

        for (Contato ctt : lista) {
            System.out.println(ctt.getId()
                    + " : " + ctt.getNome()
                    + " : " + ctt.getTelefone()
                    + " : " + ctt.getEmail());
        }
    }

    public void consultaNome(String pnome) {
        List<Contato> lista = cs.getPessoa(pnome);

        System.out.println("Consulta Pelo Nome:"
                + "\nID : Nome : Telefone : Email");

        for (Contato ctt : lista) {
            System.out.println(ctt.getId()
                    + " : " + ctt.getNome()
                    + " : " + ctt.getTelefone()
                    + " : " + ctt.getEmail());
        }
    }

    public void consultaID(int pID) {
        List<Contato> lista = cs.getPessoaID(pID);

        String resultado = "Consulta por ID:"
                + "\nID : Nome : Telefone : Email";

        for (Contato ctt : lista) {
            resultado += "\n" + ctt.getId()
                    + " : " + ctt.getNome()
                    + " : " + ctt.getTelefone()
                    + " : " + ctt.getEmail();
        }
        JOptionPane.showMessageDialog(null, resultado);
    }
    
    public void remover(int pID) {
        Object opcoes[] = {"Confirmar","Cancelar"};
        Contato c = new Contato();
        for(Contato ctt: this.cs.getPessoaID(pID)) {
            c.setNome(ctt.getNome());
        }
        int escolha = JOptionPane.showOptionDialog(null,
                                                    "Deseja Realmente remover o contato: " + c.getNome() + "?" 
                                                    ,"Aviso!",
                                                    JOptionPane.DEFAULT_OPTION,
                                                    JOptionPane.QUESTION_MESSAGE,
                                                    null,
                                                    opcoes,
                                                    opcoes[0]);
        if(escolha==0) {
            this.cs.delContato(pID);
            JOptionPane.showMessageDialog(null,"Contato "+ c.getNome()+ " removido com sucesso!");
        }else {
            JOptionPane.showMessageDialog(null,"Operacao cancelada pelo usuario");
        }
    }
}
