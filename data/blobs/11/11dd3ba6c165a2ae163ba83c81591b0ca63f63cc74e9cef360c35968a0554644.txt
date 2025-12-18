package prog.unidad07.ejercicio02;

public class Consultor extends Empleado {
  
  // Atributos
  // Tarifa por hora
  protected double tarifaHora;
  // Horas trabajadas
  protected int horasTrabajadas;

  /**
   * @param nombre Nombre del consultor. No puede ser null
   * @param dni DNI del consultor. No puede ser null
   * @param telefono Teléfono del consultor. No puede ser null
   * @param tarifaHora Tarifa que cobra el consultor por hora (no puede ser negativa)
   * @param horasTrabajadas Horas trabajadas este mes (no puede ser negativo)
   * @throws NullPointerException Si nombre, dni o telefono son null
   * @throws IllegalArgumentException Si tarifaHora u horasTrabajadas son negativas
   */
  protected Consultor(String nombre, String dni, String telefono, double tarifaHora,
      int horasTrabajadas) {
    super(nombre, dni, telefono);
    if (tarifaHora >= 0 && horasTrabajadas >= 0) {
      this.tarifaHora = tarifaHora;
      this.horasTrabajadas = horasTrabajadas;
    } else {
      throw new IllegalArgumentException("La tarifa y el número de horas deben ser positivos");
    }
  }

  @Override
  public double getSalario() {
    return redondea2Decimales(tarifaHora * horasTrabajadas);
  }
}
