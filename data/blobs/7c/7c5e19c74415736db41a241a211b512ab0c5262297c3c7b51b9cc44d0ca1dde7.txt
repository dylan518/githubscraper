package com.restwebservices.restwebservices.region;


import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.restwebservices.restwebservices.model.geojson.Geometry;
import com.restwebservices.restwebservices.model.geojson.Properties;

import java.io.FileOutputStream;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.HashSet;
import java.util.Set;

public class JacksonPojoToJson {
    public static void main(String[] args) throws IOException {
        //This commit is to sh
        // Create ObjectMapper
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);
        Properties post1 = new Properties();
        post1.setRegionID(150);
        post1.setRegionName("Beddington (_k)");
        Set<Geometry> geometry = new HashSet<>();
       /* Geometry geo1 = new Geometry("Multipolygon", BigDecimal.valueOf(5543750.560992400394753));
        Geometry geo2 = new Geometry("Multipolygon",BigDecimal.valueOf(571652.936367866466753));
        Geometry geo3 = new Geometry("Multipolygon",BigDecimal.valueOf(624923.597685541724786));


        geometry.add(geo1);
        geometry.add(geo2);
        geometry.add(geo3);
  */

        //post1.setGeometry(geometry);

        // Convert object to JSON string
        String postJson = mapper.writeValueAsString(post1);
        System.out.println(postJson);

        // Save JSON string to file
        FileOutputStream fileOutputStream = new FileOutputStream("region.json");
        mapper.writeValue(fileOutputStream, post1);
        fileOutputStream.close();
    }
}
