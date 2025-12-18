public class Main {
    public static void main(String[] args) {
        // В экспедицию должна поехать бригада изыскателей.
        // Обязательно должен поехать бригадир и/или его заместитель.
        // Кроме того должен поехать геодезист и геолог.
        // Обязательно должен поехать один из двух водителей, но не оба одновременно.
        // Составьте логическое выражение для поездки в экспедицию и задайте начальные переменные так,
        // чтобы экспедиция состоялась (т.е. логическое выражение было истинным)
        boolean isMasterPresented = true;
        boolean isSamMasterPresented = true;
        boolean isGeodesistPresented = true;
        boolean isGeolodPresented = true;
        boolean isDriver1Presented = true;
        boolean isDriver2Presented = false;
        boolean isTourHappens = (isMasterPresented || isSamMasterPresented) && isGeodesistPresented && isGeolodPresented);
        System.out.println(isTourHappens);
    }
}