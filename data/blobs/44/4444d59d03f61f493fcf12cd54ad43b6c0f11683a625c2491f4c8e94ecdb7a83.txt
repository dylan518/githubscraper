package list.OperacoesBasicas2;

import java.util.ArrayList;
import java.util.List;

public class CarrinhoDeCompras{

    private List<Item> itemList;

    public CarrinhoDeCompras(){
        this.itemList = new ArrayList<>();
    }
    public void adicionarItem(String nome, double preco, int quantidade){
        Item item = new Item(nome,preco,quantidade);
        itemList.add(item);
    }
    public void removerItem(String nome){
        List<Item> itemRemover = new ArrayList<>();
        if (!itemList.isEmpty()){
            for(Item I : itemList){
                if(I.getNome().equalsIgnoreCase(nome)){ 
                itemRemover.add(I);
                }
            }
            itemList.removeAll(itemRemover);
        }else{
            throw new RuntimeException("A lista está vazia ");
        }       
    
    }    
    public double calcularValorTotal(){
        double total = 0;
        double totalFinal =0;
        if(!itemList.isEmpty()){
            for(Item item : itemList){
            total = item.getPreco() * item.getQuantidade();
            totalFinal += total;
            }
             
        }else{
            throw new RuntimeException("A lista está vazia");
        }   
        return totalFinal;  
    }
    public void exibirItens(){
        if(!itemList.isEmpty()){
            System.out.println(itemList);
        }else{
            throw new RuntimeException("Não tem produtos");  
        }
    }
    public static void main(String[] args) {
        CarrinhoDeCompras carrinhoDeCompras = new CarrinhoDeCompras();
        
        carrinhoDeCompras.adicionarItem("Caneta", 2.59, 3);
        carrinhoDeCompras.adicionarItem("Caneta", 2.59, 3);
        carrinhoDeCompras.adicionarItem("Mochila", 60.50, 1);
        carrinhoDeCompras.adicionarItem("bola", 50.90, 2);

        carrinhoDeCompras.removerItem("Caneta");
        carrinhoDeCompras.exibirItens();

        System.out.println("Total da Compra: " + carrinhoDeCompras.calcularValorTotal());

    }

}