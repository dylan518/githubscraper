public class QuadraticEquation {
    private double a, b, c;
    private Double x1, x2;

    public QuadraticEquation(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;

        double discriminant = b * b - 4 * a * c;
        if (discriminant > 0) {
            x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            x2 = (-b - Math.sqrt(discriminant)) / (2 * a);
        } else if (discriminant == 0) {
            x1 = x2 = -b / (2 * a);
        } else {
            x1 = x2 = null;
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        QuadraticEquation that = (QuadraticEquation) obj;
        return (x1 == null ? that.x1 == null : x1.equals(that.x1)) &&
                (x2 == null ? that.x2 == null : x2.equals(that.x2));
    }

    @Override
    public int hashCode() {
        return (x1 == null ? 0 : x1.hashCode()) + (x2 == null ? 0 : x2.hashCode());
    }

    @Override
    public String toString() {
        return "QuadraticEquation{\n"
                + "\ta= " + a + ",\n"
                + "\t b= " + b + ",\n"
                + "\t c= " + c + ",\n"
                + "\t x1= " + x1  + ",\n"
                + "\t x2= " + x2  + ",\n"
                +  "}";
    }
}
