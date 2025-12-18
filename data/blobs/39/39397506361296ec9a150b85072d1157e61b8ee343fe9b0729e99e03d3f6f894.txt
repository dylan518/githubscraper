//Tugas no.2
public class PeminjamanDemo {
    public static void main(String[] args) throws Exception {
        Peminjaman pj = new Peminjaman();
        pj.id = 01;
        pj.namaMember = "Rizqi Hendra";
        pj.namaGame = "Pro Evolution Soccer 2023";
        pj.harga = 6000;
        pj.lamasewa = 2;
        pj.totalHarga();
        pj.cetakData();
    }
}
