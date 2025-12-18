package Exceptions;
//Throws java throws keyword is used to declare an exception.
//This gives an information to the programmer that there might be an exception so its better to be prepared with a try catch block!

class AdultCheckException extends Exception{
	@Override
    public String toString()   //function called when a user defined exception object is printed sysout(e)
    {
    	return "Not an Adult";
    }
}

public class ThrowVsThrowsExample {

    public static int agecal(int age) throws AdultCheckException{
        if (age<18){
            throw new AdultCheckException();
        }
        int result = age;
        return result;
    }
    
    public static void main(String[] args) {
        
        try{
            int age = agecal(10);
            System.out.println(age);
        }
        catch(Exception e){
            System.out.println(e);
            
        }
    }
}