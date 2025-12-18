public class Main {
  public static void main(String[] args) {
      VeiculoFactory fabrica;

      fabrica = VeiculoFactory.getFactory("esportivo");
      Carro carroEsportivo = fabrica.criarCarro();
      Moto motoEsportiva = fabrica.criarMoto();

      carroEsportivo.exibirDetalhes();
      motoEsportiva.exibirDetalhes();

      fabrica = VeiculoFactory.getFactory("luxuoso");
      Carro carroLuxuoso = fabrica.criarCarro();
      Moto motoLuxuosa = fabrica.criarMoto();

      carroLuxuoso.exibirDetalhes();
      motoLuxuosa.exibirDetalhes();  
  }
}
