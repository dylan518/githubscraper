/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
lick nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package csc229.csc229_final_hw;
import csc229.csc229_final_hw.Plane;
import java.util.*;
import java.lang.Math;
import java.time.LocalDateTime;

/**
 *
 * @author tonypittella
 */
public class Airport {
    //create the 4 runways, used the 4 cardinal directions
    private Queue<String> northRunway = new LinkedList<>();
    private Queue<String> southRunway = new LinkedList<>();
    private Queue<String> eastRunway = new LinkedList<>();
    private Queue<String> westRunway = new LinkedList<>();
    //the queue of all planes
    private Queue<String> allPlanes = new LinkedList<>();

    //need the info from the Plane class
    public void assignRunway(LocalDateTime arrivalTime, String departurePoint,String planeID, String destination) {
        //create random int between 1- 100 to act as percentage
        int ranPercent = (int) (Math.random() * 100) + 1;

        // acts as check for the 70%
        if (ranPercent <= 70) {
            // get random int 0-3 to act as the runway choice 
            int ranDirection = (int) (Math.random() * 4); 
            //create a switch case to add the correct runway to direction
            //add planeID and destination to the disired runway
            switch (ranDirection) {
                case 0:
                    //adds to the north runway
                    northRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    //adds to the overal queue
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                    break;
                case 1:
                    southRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                    break;
                case 2:
                    eastRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                    break;
                case 3:
                    westRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                    break;
                }
        //acts as the check for 20%
        } else if (ranPercent <= 90) {
            //20% has two runways to choose from so it needs 2 random directions
            int ranDirection1 = (int) (Math.random() * 4);
            int ranDirection2 = (int) (Math.random() * 4);
            
            //check if the 2 runways are the same
            //if same redo random direction
            while (ranDirection2 == ranDirection1) {
                ranDirection2 = (int) (Math.random() * 4);
            }
            //if random direction 1 or R.D. 2 equal 0(north) then compair size
            if (ranDirection1 == 0 || ranDirection2 == 0) {
            // see if north is shorter then the rest if so add to its runway 
                if (northRunway.size() <= southRunway.size() && northRunway.size() <= eastRunway.size() && northRunway.size() <= westRunway.size()) {
                    northRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
            // remove north and see if south is smaller then east and west
                } else if (southRunway.size() <= eastRunway.size() && southRunway.size() <= westRunway.size()) {
                    southRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
            // remove north and south. compare east size to west size       
                } else if (eastRunway.size() <= westRunway.size()) {
                    eastRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
            // only west is left so add to it runway        
                } else {
                    westRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                }//end inner if
            // if R.D.1 or 2 are 1(south) 
            } else if (ranDirection1 == 1 || ranDirection2 == 1) {
                //see if south runway is the smallest, if so then add
                if( southRunway.size() <= northRunway.size() && southRunway.size() <= eastRunway.size() && southRunway.size() <= westRunway.size()) {
                    southRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                //same logic as above    
                 } else if (northRunway.size() <= eastRunway.size() && northRunway.size() <= westRunway.size()) {
                    northRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                 //same logic as above    
                }else if (eastRunway.size() <= westRunway.size()) {
                    eastRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                } else {
                    westRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                }  //end inner if     
            // if R.D.1 or 2 are 2(east)     
            } else if (ranDirection1 == 2 || ranDirection2 == 2){
                //see if east runway is the smallest, if so then add
                if( eastRunway.size() <= northRunway.size() && eastRunway.size() <= southRunway.size() && eastRunway.size() <= westRunway.size()) {
                   eastRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                   allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                //same logic as above    
                 } else if (westRunway.size() <= northRunway.size() && westRunway.size() <= southRunway.size()) {
                    westRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                 //same logic as above    
                }else if (northRunway.size() <= southRunway.size()) {
                    northRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                } else {
                    southRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                }  //end inner if
            // and finally if R.D.1 or 2 are 3(west)    
            }else if (ranDirection1 == 3 || ranDirection2 == 3){
                //see if east runway is the smallest, if so then add
                if( westRunway.size() <= northRunway.size() && westRunway.size() <= southRunway.size() && westRunway.size() <= eastRunway.size()) {
                   westRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                   allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                //same logic as above    
                 } else if (eastRunway.size() <= northRunway.size() && eastRunway.size() <= southRunway.size()) {
                    eastRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                 //same logic as above    
                }else if (northRunway.size() <= southRunway.size()) {
                    northRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                } else {
                    southRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                }  //end inner if 
            }
            
        //checks everything else, 10%
        } else {
            //10% has 3 runways
            int ranDirection1 = (int) (Math.random() * 4); 
            int ranDirection2 = (int) (Math.random() * 4); 
            int ranDirection3 = (int) (Math.random() * 4);
            
            //check to make sure they are not the same runways
            while (ranDirection2 == ranDirection1 || ranDirection2 == ranDirection3) {
                ranDirection2 = (int) (Math.random() * 4);
            }
            while (ranDirection3 == ranDirection1 || ranDirection3 == ranDirection2) {
                ranDirection3 = (int) (Math.random() * 4);
            }
            // if R.D.1 2 or 3  are 0(north) 
            if (ranDirection1 == 0 || ranDirection2 == 0 || ranDirection3 == 0) {
            // see if north is shorter then the rest if so add to its runway 
                if (northRunway.size() <= southRunway.size() && northRunway.size() <= eastRunway.size() && northRunway.size() <= westRunway.size()) {
                    northRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
            // remove north and see if south is smaller then east and west
                } else if (southRunway.size() <= eastRunway.size() && southRunway.size() <= westRunway.size()) {
                    southRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
            // remove north and south. compare east size to west size       
                } else if (eastRunway.size() <= westRunway.size()) {
                    eastRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
            // only west is left so add to it runway        
                } else {
                    westRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                }//end inner if
            // if R.D.1 2 or 3  are 1(south) 
            } else if (ranDirection1 == 1 || ranDirection2 == 1 || ranDirection3 == 1) {
                //see if south runway is the smallest, if so then add
                if( southRunway.size() <= northRunway.size() && southRunway.size() <= eastRunway.size() && southRunway.size() <= westRunway.size()) {
                    southRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                //same logic as above    
                 } else if (northRunway.size() <= eastRunway.size() && northRunway.size() <= westRunway.size()) {
                    northRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                 //same logic as above    
                }else if (eastRunway.size() <= westRunway.size()) {
                    eastRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                } else {
                    westRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                }  //end inner if     
            // if R.D.1 2 or 3 are 2(east)     
            } else if (ranDirection1 == 2 || ranDirection2 == 2 || ranDirection3 == 2){
                //see if east runway is the smallest, if so then add
                if( eastRunway.size() <= northRunway.size() && eastRunway.size() <= southRunway.size() && eastRunway.size() <= westRunway.size()) {
                   eastRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                   allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                //same logic as above    
                 } else if (westRunway.size() <= northRunway.size() && westRunway.size() <= southRunway.size()) {
                    westRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                 //same logic as above    
                }else if (northRunway.size() <= southRunway.size()) {
                    northRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                } else {
                    southRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                }  //end inner if
            // and finally if R.D.1 2 or 3 are 3(west)    
            }else if (ranDirection1 == 3 || ranDirection2 == 3 || ranDirection3 == 3){
                //see if east runway is the smallest, if so then add
                if( westRunway.size() <= northRunway.size() && westRunway.size() <= southRunway.size() && westRunway.size() <= eastRunway.size()) {
                   westRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                   allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                //same logic as above    
                 } else if (eastRunway.size() <= northRunway.size() && eastRunway.size() <= southRunway.size()) {
                    eastRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                 //same logic as above    
                }else if (northRunway.size() <= southRunway.size()) {
                    northRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                } else {
                    southRunway.add("Plane ID: " + planeID + ", Destination: " + destination);
                    allPlanes.add("Plane ID: " + planeID + ", Destination: " + destination);
                }  //end inner if 
            }
        }//end else
    }//end assign
    //the queue getters 
    public Queue getNorthRunPlanes() {
        return northRunway;
    }
    public Queue getSouthRunPlanes() {
        return southRunway;
    }
    public Queue getEastRunPlanes() {
        return eastRunway;
    }
    public Queue getWestRunPlanes() {
        return westRunway;
    }
    public Queue getAllPlanes() {
        return allPlanes;
    }
    //the printer
    public void printPlanes( Queue<String> queue) {
        for(String plane: queue){
            System.out.println(plane);
        }
    }
    
    public static void main(String[] args) {
    Airport airport = new Airport();
    LocalDateTime arrivalTime = LocalDateTime.now();
    Plane plane1 = new Plane("FLY123", "New York", LocalDateTime.now(), LocalDateTime.now().plusHours(2), "North");
    Plane plane2 = new Plane("DLT449", "Los Angeles", LocalDateTime.now(), LocalDateTime.now().plusHours(3), "South");
    Plane plane3 = new Plane("BLU293", "Boston",LocalDateTime.now(),LocalDateTime.now().plusHours(5), "East" );
    Plane plane4 = new Plane("TNY888", "San Diego",LocalDateTime.now(),LocalDateTime.now().plusHours(7), "West" );
    Plane plane5 = new Plane("AIR222", "Pensicola", LocalDateTime.now(), LocalDateTime.now().plusHours(1), "South");
    Plane plane6 = new Plane("UNT483", "Falon", LocalDateTime.now(), LocalDateTime.now().plusHours(4), "East");
    Plane plane7 = new Plane("SPR243", "Olympia",LocalDateTime.now(),LocalDateTime.now().plusHours(2), "West" );
    Plane plane8 = new Plane("PLN636", "Woodstock",LocalDateTime.now(),LocalDateTime.now().plusHours(3), "North" );
    

    airport.assignRunway(plane1.getArivalTime(), plane1.getDeparturePoint(), plane1.getPlaneID(), plane1.getDestination());
    airport.assignRunway(plane2.getArivalTime(), plane2.getDeparturePoint(), plane2.getPlaneID(), plane2.getDestination());
    airport.assignRunway(plane3.getArivalTime(), plane3.getDeparturePoint(), plane3.getPlaneID(), plane3.getDestination());
    airport.assignRunway(plane4.getArivalTime(), plane4.getDeparturePoint(), plane4.getPlaneID(), plane4.getDestination());
    airport.assignRunway(plane5.getArivalTime(), plane5.getDeparturePoint(), plane5.getPlaneID(), plane5.getDestination());
    airport.assignRunway(plane6.getArivalTime(), plane6.getDeparturePoint(), plane6.getPlaneID(), plane6.getDestination());
    airport.assignRunway(plane7.getArivalTime(), plane7.getDeparturePoint(), plane7.getPlaneID(), plane7.getDestination());
    airport.assignRunway(plane8.getArivalTime(), plane8.getDeparturePoint(), plane8.getPlaneID(), plane8.getDestination());
    
    
    //prints runways
    System.out.println("North Runway:");
    airport.printPlanes(airport.getNorthRunPlanes());
    System.out.println("----------------------------------");
    System.out.println("South Runway:");
    airport.printPlanes(airport.getSouthRunPlanes());
    System.out.println("----------------------------------");
    System.out.println("East Runway:");
    airport.printPlanes(airport.getEastRunPlanes());
    System.out.println("----------------------------------");
    System.out.println("West Runway:");
    airport.printPlanes(airport.getWestRunPlanes());
    System.out.println("----------------------------------");
    System.out.println("The Plane Queue:");
    airport.printPlanes(airport.getAllPlanes());
    
    }
    
    
}//end airport


