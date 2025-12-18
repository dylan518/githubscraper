public class Sphere extends Shape implements Volume {
    private double radius;

    // Constructor to initialize sphere radius
    public Sphere(double radius) {
        super("Sphere");
        this.radius = radius;
    }

    @Override
    public double calculateArea() {
        return 4 * Math.PI * radius * radius; // Surface area formula for a sphere
    }

    @Override
    public double calculatePerimeter() {
        return 0; // Perimeter does not apply to spheres
    }

    @Override
    public double calculateVolume() {
        return (4.0 / 3.0) * Math.PI * Math.pow(radius, 3); // Volume formula for a sphere
    }
}

