package ch06;



class Car{
	private int speed;
	private boolean stop;
	
	public int getSpeed() {
		return speed;
	}
	
	public void setSpeed(int speed) {
		  if(speed<0) {
			  System.out.println("스피드는 0이상 이여야 합니다.");
		  }else {
			  this.speed = speed;
		  }
	}
	
	public boolean isStop() {
		return stop;
	}
	
	public void setStop(boolean stop) {
		this.stop = stop;
		if(stop==true) this.speed = 0;
	}
}

public class GetterSetter {

	public static void main(String[] args) {
		
		Car myCar = new Car();
		
		myCar.setSpeed(-50);
		System.out.println("현재 속도: "+myCar.getSpeed());
		

		myCar.setSpeed(60);
		System.out.println("현재 속도: "+myCar.getSpeed());
		

		if(!myCar.isStop()) {
			myCar.setStop(true);
		}
		System.out.println("현재 속도: "+myCar.getSpeed());
	}

}
