package projectsoftt.quiz;

import javax.swing.*;

public class QuizManager {
    private static QuizManager instance; // Singleton instance
    private QuizManager() {}
    public static QuizManager getInstance() {
        if (instance == null) {
            instance = new QuizManager();
        }
        return instance;
    }    
    public static boolean isQuizAvailable() {
        return instance != null;
    }

    public void displayAllQuestions() {
        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

        Question question = QuestionFactory.createQuestion("Multiple Choice");
        question.displayQuestion(); 

        Question question1 = QuestionFactory.createQuestion("True/False");
        question1.displayQuestion(); 
    }
}
