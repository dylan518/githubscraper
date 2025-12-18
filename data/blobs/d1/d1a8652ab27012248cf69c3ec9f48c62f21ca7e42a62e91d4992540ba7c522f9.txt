package myobj.rpsgame;

import java.util.InputMismatchException;
import java.util.Scanner;

public class RockPaperScissors {
	ScoreFileManager file = new ScoreFileManager();
	
	private String scissor = "가위";
	private String rock = "바위";
	private String paper = "보";
	
	private int win;
	private int draw;
	private int lose;
	
	private int[] score = new int[3];
	
	// 플레이 후 전적를 저장
	private void saveScoreResult() {
		win = score[0];
		draw = score[1];
		lose = score[2];
	}
	
	// 파일에서 불러온 전적를 적용
	private void playScoreResult() {
		score[0] = win;
		score[1] = draw;
		score[2] = lose;
	}
	
	// 플레이어턴 동작 메서드
	private String userTurn() {
		Scanner sc = new Scanner(System.in);
		int userInput;
		
		while (true) {
			try {
				System.out.println("##### 플레이어의 선택 #####\n[[1.가위][2.바위][3.보]]");
				System.out.print(">>");
				userInput = sc.nextInt();

				switch (userInput) {
				case 1:
					return scissor;
				case 2:
					return rock;
				case 3:
					return paper;
				default :
					System.out.println("[ERROR]입력이 잘못되었습니다.");	
				}
				break;
			} catch (InputMismatchException e) {
				sc.nextLine();
				System.out.println("숫자가 아닌 문자를 입력했습니다.");
			}
		}
		return null;
	}
	
	// 컴퓨터턴 동작 메서드
	private String computerTurn() {
		int[] rps = {1, 2, 3};
		
		int computerInput = rps[(int)(Math.random() * 3)];
		
		switch (computerInput) {
			case 1 :
				System.out.printf("컴퓨터는 '%s'를 선택했습니다.\n", scissor);
				return scissor;
			case 2 :
				System.out.printf("컴퓨터는 '%s'를 선택했습니다.\n", rock);
				return rock;
			case 3 :
				System.out.printf("컴퓨터는 '%s'를 선택했습니다.\n", paper);
				return paper;
		}
		return null;
	}
	
	// 승패확인을 위한 비교 메서드
	private String compare(String userHand, String computerHand) {
		if (userHand.equals(computerHand)) {
			return "draw";
		}
		if (userHand.equals(scissor) ) {
			if (computerHand.equals(rock)) {
				return "lose";
			} else {
				return "win";
			}
		} else if (userHand == rock) {
			if (computerHand == paper) {
				return "lose";
			} else {
				return "win";
			}
		} else {
			if (computerHand == scissor) {
				return "lose";
			} else {
				return "win";
			}
		}
	}

	// 게임플레이 동작 메서드
	public void play() {
		String result = compare(userTurn(), computerTurn());
		
		switch (result) {
			case "win" :
				System.out.println("\n당신이 이겼습니다!!\n");
				win++;
				System.out.println("당신이 이긴 횟수 : " + win);
				break;
			case "draw" :
				System.out.println("\n비겼습니다\n");
				draw++;
				System.out.println("당신이 비긴 횟수 : " + draw);
				break;
			case "lose" :
				System.out.println("\n당신은 패배했습니다...\n");
				lose++;
				System.out.println("당신이 패배한 횟수 : " + lose);
				break;
		}
	}
	
	// 전적을 출력하기위한 메서드
	public void printScore() {
		playScoreResult();
		System.out.printf("\n현재까지의 전적\nWin[%d] Draw[%d] Lose[%d]\n\n", score[0], score[1], score[2]);
	}
	
	// 플레이 전적 저장 메서드
	public void saveScore() {
		playScoreResult();
		System.out.println("[NOTICE]전적을 저장중입니다...");
		file.scoreSave(score);
	}
	
	// 파일로부터 전적을 불러오는 메서드
	public void readScore() {
		System.out.println("[NOTICE]전적을 불러오고 있습니다...");
		if(file.scoreRead() == null) {
			System.out.println("### 초기데이터로 전환합니다. ###");
			resetScore();
		} else {
			System.out.println("[NOTICE]전적을 성공적으로 불러왔습니다.\n");
			score = file.scoreRead();
			saveScoreResult();
		}
	}
	
	// 초기데이터로 변경을 위한 메서드
	public void resetScore() {
		win = 0;
		draw = 0;
		lose = 0;
		playScoreResult();
		file.resetScore();
	}
}
