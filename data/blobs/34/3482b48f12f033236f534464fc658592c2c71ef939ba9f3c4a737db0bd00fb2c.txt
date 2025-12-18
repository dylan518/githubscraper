package pl.edu.wszib.java;

public class PackagePresenter {
    public PackagePresenter() {
        System.out.println("raz dwa trzy");
    }

    public void showPackage() {
        System.out.println("To jest obiekt klasy " + this.getClass().getSimpleName() + "," + "w pakiecie " + this.getClass().getPackageName());
    }

    public static void main(String[] args) {
        PackagePresenter packagePresenter = new PackagePresenter();
        packagePresenter.showPackage();
    }
}
