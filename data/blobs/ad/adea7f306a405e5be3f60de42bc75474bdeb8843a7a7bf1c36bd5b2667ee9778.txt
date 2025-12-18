package sec2;

public class Bus {
	int no;
	int cnt;
	int money;
	
	 public Bus(int num) {
		this.no = num;
	 }
	
	 public void take(int money) {
		 this.money += money;
		 cnt++;
	 }	 
	 public void show() {
		 System.out.println("버스 번호: "+this.no+"버스 승객 :"+this.cnt+"버스 수입 :"+this.money);
	 }
}
