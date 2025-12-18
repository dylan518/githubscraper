package ada.poo.interfaces.funcioal.exercicio.model;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
public class Produto {

    private Double preco;
    private Double peso;

    public Produto(Double preco, Double peso) {
        this.preco = preco;
        this.peso = peso;
    }
}
