package com.github.savely03;

import com.beust.jcommander.JCommander;
import com.github.savely03.context.Calculator;
import com.github.savely03.service.CalculatorService;
import com.github.savely03.strategy.Definer;

public class Main {
    public static void main(String[] args) {
        CalculatorService calculatorService = new CalculatorService(new Calculator(), new Definer());
        System.out.println(calculatorService.invokeAndCalculate(createData(args)));
    }

    public static Data createData(String[] args) {
        Data data = new Data();
        JCommander.newBuilder().addObject(data).build().parse(args);
        return data;
    }
}