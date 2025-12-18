package Shape3D;

public class Cube extends Shape3D{
	protected double side;
	
	public Cube(double side) {
		this.side = side;
		volume = (Math.pow(side, 3));
	}

	@Override
	public void getEquivilantCube() {
		System.out.println("Cube with volume of a cube with side " + String.valueOf(side) + " has a side length "
				+ String.valueOf(side));
	}

	@Override
	public String toString() {
		return ("Cube with side " + String.valueOf(side) + 
				" and volume of " + String.valueOf(volume));
	}

}
