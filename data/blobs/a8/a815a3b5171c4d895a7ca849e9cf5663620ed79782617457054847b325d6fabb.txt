package Model;

public class NhanVienIntern extends modelNhanvien implements InterFaceEmplayee{

	


	private String ChuyenNganhMajors;
	private int Hockidanghoc;
	
	private String University_name;
	

	public NhanVienIntern(int iD, String fullName, int namSinh, int phone, String email, String employee_Type,
			String chuyenNganhMajors, int hockidanghoc, String university_name) {
		super(iD, fullName, namSinh, phone, email, employee_Type);
		ChuyenNganhMajors = chuyenNganhMajors;
		Hockidanghoc = hockidanghoc;
		University_name = university_name;
	}


	@Override
	public String Showinfo() {
		return "NhanVienIntern [ChuyenNganhMajors=" + ChuyenNganhMajors + ", Hockidanghoc=" + Hockidanghoc
				+ ", University_name=" + University_name + ", NamSinh=" + NamSinh + ", Showinfo()=" + Showinfo()
				+ ", getID()=" + getID() + ", getFullName()=" + getFullName() + ", getNamSinh()=" + getNamSinh()
				+ ", getPhone()=" + getPhone() + ", getEmployee_Type()=" + getEmployee_Type() + ", getEmployee_count()="
				+ ", getClass()=" + getClass() + ", hashCode()=" + hashCode() + ", toString()="
				+ super.toString() + "]";
	}







	

}
