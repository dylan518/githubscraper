package Homeworks.Homework13;

import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.annotations.Test;
import pojos.UserPojo;
import utilities.ObjectMapperUtils;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

public class Homework_13Put {
    //Write an automation test that will create a 'user' then read, update and delete the created user using the
    // "https://petstore.swagger.io/" document. (Create a classes for each request.)

    String url = "https://petstore.swagger.io/v2/user";

    @Test
    public void PutUser() {

        String strJson = """
                {
                     "id": 303,
                     "username": "shatha3",
                      "firstName": "shatha",
                      "lastName": "Alharbi",
                      "email": "shatha@hotmail.com",
                      "password": "98564",
                      "phone": "057894613",
                       "userStatus": 0
                      }
                                     """;


        UserPojo expectedData = ObjectMapperUtils.convertJsonToJava
                (strJson, UserPojo.class);
        System.out.println("expectedData = " + expectedData);

        Response response = given()
                .body(expectedData)
                .contentType(ContentType.JSON)
                .put(url+"/"+expectedData.getUsername());
        response.prettyPrint();

        response
                .then()
                .statusCode(200)
                .body("code",equalTo(response.getStatusCode())
                        , "type",equalTo("unknown")
                        ,"message",equalTo(expectedData.getId()+""));


}}
