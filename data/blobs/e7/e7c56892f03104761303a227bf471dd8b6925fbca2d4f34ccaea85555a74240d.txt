package com.cognyte.examservice.mathgenerator.service;

import com.cognyte.examservice.QuestionGenerator;
import com.cognyte.examservice.models.Question;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

@Service("math")
public class MathQuestionGenerator implements QuestionGenerator {
    @Override
    public Question getRandomQuestion() {
        Random rand = new Random();
        int a = rand.nextInt(10);
        int b = rand.nextInt(10);
        //return new Question("%d + %d".formatted(a,b),String.valueOf(a+b));
        return Question.builder().question(a+ " + "+b+ "=?")
                .answer(String.valueOf(a+b)).build();
    }

    @Override
    public List<Question> getRandomQuestions(int amount) {
        ArrayList<Question> questions = new ArrayList<>();
        for (int i = 0; i<amount; i++) {
            questions.add(getRandomQuestion());
        }
        return questions;
    }
}
