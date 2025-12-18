package com.bbva;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

// This class controls the flow of the queue and transaction
public class TellerWindow{ 
	// Atributes
	private int elapsedTime = 0;
	private List<Client> clients = new ArrayList<>();
	private boolean isAlexDone = false;
	private int alexWaitTime = 0;
	
	// Constructor
	public TellerWindow(List<Integer> transactions) {
		
		// Add all clients
		for(int i = 0; i < transactions.size() - 1 ; i++) {
			clients.add(new Client(transactions.get(i)));
		}
		
		// Add Alex at the end of the tail (he will be always the last element in the queue)
		clients.add(new Alex(transactions.get(transactions.size()-1)));
		System.out.println(clients);
	}
	
	// Methods
	public int calculateAlexWaitTime() {
		
		// Iterate over the collection  
		while(!clients.isEmpty() && !isAlexDone) {
			Iterator<Client> it = clients.iterator();
			while(it.hasNext() && !isAlexDone) {
				doTransacation(it.next(), it);
			}
		}
		return alexWaitTime;
	}
	
	public void doTransacation(Client client, Iterator<Client> iterator) {
		
		// Reduce the number of needed operations of a client and increase the elapsed time
		client.updateOperations();
		elapsedTime++;
		
		// Check if a client has remaining operations
		if(client.getRemainingOperations() <= 0) {
			// If so assign to client the elapsed time
			client.setWaitedTime(elapsedTime);
			
			// If Alex has completed all his operations then stop all the lops and obtain elapsed time units
			if(client instanceof Alex) {
				client.setWaitedTime(elapsedTime);
				System.out.println("Posición actual de Alex [" + client.currentposition + "] , operaciones realizadas [" 
			+ client.getCompletedOperations() + "] , operaciones restantes [" + client.getRemainingOperations() + "].");
				alexWaitTime = client.getWaitedTime();
				isAlexDone = true;
			}
			
			// If any other client has completed his/her operations then delete client from list
			iterator.remove();
		}else {
			// If any client including Alex complete a transaction and still having operation to do then send them to tha tail of queue
			sendToTail(client);
		}
		// Every time a transaction is completed update positions in queue
		updateQueuePosition();
	}
	
	public void sendToTail(Client client) {
		
		// Send a client to tail of queue
		client.setCurrentePosition(clients.size() - 1);
	}
	
	public void updateQueuePosition() {

		// Iterate over collection
		Iterator<Client> it = clients.listIterator();
		while(it.hasNext()) {
			Client client = it.next();
			// Display Alex tracking through the queue
			if(client instanceof Alex) {
				System.out.println("Posición actual de Alex [" + client.currentposition + "] , operaciones realizadas [" 
			+ client.getCompletedOperations() + "] , operaciones restantes [" + client.getRemainingOperations() + "].");
			}
			// Make clients go forward in the queue
			client.goForward();
		}
	}
}