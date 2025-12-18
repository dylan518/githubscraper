public class HotelApp {
    public static void main(String[] args) {
        HotelService valet = new Valet();
        HotelService houseKeeping = new HouseKeeping();
        HotelService cart = new Cart();

        FrontDesk frontDesk = new FrontDesk(valet, houseKeeping, cart);

        frontDesk.requestValet("ABC1234");
        frontDesk.requestHouseKeeping(106);
        frontDesk.requestCart(2); 
    }
}
