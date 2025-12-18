package sDET;

public class RemoveJunkFromString {

	public static void main(String[] args) 
	{
		String s= "12358 *(!!()#$ onkar kola!()!()@!";
		//regular expression= [^a-zA-Z0-9];
		
		s= s.replaceAll("[^a-zA-Z0-9]", "");
        System.out.println(s);
	}

}
