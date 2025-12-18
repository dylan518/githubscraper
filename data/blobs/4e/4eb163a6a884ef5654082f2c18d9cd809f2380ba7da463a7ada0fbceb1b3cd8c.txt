package parkinglot2;

import parkinglot2.observer.Observer;
import parkinglot2.parkingFeeStrategy.ParkingFeeStrategy;
import parkinglot2.parkingStrategy.ParkingStrategy;
import parkinglot2.vehicle.Vehicle;
import parkinglot2.vehicle.VehicleType;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ParkingLot {

    private static ParkingLot instance;
    private List<ParkingFloor> parkingFloorList;
    private ParkingStrategy parkingStrategy;
    private List<Observer> observers;
    private Map<Integer, ParkingFeeStrategy> feeStrategyMap;


    //Singleton design pattern
    //Private constructor
    private ParkingLot(int numberOfFloors, int capacityOfEachFloor, List<VehicleType> vehicleTypes){
        this.parkingFloorList = new ArrayList<>(numberOfFloors);
        this.observers = new ArrayList<>();
        feeStrategyMap = new HashMap<>();

        for(int i=0;i<numberOfFloors;i++){
            parkingFloorList.add(new ParkingFloor(i+1,capacityOfEachFloor, vehicleTypes.get(i)));
        }
    }

    public static ParkingLot getInstance(int numberOfFloors, int capacityOfEachFloor, List<VehicleType>vehicleTypeForEachFloor){
        if(instance == null){
            instance = new ParkingLot(numberOfFloors,capacityOfEachFloor,vehicleTypeForEachFloor);
        }

        return instance;
    }

    public List<ParkingFloor> getParkingFloorList() {
        return parkingFloorList;
    }

    public void setParkingStrategy(ParkingStrategy parkingStrategy) {
        this.parkingStrategy = parkingStrategy;
    }

    public Ticket parkVehicle(Vehicle vehicle){
      for(ParkingFloor floor : parkingFloorList){
          if(floor.getVehicleType() == vehicle.getVehicleType()){
              ParkingSpot spot = parkingStrategy.findSpot(floor.getParkingSpotList());

              if(spot != null){
                  spot.acquireSpot(vehicle);
                  Ticket ticket = new Ticket(vehicle.getLicenseNumber(),spot, floor.getFloorNumber());
                  notifyObservers("Vehicle "+ vehicle.getLicenseNumber() + "parked at spot "+spot.getId()+ " on floor "+floor.getFloorNumber());
                  System.out.println("Ticket generated and issued  "+ ticket.getTicketId());
                  return ticket;
              }
          }
      }
        System.out.println("Sorry, No parking spot available for vehicle "+ vehicle.getLicenseNumber());
      return null;
    }

    public double leaveVehicle(Ticket ticket, int hoursParked){
        ParkingSpot spot = ticket.getParkingSpot();
        spot.vacateSpot();
        int floorNumber = ticket.getFloorNumber();
        ParkingFloor floor = parkingFloorList.get(floorNumber-1);
        ParkingFeeStrategy parkingFeeStrategy = feeStrategyMap.get(floorNumber);
        double fee = parkingFeeStrategy.calculateFee(hoursParked);
        System.out.println("Parking fee for ticket "+ticket.getTicketId() + "is "+ fee);
        notifyObservers("Vehicle "+ ticket.getLicensePlate() + "left spot "+ spot.getId() + " on floor "+floor.getFloorNumber());
        return fee;

    }

    public void setFeeStrategyMap(int floorNumber, ParkingFeeStrategy parkingFeeStrategy) {
         feeStrategyMap.put(floorNumber,parkingFeeStrategy);
    }

    public void addObserver(Observer observer){
        observers.add(observer);
    }

    public void removeObserver(Observer observer){
        observers.remove(observer);
    }

    public void notifyObservers(String message){
        for(Observer observer : observers){
            observer.update(message);
        }
    }

}
