package tech.thiagorsouza.core;

import tech.thiagorsouza.utils.DialogMessage;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Pedido {

  private final Cliente cliente;
  private final int codigo;
  private int avaliacao;
  private List<Produto> produtos = new ArrayList<>();

  private static final double VALOR_ITEM = 10.00;

  public Pedido(Cliente cliente) {
    this.cliente = cliente;
    this.codigo = UUID.randomUUID().hashCode();
  }

  public void setAvaliacao(int avaliacao) {
    this.avaliacao = avaliacao;
  }

  public int getAvaliacao() {
    return avaliacao;
  }

  public void adicionarProduto() {
    String codigoProduto = DialogMessage.showInput("Digite o código do produto:");
    int quantidade = DialogMessage.showIntegerInput("Digite a quantidade:");

    if (quantidade <= 0) {
      DialogMessage.showMessage("Quantidade inválida. A quantidade deve ser um número positivo.");
      return;
    }

    Produto produto = new Produto(codigoProduto, quantidade);
    produtos.add(produto);
  }

  public List<Produto> getProdutos() {
    return produtos;
  }

  public double getValorTotal() {
    double sum = 0.0;
    for (Produto produto : produtos) {
      sum += produto.getValorTotal();
    }
    return sum;
  }

  private class Produto {
    private String codigoProduto;
    private int quantidade;

    public Produto(String codigoProduto, int quantidade) {
      this.codigoProduto = codigoProduto;
      this.quantidade = quantidade;
    }

    public double getValorTotal() {
      return quantidade * VALOR_ITEM;
    }
  }
}