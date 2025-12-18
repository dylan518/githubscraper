public class Calculation {
	//싱글톤 패턴
	private static final Calculation instance = new Calculation();
	//getter
	public static Calculation getInstance() {
		return instance;
	}
	//객체 생성 방어
	private Calculation() {}

	//기본 요금
	public int baseFee(int kWh) {

		//200이하 사용시 910원
		if(kWh<=200)
			return 910;
		//201~400 사용시 1600원
		else if(kWh>=201 && kWh<=400)
			return 1600;
		//400이상 사용시 7300원
		else
			return 7300;
	}

	//1,2,3단계 요금 초기화
	double firstStageFee = 0;
	double secondStageFee = 0;
	double thirdStageFee = 0;

	//전력량 요금(1원 미만 절사)
	public int electricityFee(int kWh) {

		//200이하 사용시 1kWh당 120원
		if(kWh<=200) {
			firstStageFee = (double)120*kWh;
			return (int)firstStageFee;
		}
		//201~400 사용시 1kWh당 214.6원
		else if(kWh>=201 && kWh<=400) {
			firstStageFee = (double)120*200;
			secondStageFee = (double)214.6*(kWh-200);
			return (int)(firstStageFee + secondStageFee);
		}
		//400이상 사용시 1kWh당 307.3원
		else {
			firstStageFee = (double)120*200;
			secondStageFee = (double)213.6*200;
			thirdStageFee = (double)307.3*(kWh-400);
			return (int)(firstStageFee + secondStageFee + thirdStageFee);
		}
	}

	//기후환경 요금
	public int climateEnvironmentFee(int kWh) {

		//사용시 1kWh당 9원
		return kWh * 9;
	}

	//전기 요금(기본 요금 + 전력량 요금 + 기후환경 요금)
	public int totalElectricityFee(int kWh) {

		return (int)(instance.baseFee(kWh)+
				instance.electricityFee(kWh)+
				instance.climateEnvironmentFee(kWh));
	}

	//전력기반기금
	public int electricityInfrastructureFund(int kWh) {

		//전기요금 * 3.7% (10원미만절사)
		return (int)(instance.totalElectricityFee(kWh)*37/1000/10)*10;
	}


	//부가 가치세
	public int valueAddedTax(int kWh) {

		// 전기요금 * 10% (1원미만 반올림)
		return (int)Math.round(instance.totalElectricityFee(kWh)/10);
	}

	//청구 금액
	public int totalCharge(int kWh) {
		
		//전기 요금(기본 요금 + 전력량 요금 + 기후환경 요금) + 전력기반기금 + 부가 가치세 (10원 미만 절사)
		return (int)(instance.totalElectricityFee(kWh)+
				instance.electricityInfrastructureFund(kWh)+
				instance.valueAddedTax(kWh)
				/10)*10;
	}
}
