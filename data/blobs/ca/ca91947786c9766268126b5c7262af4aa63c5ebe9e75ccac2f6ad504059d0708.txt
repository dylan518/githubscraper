package com.jdojo.common;


/*
* IMPORTANT!!!:
* For all reference type instance variable of an immutable class,
* When you receive an object's reference and store it in a reference type instance variable of a class,
* The client code may change the state of this object through the same reference.
* In such case, you must copy all necessary instance variables of the object. 
*/
public class IntHolderWrapper3{
	private final IntHolder holder;

	public IntHolderWrapper3(int value){
		this.holder = new IntHolder(value);
	}

	public IntHolderWrapper3(IntHolder ih){
		// MUST MAKE A COPY OF FORMAL PARAMATER FOR IMMUTABILITY
		this.holder = new IntHolder(ih.getValue());

		// ERROR: this.holder = ih;
		// By setting the reference value. You allow direct access to object from outside
		// as the client code will have the same reference value 

	}

	public IntHolder getHolder(){
		// Here we returned a copy of our reference type instance variable
		return new IntHolder(this.holder.getValue());
	}

	public int getValue(){
		return this.holder.getValue();
	}
}