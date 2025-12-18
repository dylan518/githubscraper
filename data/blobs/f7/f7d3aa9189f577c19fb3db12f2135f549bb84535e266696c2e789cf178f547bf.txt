package com.product;

public class Main {

	public static void main(String[] args) {
		
//		int pid, String pname, int qty, double price
		Product p1 = new Product(101,"Kit-Kat",20,400);
		Product p2 = new Product(102,"Perk",100,1000);
		Product p3 = new Product(103,"Munch",50,500);
		Product p4 = new Product(104,"5-Star",25,250);
		Product p5 = new Product(105,"Sneakers",150,1500);
		
		LinkedList list = new LinkedList();
		
		list.insert(p1);
		list.insert(p2);
		list.insert(p3);
		list.insert(p4);
		list.insert(p5);
		
		list.display();
	}

}
