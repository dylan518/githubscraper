package day011;

public class VipCustomer extends Customer {
	private String consultantName;
	double saleRatio;	

	public VipCustomer() {}
	
	public VipCustomer(int id, String name, String cName) {
		super(id, name);
		customerGrade = "Vip";
		bonusRatio = 0.05;
		saleRatio = 0.1;
		this.consultantName = cName;
	}

	@Override
	public int calcPrice(int price) {
		bonusPoint += (int) price * bonusRatio;
		return price -= (int) price * saleRatio;
	}
		
	@Override
	public String customerInfo() {
		return super.customerInfo() + " 담당 상담원은 " + consultantName + "입니다.";
	}

	public String getConsultantName() {
		return consultantName;
	}

	public void setConsultantName(String consultantName) {
		this.consultantName = consultantName;
	}
}
