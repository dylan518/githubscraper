import java.util.ArrayList;  
import java.util.List;  
import java.util.Scanner;  
import java.util.Timer;  
import java.util.TimerTask;  

class Question {  
    String question;  
    List<String> options;  
    int correctAnswer;  

    public Question(String question, List<String> options, int correctAnswer) {  
        this.question = question;  
        this.options = options;  
        this.correctAnswer = correctAnswer;  
    }  
}  

public class QuizApp {  
    private static List<Question> questions = new ArrayList<>();  
    private static int score = 0;  
    
    public static void main(String[] args) {  
        // Sample Questions  
        initializeQuestions();  
        runQuiz();  
        displayResults();  
    }  

    private static void initializeQuestions() {  
        questions.add(new Question("What is the capital of France?", List.of("1. Berlin", "2. Paris", "3. Madrid", "4. Rome"), 1));  
        questions.add(new Question("Which planet is known as the Red Planet?", List.of("1. Earth", "2. Mars", "3. Jupiter", "4. Venus"), 1));  
        questions.add(new Question("What is the largest ocean on Earth?", List.of("1. Atlantic Ocean", "2. Indian Ocean", "3. Arctic Ocean", "4. Pacific Ocean"), 3));  
        questions.add(new Question("What is the chemical symbol for Gold?", List.of("1. Au", "2. Ag", "3. Pb", "4. Fe"), 0));  
        questions.add(new Question("Who wrote 'Romeo and Juliet'?", List.of("1. Mark Twain", "2. Charles Dickens", "3. William Shakespeare", "4. J.K. Rowling"), 2));  
    }  

    private static void runQuiz() {  
        Scanner scanner = new Scanner(System.in);  
        
        for (int i = 0; i < questions.size(); i++) {  
            Question currentQuestion = questions.get(i);  
            System.out.println("Question " + (i + 1) + ": " + currentQuestion.question);  
            currentQuestion.options.forEach(System.out::println);  
            
            // Start timer for 10 seconds  
            Timer timer = new Timer();  
            TimerTask task = new TimerTask() {  
                @Override  
                public void run() {  
                    System.out.println("\nTime is up! Moving to the next question.");  
                    scanner.nextLine(); // Consume leftover input  
                }  
            };  
            timer.schedule(task, 10000); // 10 seconds  

            // Get user input  
            System.out.print("Your answer (1-4): ");  
            int userAnswer = -1;  
            try {  
                userAnswer = Integer.parseInt(scanner.nextLine()) - 1;  
                timer.cancel(); // Stop the timer if the user answered in time  
            } catch (NumberFormatException e) {  
                System.out.println("Invalid input!");  
            }  

            if (userAnswer == currentQuestion.correctAnswer) {  
                score++;  
                System.out.println("Correct!");  
            } else {  
                System.out.println("Incorrect. The correct answer was: " + (currentQuestion.correctAnswer + 1));  
            }  
            System.out.println();  
        }  
    }  

    private static void displayResults() {  
        System.out.println("Quiz completed! Your final score is: " + score + " out of " + questions.size());  
    }  
}
