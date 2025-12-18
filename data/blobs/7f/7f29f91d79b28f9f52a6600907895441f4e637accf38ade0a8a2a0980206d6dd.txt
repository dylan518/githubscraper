package test;

public class Triangle {
	private int base;
	private int height;
	
	public Triangle (int base, int height) {
		this.base = base;
		this.height = height;
	}
	
	public double calArea() {
	    return (base * height) / 2.0;
	}
	
	@Override
	public String toString() {
	     return "밑변 : " + base + " 높이 : " + height + " 넓이 : " + calArea();
	}
}
