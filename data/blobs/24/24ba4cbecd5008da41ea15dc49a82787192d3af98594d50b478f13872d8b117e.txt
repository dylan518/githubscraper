package loopAssignment;

public class ChocolateBox {

	int numberOfChocolatesPresent = 27;
	int totalChocolatesInBox = 63;

	void calculateChocolates() {

		while (numberOfChocolatesPresent <= totalChocolatesInBox)

		{
			if (numberOfChocolatesPresent < 63) {
				System.out.println("Total number of chocolates in the box : " + numberOfChocolatesPresent);

				numberOfChocolatesPresent += 5;
			} else

				System.out.println("Total number of chocolates in the box cannot be more that 63");

		}

	}
}
