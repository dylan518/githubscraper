package renastech2.day1_Intro.day4;

import org.testng.Assert;
import org.testng.annotations.*;

public class c6_TestNGExamples {
    @BeforeClass
    public void setupClass(){
        System.out.println("Before class is running");
    }

    @AfterClass
    public void setUpAfterClass(){
        System.out.println("After class is running");
    }

    @BeforeMethod
    public void setUp(){
        System.out.println("before Method is running");
    }

    @AfterMethod
    public void closing(){
        System.out.println("After method is running");
    }
//this is giving them an order to run by priority so I am saying run this one 3rd
    @Test(priority = 3)
    public void TC1_1(){
        System.out.println("Test 1 is running");
    }

    @Test(priority = 1)
    public void TC3_3(){
        System.out.println("Test case 3 is running");

        String actualWord ="New York";
        String expectedWord= "Ohio";
//the below method is like using if else condition its like saying if actualword = expected word its true
        //which in this case is false because they are both two different words
        //REMEMBER THAT IF YOUR ASSERT=(METHOD).EQUALS-->=(CONDITION) FAILS THEN NOTHING ELSE AFTER INSIDE
        //YOUR CODE BLOCK WILL RUN {} "CODE HAS FAILED WILL NOT EXECUTE"**
        Assert.assertEquals(actualWord,expectedWord);
        System.out.println("code failed");

    }

    @Test(priority = 2)
    public void TC2_2(){
        System.out.println("Test2 is running");
        String name1 = "Alex";
        String name2 = "Alex";

        Assert.assertEquals(name1,name2);
    }


}
