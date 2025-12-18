public class Power extends Function {
    private Function base;
    private double exponent;

    public Power(Function base, double exponent) {
        this.base = base;
        this.exponent = exponent;
    }

    @Override
    public double valueAt(double point) {
        return Math.pow(base.valueAt(point), exponent);
    }

    @Override
    public String toString() {
        if (exponent == 1) {
            return base.toString();
        } else {
            return "(" + base.toString() + ")^" + exponent + "";
        }
    }

    @Override
    public Function derivative() {
        Function derivativeBase = base.derivative();
        if (exponent == 1) {
            return derivativeBase;
        }
        else {
            String derivativeExponent = "" + exponent + " * (" + base.toString() + ")^" + (exponent - 1) + "";
            return "(" + derivativeBase + ") * " + derivativeExponent;
        }
    }
}
