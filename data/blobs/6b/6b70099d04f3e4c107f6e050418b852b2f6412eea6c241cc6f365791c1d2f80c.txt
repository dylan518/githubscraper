package get_request;

import base_url.DummyRestApiBaseUrl;
import io.restassured.response.Response;
import io.restassured.response.ValidatableResponse;
import org.junit.Test;
import pojo.DummyRestApiDataPojo;
import pojo.DummyRestApiResponseBodyPojo;
import utilities.ObjectMapperUtils;

import static io.restassured.RestAssured.*;
import static org.junit.Assert.assertEquals;

public class Get17  extends DummyRestApiBaseUrl {
    /*
Given

URL: https://dummy.restapiexample.com/api/v1/employee/1
When
   User sends GET Request
Then
   Status code is 200
 And

    "employee_name" is "Tiger Nixon"
And
    "employee_salary" is 320800
And
    "employee_age" is 61
And
    "status" is "success"
And
  "message" is "Successfully! Record has been fetched."

     */

    @Test
    public void post01(){
        spec.pathParams("first","employee","second", 1);
        DummyRestApiDataPojo innerData=
                new DummyRestApiDataPojo("Tiger Nixon",320800,61,"",1);

        DummyRestApiResponseBodyPojo expectedData=
                new DummyRestApiResponseBodyPojo("success",innerData,"Successfully! Record has been fetched.");
        Response response=given().spec(spec).when().get("/{first}/{second}");
        response.prettyPrint();

        DummyRestApiResponseBodyPojo actualData= ObjectMapperUtils.convertJsonToJava(response.asString(),DummyRestApiResponseBodyPojo.class);
        System.out.println("actualData: "+actualData);

        //1.Assert meth.
        assertEquals(200,response.statusCode());
        assertEquals(innerData.getEmployee_name(),actualData.getData().getEmployee_name());
        assertEquals(innerData.getEmployee_age(),expectedData.getData().getEmployee_age());
        assertEquals(innerData.getEmployee_salary(),expectedData.getData().getEmployee_salary());

        assertEquals(expectedData.getStatus(),actualData.getStatus());
        assertEquals(expectedData.getMessage(),actualData.getMessage());




    }






}
