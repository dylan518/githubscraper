package AirportRooms;

import PeopleClasses.Passenger;
import TerminalObjects.SelfCheckIn;

import java.util.ArrayList;
import java.util.List;

public class MainLobby extends Room {
    List<SelfCheckIn> selfCheckIns;

    public MainLobby(String roomID) {
        super(roomID);
        this.selfCheckIns = new ArrayList<>();

        //we only need 6 self checkins to be in the lobby
        for (int i = 0; i < 7; i++) {
            this.selfCheckIns.add(new SelfCheckIn("kiosk" + (i +1)));
        }
    }


    @Override
    public int getCurrentCapacity() {
         return super.getCurrentCapacity();
    }


    public void MoveToTsA(TSA tsa, Passenger passenger) {


        if (passenger.isCheckedIn()) {
            tsa.addPassenger(passenger);
            System.out.println("Passenger " + passenger.getName() + " is moving to TSA.");
        }
    }

}
