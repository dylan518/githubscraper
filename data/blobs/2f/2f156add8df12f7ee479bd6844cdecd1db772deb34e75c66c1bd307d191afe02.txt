package test.main;

import java.util.HashMap;
import java.util.Map;

import org.json.JSONWriter;

/*
 *  run 했을때 아래와 같은 형식의 문자열이 출력되도록 해 보세요
 *  
 *  {
 *  	"name":"김구라",
 *  	"phone::{
 *  		"brand" : "apple",
 *  		"color":  "gold",
 *  		"regdate": 2015
 *  	}
 */
public class MainClass04 {
	public static void main(String[] args) {
		Map<String, Object>map=new HashMap<String, Object>();
		Map<String, Object>phone=new HashMap<String, Object>();
		phone.put("brand", "apple");
		phone.put("color", "gold");
		phone.put("regdate", 2015);
		map.put("name", "김구라");
		map.put("phone",phone);
		
		String result=JSONWriter.valueToString(map);
		
		System.out.println(result);
		
	}
}
