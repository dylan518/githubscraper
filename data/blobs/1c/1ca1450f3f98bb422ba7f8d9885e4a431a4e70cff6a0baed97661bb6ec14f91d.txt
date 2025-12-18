package p2;

import java.util.Scanner;

public class Toy {

	private Battery battery;
	private String text;
	private Scanner sc;
	
	public Toy(Battery battery) {
		this.battery = battery;
		text = "불편해? 불편하면 자세를 고쳐 앉아\n"+
				"짜장 안시켰다고요!!!\n"+
				"우리 유미는 뭐해!!! 오늘 서포터 진짜 왜 이래!!!!!\n";

		sc = new Scanner(text);
		
	}
	
	public void run() {
		if (sc.hasNextLine() == false) {
			sc = new Scanner(text);
		}
		if(sc.hasNextLine() && battery.getEnergy() >= 10) {
			String line = sc.nextLine();
			System.out.println(line);
			
			battery.useEnergy();
		}
		else {
			System.out.println("에너지 없음");
		}
	}
}
