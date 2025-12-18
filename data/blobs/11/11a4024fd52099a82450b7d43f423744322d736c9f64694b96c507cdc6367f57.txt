package utils;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import com.google.gson.JsonArray;

public class JsonManager extends MainClass {
	private static FileReader fileReader;
	private static JSONObject jsonObject;
	
public static JSONArray readDataFromJSON(String filePath) {
	Object object = null;
	JSONParser jsonParser = new JSONParser();//parse the json data
	try {
		fileReader = new FileReader(filePath);//load the json file
	} catch (FileNotFoundException exception) {
	}
	try {
		object = jsonParser.parse(fileReader);//parses the loaded json file and saved in normal object

	} catch (IOException readException) {
	
	} catch (ParseException parseException) {
		
	}
	JSONArray jsonArray = (JSONArray) object;//now the object is typecasting into jsonarray means converting from object to jsonarray 
//	logger.info("Read data from JSON");
	return jsonArray;
}

/** A method to fetch data from JSON */
public static JSONObject fetchData(String JSONPath, String category) { 
	JSONArray credentialsList = readDataFromJSON(workingDir + property.getProperty(JSONPath));
	for (int i = 0; i < credentialsList.size(); i++) {
		jsonObject = (JSONObject) credentialsList.get(i);
		if (jsonObject.keySet().contains(category)) {
			jsonObject = (JSONObject) jsonObject.get(category);
			break;
		}
	}
	return jsonObject;
}
	
}
