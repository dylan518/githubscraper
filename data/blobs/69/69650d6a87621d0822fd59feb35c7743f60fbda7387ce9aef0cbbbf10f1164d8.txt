import java.util.Objects;

public class Fraction {
    private int denominator;
    private int numerator;

    public Fraction(int denominator, int numerator) {
        this.denominator = denominator;
        this.numerator = numerator;
    }

    public int getDenominator() {
        return denominator;
    }

    public void setDenominator(int denominator) {
        this.denominator = denominator;
    }

    public int getNumerator() {
        return numerator;
    }

    public void setNumerator(int numerator) {
        this.numerator = numerator;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Fraction fraction = (Fraction) o;
        return denominator == fraction.denominator && numerator == fraction.numerator;
    }

    @Override
    public int hashCode() {
        return Objects.hash(denominator, numerator);
    }

    @Override
    public String toString() {
        return "Fraction{" +
                "denominator=" + denominator +
                ", numerator=" + numerator +
                '}';
    }
}
