package ejercicio1.pkg5;

import java.util.ArrayList;
import java.util.List;

public class SellTickets {

    public static void main(String[] args) {
        // Creamos algunas áreas de asientos
        SeatArea area1 = new SeatArea("Principal", 200, 25.0, 17.5);
        SeatArea area2 = new SeatArea("PalcoB", 40, 70.0, 40.0);
        SeatArea area3 = new SeatArea("Central", 400, 20.0, 14.0);

        // Creamos una lista de áreas de asientos
        List<SeatArea> areas = new ArrayList<>();
        areas.add(area1);
        areas.add(area2);
        areas.add(area3);

        // Simulamos la venta de tickets
        sellTicket(areas, "Principal", "JuanDiego", true); // NormalTicket
        sellTicket(areas, "PalcoB", "Leydi", false); // SubscriberTicket
        sellTicket(areas, "Central", "Pedro", true); // NormalTicket
        sellTicket(areas, "Principal", "Carlitos", false); // SubscriberTicket
        sellTicket(areas, "Central", "Nathan", true); // NormalTicket

        // Mostramos los tickets vendidos
        for (SeatArea area : areas) {
            System.out.println("Area: " + area.getName());
            for (Ticket ticket : area.getTickets()) {
                System.out.println("  " + ticket.getClientName() + " - " + ticket.getPrice());
            }
        }
    }

    public static void sellTicket(List<SeatArea> areas, String areaName, String clientName, boolean isNormal) {
        // Buscamos el área de asientos correspondiente
        SeatArea area = findArea(areas, areaName);
        if (area == null) {
            System.out.println("Area no encontrada");
            return;
        }

        // Verificamos si el área está llena
        if (area.isFull()) {
            System.out.println("Area llena");
            return;
        }

        // Creamos el ticket correspondiente
        Ticket ticket;
        if (isNormal) {
            ticket = new NormalTicket(area, clientName);
        } else {
            ticket = new SubscriberTicket(area, clientName);
        }

        // Agregamos el ticket a la lista de tickets de la área
        area.addTicket(ticket);

        // Incrementamos la cantidad de tickets vendidos
        area.sellTicket();
    }

    public static SeatArea findArea(List<SeatArea> areas, String areaName) {
        for (SeatArea area : areas) {
            if (area.getName().equals(areaName)) {
                return area;
            }
        }
        return null;
    }
}

class Ticket {
    private int identity;
    private SeatArea zone;
    private String clientName;
    double price;

    public Ticket(SeatArea zone, String clientName) {
        this.zone = zone;
        this.clientName = clientName;
    }

    public String getClientName() {
        return clientName;
    }

    public double getPrice() {
        return price;
    }
}

class NormalTicket extends Ticket {
    public NormalTicket(SeatArea zone, String clientName) {
        super(zone, clientName);
        this.price = zone.getNormalPrice();
    }
}

class SubscriberTicket extends Ticket {
    public SubscriberTicket(SeatArea zone, String clientName) {
        super(zone, clientName);
        this.price = zone.getSubscriberPrice();
    }
}

class ReducedTicket extends Ticket {
    public ReducedTicket(SeatArea zone, String clientName) {
        super(zone, clientName);

    }
}

class SeatArea {
    private String name;
    private int numLocalities;
    private double normalPrice;
    private double subscriberPrice;
    private int soldTickets;
    private List<Ticket> tickets;

    public SeatArea(String name, int numLocalities, double normalPrice, double subscriberPrice) {
        this.name = name;
        this.numLocalities = numLocalities;
        this.normalPrice = normalPrice;
        this.subscriberPrice = subscriberPrice;
        this.soldTickets = 0;
        this.tickets = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public boolean isFull() {
        return soldTickets >= numLocalities;
    }

    public void sellTicket() {
        soldTickets++;
    }

    public List<Ticket> getTickets() {
        return tickets;
    }

    public double getNormalPrice() {
        return normalPrice;
    }

    public double getSubscriberPrice() {
        return subscriberPrice;
    }

    public void addTicket(Ticket ticket) {
        tickets.add(ticket);
    }
}