package stringPrograms;

public class EvenLengthWordInSting {

	public static void main(String[] args) {

		String input = "he is coming there to see him";

		String[] stringArray = input.split(" ");

		for (int i = 0; i < stringArray.length; i++) {
			if (stringArray[i].length() % 2 == 0)
				System.out.println("even length word : " + stringArray[i]);
		}

	}

}
