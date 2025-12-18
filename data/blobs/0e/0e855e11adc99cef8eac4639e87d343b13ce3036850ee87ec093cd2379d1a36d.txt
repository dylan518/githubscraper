package com.camel.jpa;

import org.apache.camel.Exchange;
import org.apache.camel.Processor;

import com.fasterxml.jackson.databind.ObjectMapper;

public class BookBindProcess  implements Processor{

	public void process(Exchange exchange) throws Exception {

		ObjectMapper obj = new ObjectMapper();
		
		Book book= obj.readValue(exchange.getIn().getBody(String.class),Book.class);
		exchange.getIn().setBody(book);
	}

	

}
