package Random;

import java.util.Scanner;
import java.util.Random;
import java.lang.Math;


public class NumGuesserGame {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rand = new Random();

        System.out.println("Welcome to Guess the Number Game!");

        boolean shouldRun = true;
        Integer firstNum = null;
        Integer secondNum = null;
        Integer minNum = null;
        Integer maxNum = null;
        Integer lastNum = null;
        Integer randomNumber = null;
        Integer attempts = null;

        while (shouldRun) {
            System.out.print("\nWhat mode you want to play: ");
            switch (input.nextLine().trim().toLowerCase()) {

                case "classic" -> {
                    attempts = 3;
                    minNum = 1;
                    maxNum = 10;
                    randomNumber = rand.nextInt(maxNum) + minNum;

                    shouldRun = false;
                }

                case "normal" -> {
                    System.out.print("\nWith how many digits you wanna play: ");

                    String digits = input.nextLine().trim();

                    if (numCheck(digits) != null) {
                        minNum = 1;
                        maxNum = (int) Math.pow(10, Integer.parseInt(digits)) - 1;
                        attempts =  (maxNum - minNum) / 3;
                        randomNumber = rand.nextInt(maxNum) + minNum;

                        shouldRun = false;
                    }
                }

                case "custom" -> {
                    System.out.print("\nSet a range \"num - num\": ");

                    String nums = input.nextLine();
                    String[] idk = nums.trim().split("[,-]");

                    firstNum = numCheck(idk[0].trim());
                    secondNum = numCheck(idk[1].trim());

                    if (firstNum != null && secondNum != null) {
                        minNum = Math.min(firstNum, secondNum);
                        maxNum = Math.max(firstNum, secondNum);
                        attempts =  (maxNum - minNum) / 3;
                        randomNumber = rand.nextInt(maxNum - minNum + 1) + minNum;

                        shouldRun = false;
                    }
                }

                default -> System.out.println("Enter valid mode name");

            }
        }

        final String randomNumberStr = Integer.toString(randomNumber);
        System.out.println("Your goal is to guess number between " + minNum + " - " + maxNum + "!");

        while (true) {
            System.out.print("Guess number: ");
            String guess = input.nextLine().trim();

            if (guess.equals(randomNumberStr)) {
                System.out.println("You won! The number was " + randomNumber);
                break;
            }

            if (guess.equals("hint")) {
                if (attempts > 0) {
                    if (lastNum == null) {
                        System.out.println("You haven't guessed yet dumbass!");
                    } else {
                        attempts -= 1;
                        System.out.println(lastNum > randomNumber ? "Lower" : "Upper");
                    }
                } else {
                    System.out.println("You don't have any hints left!");
                }

            } else {
                lastNum = Integer.valueOf(guess);

                if (numCheck(guess) != null) {
                    System.out.println("You guessed wrong! Try again...");
                }
            }
        }
    }


    public static Integer numCheck(String str) {
        try {
            return Integer.parseInt(str);
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Next time enter a number.");
            return null;
        }
    }
}
