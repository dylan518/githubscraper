package userInput;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

import mainApplication.MainUI;

public class CountryValidator implements Validator {

	/**
	 * This method is called by the ParametorsSelector whenever a user chooses new
	 * parameters from the drop down menus. It checks to see if the currently selected
	 * country is available for data fetching. If it is, the valid flag is turne on
	 * for the country parameter. If it is invalid, an error message is displayed.
	 */
	public void update() {
			
		MainUI gui = MainUI.getInstance();
		ParametersSelector params = gui.getParams();

		Boolean valid = true;
		try {
			valid = csvValidator(valid, params.getCountry().value);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		if (!valid) {
			params.setCountryValid(false);
			JFrame frame = new JFrame("Invalid Selection");
			JOptionPane.showMessageDialog(frame,
					"Data fetching is not permitted for " + params.getCountry().value + ". Please select another country.",
					"Invalid Selection", JOptionPane.ERROR_MESSAGE);
		} else {
			params.setCountryValid(true);
		}

	}

	/**
	 * csvValidator is a method that takes in certain parameters and returns the validity state of the selected years on the selected analysis.
	 * 
	 * @param valid a Boolean value to hold the result of the analysis
	 * @param country the country currently selected analysis type
	 * @return valid returns true of the parameters are valid, and false if they are not
	 * @throws IOException
	 */
	private boolean csvValidator(boolean valid, String country) throws FileNotFoundException {
		String filePath = "src/dataManagement/InvalidCountries.csv";
		Scanner x = new Scanner(new File(filePath));
		while (x.hasNextLine()) {
			String invalidCountry = x.nextLine();

			if (invalidCountry.equals(country)) {
				valid = false;
			}
		}
		x.close();
		return valid;
	}
}
