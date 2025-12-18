package calculator;

import java.util.*;
import java.util.stream.*;

public class ArithmeticCalculator<T extends Number> {
    private static final List<Double> results = new ArrayList<>();
    private static final int MAX_SIZE = 5;

    public double calculate(T a, T b, OperatorType operator) {
        double num1 = a.doubleValue();
        double num2 = b.doubleValue();
        double result = operator.doCalculation(num1, num2);
        addResult(result);
        return result;
    }

    public void addResult(double result) {
        results.add(result);
        removeOldestResult();
    }

    public void removeOldestResult() {
        if (results.size() > MAX_SIZE) {
            results.remove(0);
            System.out.println("저장된 결과가 5개 초과하여, 가장 먼저 입력된 결과가 삭제됩니다.");
        }

    }


    public List<Double> getBigResult(String input) {

        try {
            double big = Double.parseDouble(input);
            List<Double> filteredResults = results.stream()
                    .filter(result -> result > big)
                    .collect(Collectors.toList());
            return filteredResults;
        } catch (NumberFormatException e) {
            System.out.println("조회 기능을 건너뜁니다.");
            return null;
        }


    }
}
