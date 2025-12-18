package test.bebidaTest;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import Model.Bebida;

public class bebidaTest {

    Bebida sacola = new Bebida(222,"Coca Cola","Refrigerante de 2 litros",3, 15.00);

    @DisplayName("Classe para teste da Bebida")
    @Test
    public void testCriaBebida(){
        Assertions.assertAll("sacola",
        () -> assertEquals(222,sacola.getId_bebida()),
        () -> assertEquals("Coca Cola",sacola.getNome()),
        () -> assertEquals("Refrigerante de 2 litros",sacola.getDescricao()),
        () -> assertEquals(3,sacola.getQuantidade())
        );
    }
    @DisplayName("Classe para calcular valor para pagar")
    @Test
        public void testAddItem() {
            double preco = (sacola.getQuantidade() * sacola.getValor_compra());
            Assertions.assertEquals(45, preco);
                
        }
    @DisplayName("Classe para verificar se são mesmo lote de bebida")
    @Test
        public void testLoteIgualBebida(){
           Bebida sacola2 = new Bebida(225,"Coca Cola","Refrigerante de 2 litros",3, 15.00);
           
           assertNotEquals(sacola.getId_bebida(),sacola2.getId_bebida());
 
        }

     @DisplayName("Classe para aumentar o valor de uma bebida")
        @Test
        public void testAumentoDepreco(){

            double aumento = 1.4 ;
            sacola.setValor_compra(sacola.getValor_compra() * aumento);
            Assertions.assertEquals(21, sacola.getValor_compra());
            
        }

         @DisplayName("Classe para diminuir o valor de uma bebida")
        @Test
        public void testDiminuirDepreco(){

            double promocao = 0.8 ;
            sacola.setValor_compra(sacola.getValor_compra() * promocao);
            Assertions.assertEquals(12, sacola.getValor_compra());
            
        }

        @DisplayName("Classe para alterar descricao")
        @Test
        public void testAlterarDescricao(){
            sacola.setDescricao("Refrigerante zero açucar");
             Assertions.assertEquals("Refrigerante zero a\u00E7ucar", sacola.getDescricao());
            
        }

}