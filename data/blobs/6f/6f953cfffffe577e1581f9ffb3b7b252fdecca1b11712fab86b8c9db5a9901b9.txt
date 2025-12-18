package main.java.map.Pesquisa;

import java.util.HashMap;
import java.util.Map;

public class EstoqueProdutos {
  private Map<Long, Produto> estoqueProdutosMap;


  public EstoqueProdutos() {
    this.estoqueProdutosMap = new HashMap<>();
  }

  public void adicionarProcuto(long cod, String nome, int quantidade, double preco) {
    estoqueProdutosMap.put(cod, new Produto(nome, preco, quantidade));
  }

  public void exibirProdutos() {
    System.out.println(estoqueProdutosMap);
  }

  public double calcularValorTotaltEstoque(){
    double valorTotalEstoque = 0d;
    if(!estoqueProdutosMap.isEmpty()) {
      for(Produto p: estoqueProdutosMap.values()) {
        valorTotalEstoque += (p.getPreco() * p.getQuantidade());
      }
    }
    return valorTotalEstoque;
  }

  public Produto obterProdutoMaisCaro() {
    Produto produtoMaisCaro = null;
    double maiorPreco = Double.MIN_VALUE;

    if(!estoqueProdutosMap.isEmpty()) {
      for(Produto p: estoqueProdutosMap.values()) {
        if(p.getPreco() > maiorPreco) {
          produtoMaisCaro = p;
        }
      }
    }

    return produtoMaisCaro;

  }

  public Produto obterProdutoMaisBarto() {
    Produto produtoMaisBarato = null;
    double menorPreco = Double.MAX_VALUE;

    if(!estoqueProdutosMap.isEmpty()) {
      for(Produto p: estoqueProdutosMap.values()) {
        if(p.getPreco() < menorPreco) {
          System.out.println(menorPreco);
          menorPreco = p.getPreco();
          produtoMaisBarato = p;
        }
      }
    }

    return produtoMaisBarato;
  }

  public Produto obterProdutoMaiorQuantidadeValorTotalNoEstoque() {
    Produto produtoMaiorValorTotal = null;
    double valorTotal = 0;
    double maiorValorTotal = Double.MIN_VALUE;

    if(!estoqueProdutosMap.isEmpty()) {
      for(Produto p: estoqueProdutosMap.values()) {
        valorTotal = p.getPreco() * p.getQuantidade();
        if( valorTotal > maiorValorTotal) {
          maiorValorTotal = valorTotal;
          produtoMaiorValorTotal = p;
        }
      }
    }
    
    return produtoMaiorValorTotal;
  }

  public static void main(String[] args) {
    EstoqueProdutos estoque = new EstoqueProdutos();

    estoque.exibirProdutos();

    estoque.adicionarProcuto(1l, "Produto A", 10, 5.0);
    estoque.adicionarProcuto(2L, "Produto B", 15, 10.0);
    estoque.adicionarProcuto(3l, "Produto C", 2, 15.0);

    estoque.exibirProdutos();

    System.out.println(estoque.calcularValorTotaltEstoque());
    System.out.println(estoque.obterProdutoMaisCaro());
    System.out.println(estoque.obterProdutoMaisBarto());
    System.out.println(estoque.obterProdutoMaiorQuantidadeValorTotalNoEstoque());
  }
}
