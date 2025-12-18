package ScoreManager;

import java.util.*; // usually should be in main class

/*
fields, constructor (when needed), mutators, accessors, utility methods
*/

public class ScoreManager {
  // declare field(s)
  private int[] scores = new int[25];

  // mutators
  public void setScores() {
    Random rand = new Random();
    final int MAX_SCORE = 100;
    final int MIN_SCORE = 0;

    for (int i = 0; i < 25; i++)
      scores[i] = rand.nextInt(MAX_SCORE - MIN_SCORE + 1) + MIN_SCORE;
  }

  // accessors
  public int[] getScores() {
    return scores;
  }

  public int getNumOfB(int[] grades) {
    int counter = 0;

    for (int i = 0; i < 25; i++) {
      if (grades[i] < 90 && grades[i] >= 80)
        counter++;
    }
    return counter;
  }

  // utility methods
  public int[] copyScores(int[] grades) {
    for (int i = 0; i < 25; i++)
      grades[i] = scores[i];

    return grades;
  }

  public void printScores(int[] grades) {
    for (int i = 0; i < 25; i++)
      System.out.print(grades[i] + " ");
  }
}
