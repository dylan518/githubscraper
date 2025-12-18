package com.damlaerismis;

import java.util.ArrayList;
import java.util.List;

public class GiyimManager {
	
	private final String marka="marka";
    private String model;
    private String beden;
    private int stokSayisi;
    private double fiyat;
    
    
	public GiyimManager(String model, String beden, int stokSayisi, double fiyat) {
		super();
		this.model = model;
		this.beden = beden;
		this.stokSayisi = stokSayisi;
		this.fiyat = fiyat;
	}
	
	
	public void bedenListesi() {
		List<String> bedenler = new ArrayList<String>();
		bedenler.add("small");
		bedenler.add("medium");
		bedenler.add("large");
		bedenler.add("xlarge");
	}
	
	public GiyimManager() {
		super();
	}
	public void stokEkle(int gelenStok) {
		 stokSayisi+= gelenStok;
	}
	public void stokAzalt(int satis) {
		stokSayisi -= satis;
	}


	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public String getBeden() {
		return beden;
	}

	public void setBeden(String beden) {
		this.beden = beden;
	}

	public int getStokSayisi() {
		return stokSayisi;
	}

	public void setStokSayisi(int stokSayisi) {
		this.stokSayisi = stokSayisi;
	}

	public double getFiyat() {
		return fiyat;
	}

	public void setFiyat(double fiyat) {
		this.fiyat = fiyat;
	}

	public String getMarka() {
		return marka;
	}
    
    

}
