package com.in28minutes.rest.webservices.restfulwebservices.filtering;

import org.springframework.http.converter.json.MappingJacksonValue;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FilteringController {
	
	@GetMapping("/filtering")
	public MappingJacksonValue filtering()
	{
		
		SomeBean someBean = new SomeBean("val1", "val2", "val3");
		
		MappingJacksonValue mappingJasksonValue = new MappingJacksonValue(someBean);
		 

		return mappingJasksonValue;
	}

}
