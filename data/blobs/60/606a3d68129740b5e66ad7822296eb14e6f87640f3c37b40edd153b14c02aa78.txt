package com.project.codesnippet.DBConnection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;

@Component
public class DBConnection {
    

    @Autowired(required = false)                            //Required declare it as false. By default it is True.
    SqlConnection sqlConnection;


    @Autowired(required = false)                          
    NoSqlConnection noSqlConnection;                


/*  
 !  If it is not declared as false, then Spring will feel its mandatory to create object of the Class but 
 ! as the ConditionOnProperty doesn't matches Spring is thus unable to create Object even though its Mandatory to create Object
 ?                                                          
 ?                      Hence it will Throw Error.
 ?                                                          Thus it is necessary to declare them as false
 */

    public DBConnection()
    {
        System.out.println("DB Connection Constructor Running");
    }


    @PostConstruct
    public void check()
    {
        System.out.println("NoSql connection value= "+noSqlConnection);
        System.out.println("Sql connection value= "+sqlConnection);
    }

    @PreDestroy
    public void devastate()
    {
        System.out.println("Destroy method");
    }
}
