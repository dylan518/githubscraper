package vo.keep;

public class KeepVO {

	private int keepNo;
	private String keepHow;
	private int productNo;
	
	
	public KeepVO() {
		super();
	}


	public KeepVO(int keepNo, String keepHow, int productNo) {
		super();
		this.keepNo = keepNo;
		this.keepHow = keepHow;
		this.productNo = productNo;
	}


	public int getKeepNo() {
		return keepNo;
	}


	public void setKeepNo(int keepNo) {
		this.keepNo = keepNo;
	}


	public String getKeepHow() {
		return keepHow;
	}


	public void setKeepHow(String keepHow) {
		this.keepHow = keepHow;
	}


	public int getProductNo() {
		return productNo;
	}


	public void setProductNo(int productNo) {
		this.productNo = productNo;
	}

}