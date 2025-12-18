package src.patterns.behavioral.strategy.example1;

// Client
public class Client {
    public static void main(String[] args) {
        double a = 5.0;
        double b = 2.0;
        CalculatorContext calculatorContext = new CalculatorContext(new Add());
        calculatorContext.performCalculation(a, b);

        calculatorContext.setCalculatorStrategy(new Subtract());
        calculatorContext.performCalculation(a, b);

        calculatorContext.setCalculatorStrategy(new Multiply());
        calculatorContext.performCalculation(a, b);

        calculatorContext.setCalculatorStrategy(new Divide());
        calculatorContext.performCalculation(a, b);
    }
}

// Context
class CalculatorContext {
    private CalculatorStrategy calculatorStrategy;

    public CalculatorContext(CalculatorStrategy calculatorStrategy) {
        this.calculatorStrategy = calculatorStrategy;
    }

    public void setCalculatorStrategy(CalculatorStrategy calculatorStrategy) {
        this.calculatorStrategy = calculatorStrategy;
    }

    public void performCalculation(double a, double b) {
        calculatorStrategy.calculate(a,b);
    }
}

// Strategy Interface
interface CalculatorStrategy {
    void calculate(double a, double b);
}


// Strategies
class Add implements CalculatorStrategy{
    public @Override void calculate(double a, double b){
        double res = a + b;
        System.out.println(a + " + " + b + " = " + res);
    }
}

class Subtract implements CalculatorStrategy{
    public @Override void calculate(double a, double b){
        double res = a - b;
        System.out.println(a + " - " + b + " = " + res);    
    }
}

class Multiply implements CalculatorStrategy{
    public @Override void calculate(double a, double b){
        double res = a * b;
        System.out.println(a + " * " + b + " = " + res);
    }
}

class Divide implements CalculatorStrategy{
    public @Override void calculate(double a, double b){
        double res = a / b;
        System.out.println(a + " / " + b + " = " + res);
    }
}