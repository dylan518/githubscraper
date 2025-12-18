package Exercicios_Aula4;

import Exercicios_Aula4.Itens.ItemArmadura;
import Exercicios_Aula4.Itens.ItemDano;

public class ExecucaoDosConceitos {

    public static void main(String[] args) {
        //Screen minhaJanela = new Screen();

    }



    public static void  testeHeranca(){
        ItemDano espada = new ItemDano();
        espada.setNome("Espada Léndaria");
        espada.setRaridade("Léndaria");
        espada.setDano(10);

        System.out.println(espada.trazerInformacoesSobre());

        ItemArmadura armadura = new ItemArmadura();
        System.out.println(armadura.trazerInformacoesSobre());
    }



    public static void testeEventos(){
        for (int i = 0; i < 100; i++) {
            boolean aconteceu = GameUtil.eventoAconteceApartirDeUmaProbabilidade(90);
            System.out.println(aconteceu ? "Aconteceu" : "Não Aconteceu");
        }
    }

}
