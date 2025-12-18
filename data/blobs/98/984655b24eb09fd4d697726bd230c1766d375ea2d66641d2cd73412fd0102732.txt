package day0201.oopex.sample;

public class Tv {
	int inch; //기본값 0(따로 지정안했으면)
	int channel; //채널은 5~20번까지만 있음.
	int volume;
	boolean power; //기본값 false

	public Tv() {}

	public Tv(int inch, int channel, int volume, boolean power) {
		this.inch = inch;
		this.channel = channel;
		this.volume = volume;
		this.power = power;
	}

	public Tv(int inch) {
		this.inch = inch;
	}

	void power(){
		power = !power;
	}//power
	
	void setChannel(int c){
		if(c >=5 && c <=20) {
			channel = c;
		}else {
			System.out.println("없는 채널입니다.");
			System.out.println("기존 채널이 유지됩니다.");
		}
		System.out.println("현재 체널은 " + channel + "입니다.");
	}//setChannel
	
	void upChannel(){
		if(channel + 1 > 20) {
			channel = 5;
		}else {
			channel++;
		}
		System.out.println("현재 체널은 " + channel + "입니다.");
	}//upChannel
	
	void downChannel(){
		if(channel - 1 < 5) {
			channel = 20;
		}else {
			channel--;
		}
		System.out.println("현재 체널은 " + channel + "입니다.");
	}//downChannel
}
