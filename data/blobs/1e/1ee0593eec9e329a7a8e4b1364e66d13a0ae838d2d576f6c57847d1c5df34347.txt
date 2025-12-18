package org.example;

import org.example.entities.Split;
import org.example.entities.SplitType;
import org.example.service.ExpenseService;
import org.example.service.UserService;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        UserService userService = new UserService();
        ExpenseService expenseService = new ExpenseService();

        Scanner sc = new Scanner(System.in);

        while (true){
            switch (sc.nextInt()){
                case 0:
                    String name = sc.next();
                    String number = sc.next();

                    userService.createUser(name,number);
                    break;

                case 1:
                    String desc = "BreakFast";

                    List<Split> allSplits  = new ArrayList<>();

                    Split split1 = new Split(userService.getUser("nikhil"),100);
                    Split split2 = new Split(userService.getUser("akhil"),200);
                    allSplits.add(split1);
                    allSplits.add(split2);

                    expenseService.createExpense(desc,300,"nikhil", SplitType.UNEQUAL,allSplits);
                    break;
            }

        }
    }
}