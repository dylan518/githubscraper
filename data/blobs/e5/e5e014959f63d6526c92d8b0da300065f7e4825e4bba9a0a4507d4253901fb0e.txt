import java.util.Objects;

public class Produto {
	private String nome;
	private String fabricante;
	private double preco;
	
	public Produto(String nome, String fabricante, double preco) {
		this.nome = nome;
		this.fabricante = fabricante;
		this.preco = preco;
	}
	
	@Override
	public int hashCode() {
		return this.nome.hashCode() + this.fabricante.hashCode();
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Produto produto = (Produto) obj;
		return this.nome.equals(produto.nome);
	}

	@Override
	public String toString() {
		return this.nome + " " + this.fabricante + " por apenas R$" + this.preco;
	}
}

