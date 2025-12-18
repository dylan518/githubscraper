package main;

import java.util.ArrayList;

public class DanhSachSinhVien {
	private ArrayList<SinhVien> danhSach;

	public DanhSachSinhVien() {
		this.danhSach = new ArrayList<SinhVien>();
	}

	public DanhSachSinhVien(ArrayList<SinhVien> danhSach) {

		this.danhSach = danhSach;
	}

	public void themSV(SinhVien sv) {
		this.danhSach.add(sv);
	}

	public void printDSSV() {
		for (SinhVien sinhVien : danhSach) {
			System.out.println(sinhVien);
		}
	}

	public boolean checkIsEmpty() {
		return this.danhSach.isEmpty();
	}

	public void clearAll() {
		this.danhSach.clear();
	}

	public int getSVQuantity() {
		return this.danhSach.size();
	}
}
