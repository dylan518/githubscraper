package contoh;

import java.util.Scanner;

class Karyawan {
    private String nik;
    private String nama;
    private String jabatan;
    private int golongan;

    // Konstruktor
    public Karyawan(String nik, String nama, String jabatan, int golongan) {
        this.nik = nik;
        this.nama = nama;
        this.jabatan = jabatan;
        this.golongan = golongan;
    }

    // Getter dan setter untuk atribut karyawan
    public String getNik() {
        return nik;
    }

    public void setNik(String nik) {
        this.nik = nik;
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public String getJabatan() {
        return jabatan;
    }

    public void setJabatan(String jabatan) {
        this.jabatan = jabatan;
    }

    public int getGolongan() {
        return golongan;
    }

    public void setGolongan(int golongan) {
        this.golongan = golongan;
    }
}

class Manager extends Karyawan {
    private int kehadiran;
    private float tunjanganGolongan;
    private float tunjanganJabatan;
    private float tunjanganKehadiran;

    // Konstruktor
    public Manager(String nik, String nama, String jabatan, int golongan) {
        super(nik, nama, jabatan, golongan);
    }

    // Getter dan setter untuk atribut Manager
    public int getKehadiran() {
        return kehadiran;
    }

    public void setKehadiran(int kehadiran) {
        this.kehadiran = kehadiran;
    }

    public float tunjanganKehadiran(int hadir) {
        // Implementasikan perhitungan tunjangan kehadiran
        // Contoh sederhana: 100.000 per hari kehadiran
        tunjanganKehadiran = hadir * 100000;
        return tunjanganKehadiran;
    }

    public float tunjanganJabatan(String jabatan) {
        // Implementasikan perhitungan tunjangan jabatan
        // Contoh sederhana: Manager mendapat 5% dari gaji pokok
        float gajiPokok = 5000000; // Misalnya gaji pokoknya 5 juta
        if (jabatan.equalsIgnoreCase("Manager")) {
            tunjanganJabatan = 0.05f * gajiPokok;
        } else {
            tunjanganJabatan = 0; // Jabatan lain tidak mendapat tunjangan
        }
        return tunjanganJabatan;
    }

    public float tunjanganGolongan(int golongan) {
        // Implementasikan perhitungan tunjangan golongan
        // Contoh sederhana: 2% dari gaji pokok per golongan
        float gajiPokok = 5000000; // Misalnya gaji pokoknya 5 juta
        tunjanganGolongan = 0.02f * gajiPokok * golongan;
        return tunjanganGolongan;
    }

    public float gajiTotal() {
        // Implementasikan perhitungan gaji total
        float gajiPokok = 5000000; // Misalnya gaji pokoknya 5 juta
        float gajiTotal = gajiPokok + tunjanganKehadiran + tunjanganJabatan + tunjanganGolongan;
        return gajiTotal;
    }
}

