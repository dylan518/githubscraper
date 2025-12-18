
public class Electrodomestico {

	private double precioBase;
	private colores color;
	private consumoEnergetico consumoEnerg;
	private double peso;

	private final colores COLOR = colores.blanco;
	private final consumoEnergetico CONSUMO = consumoEnergetico.F;
	private final double PRECIO_BASE = 100;
	private final double PESO = 5;

	public Electrodomestico() {
		this.precioBase = PRECIO_BASE;
		this.color = COLOR;
		this.consumoEnerg = CONSUMO;
		this.peso = PESO;
	}

	public Electrodomestico(double precioBase, colores color, consumoEnergetico consumoEnerg, double peso) {
		super();
		this.precioBase = precioBase;
		this.color = color;
		this.consumoEnerg = consumoEnerg;
		this.peso = peso;
	}

	public Electrodomestico(double precioBase, double peso) {
		super();
		this.precioBase = precioBase;
		this.peso = peso;
		this.color = COLOR;
		this.consumoEnerg = CONSUMO;
	}

	public double getPrecioBase() {
		return precioBase;
	}

	public void setPrecioBase(double precioBase) {
		this.precioBase = precioBase;
	}

	public colores getColor() {
		return color;
	}

	public void setColor(colores color) {
		this.color = color;
	}

	public consumoEnergetico getConsumoEnerg() {
		return consumoEnerg;
	}

	public void setConsumoEnerg(consumoEnergetico consumoEnerg) {
		this.consumoEnerg = consumoEnerg;
	}

	public double getPeso() {
		return peso;
	}

	public void setPeso(double peso) {
		this.peso = peso;
	}

	@Override
	public String toString() {
		return "Electrodomestico [precioBase=" + precioBase + ", color=" + color + ", consumoEnerg=" + consumoEnerg
				+ ", peso=" + peso + ", COLOR=" + COLOR + ", CONSUMO=" + CONSUMO + ", PRECIO_BASE=" + PRECIO_BASE
				+ ", PESO=" + PESO + "]";
	}

}
