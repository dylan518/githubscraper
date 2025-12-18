/*

Austin Wang
Mr. Fox
AP Computer Science 30
25 October 2024


Leap Year Calculator
Asks the user to input a year and returns wether or not it is a leap year. 

 */


import java.lang.Math;
public class App {
    public static void main(String[] args) throws Exception {
        LeapYearMethods LYM = new LeapYearMethods();
        LYM.getInput();
        LYM.finish(LYM.conditionals());  
    }
}
