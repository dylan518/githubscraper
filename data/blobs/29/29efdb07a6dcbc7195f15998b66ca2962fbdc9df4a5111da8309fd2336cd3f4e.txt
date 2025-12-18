
public class HinhChuNhat {
	
	//khai baó biến
	float chieuDai;
	float chieuRong;
	
	//khai báo và định nghĩa hàm
	HinhChuNhat()
	{
		//code
		chieuDai = 0;
		chieuRong = 0;
	}
	
	HinhChuNhat(float n1, float n2)
	{
		//code
		chieuDai = n1;
		chieuRong = n2;
	}
	
	float tinhDienTich()
	{
		//code
		float dienTich = 0;
		dienTich = chieuDai * chieuRong;
		return dienTich;
	}
	
	float tinhChuVi()
	{
		//code
		float chuVi = 0;
		chuVi = (chieuDai + chieuRong) * 2;
		return chuVi;
	}

}
