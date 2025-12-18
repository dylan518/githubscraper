package com.xworkz.interaction.boot;

import com.xworkz.interaction.bridge.Parents;
import com.xworkz.interaction.rules.Children;

public class ChildrenRunner {
	
	public static void main(String[] args) 
	{
		
		Parents ref = new Parents();
		ref.GoingOutWithFriends();
		ref.pocketMoneyRistrictions();
		ref. boysRistriction();
		ref.respectElders();
		ref.notToArguee();
		
		System.out.println("-----------------------------------------");
		
		Children ref1= new Parents();
		ref1.GoingOutWithFriends();
		ref1.pocketMoneyRistrictions();
		ref1.boysRistriction();
		ref1.respectElders();
		ref1.notToArguee();
}
}


