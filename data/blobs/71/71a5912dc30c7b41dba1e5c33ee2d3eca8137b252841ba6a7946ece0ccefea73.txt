package ejercicio01;

/**
 * Clase CuentaCorriente
 * 
 * @author Nestor Sanchez
 */
public class CuentaCorriente {

	/**
	 * String dni: dni del usuario
	 */
	private String dni;

	/**
	 * String nombre: nombre del usuario
	 */
	private String nombre;

	/**
	 * String saldo: saldo del usuario
	 */
	private int saldo;

	/**
	 * Constructor sin parametros
	 */
	public CuentaCorriente() {
		super();
	}

	/**
	 * Constructor con todos los parametros
	 * 
	 * @param dni:    dni del usuario
	 * @param nombre: nombre del usuario
	 * @param saldo:  saldo inicial del usuario
	 */
	public CuentaCorriente(String dni, String nombre, int saldo) {
		super();
		this.dni = dni;
		this.nombre = nombre;
		this.saldo = saldo;
	}

	/**
	 * Funcion sacarDinero: saca dinero de la cuenta
	 * 
	 * @param cantidad de dinero a retirar
	 * @return: si se ha podido hacer la operacion o no
	 */
	public boolean sacarDinero(int cantidad) {

		// boolean esExitoso: booleana que indica si la funcion ha salido bien o no (por
		// defecto, es falso)
		boolean esExitoso = false;

		// If: si la cantidad es menor que el saldo, se le restara al saldo la cantidad,
		// y esExitoso sera true
		if (cantidad < saldo) {
			saldo = saldo - cantidad;
			esExitoso = true;
		} // Fin If

		// Devuelve esExitoso al main
		return esExitoso;

	}

	/**
	 * Funcion ingresarDinero: ingresa dinero a la cuenta
	 * 
	 * @param cantidad de dinero a ingresar
	 * @return: si se ha podido hacer la operacion o no
	 */
	public boolean ingresarDinero(int cantidad) {

		// boolean esExitoso: booleana que indica si la funcion ha salido bien o no (por
		// defecto, es falso)
		boolean esExitoso = false;

		// If: si la cantidad es mayor que 0, se le sumara al saldo la cantidad, y
		// esExitoso sera true
		if (cantidad > 0) {
			saldo = saldo + cantidad;
			esExitoso = true;
		} // Fin If

		// Devuelve esExitoso al main
		return esExitoso;

	}

	/**
	 * Funcion mostrarInformacion: muestra informacion de la cuenta
	 */
	public void mostrarInformacion() {

		System.out.println("DNI: " + dni);
		System.out.println("Nombre: " + nombre);
		System.out.println("Saldo: " + saldo + " NS$");

	}

}
