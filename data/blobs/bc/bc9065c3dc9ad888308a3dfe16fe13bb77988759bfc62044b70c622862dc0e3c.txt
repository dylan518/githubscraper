/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

import java.io.File;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import logica.moneda;
import org.jdom2.Document;
import org.jdom2.Element;
import org.jdom2.JDOMException;
import org.jdom2.input.SAXBuilder;

/**
 *
 * @author JDEM_
 */
public class conexionDB {

    public static String obtenerStringCon(){
        String server = null ;
        String puerto = null;
        String integratedSecurity = null ;
        String dataBase = null;
        String TrustServerCertificate = null ;
        SAXBuilder builder = new SAXBuilder();
                File xmlFile = new File("C:\\Users\\JDEM_\\Documents\\xmlJava\\stringConDBGlobalWay.xml");
        try
    {
        //Se crea el documento a traves del archivo
        Document document = (Document) builder.build( xmlFile );
 
        //Se obtiene la raiz 'tablas'
        Element rootNode = document.getRootElement();
 
        //Se obtiene la lista de hijos de la raiz 'tablas'
        List list = rootNode.getChildren();
 
        //Se recorre la lista de hijos de 'tablas'
        for ( int i = 0; i < list.size(); i++ )
        {
            //Se obtiene el elemento 'tabla'
            Element tabla = (Element) list.get(i);
 

 
            //Se obtiene la lista de hijos del tag 'tabla'
            List lista_campos = tabla.getChildren();
                 server = tabla.getChildText("server");
                String server2 = tabla.getChildText("server");
                System.out.println(server2);
                puerto = tabla.getChildTextTrim("puerto");
                dataBase = tabla.getChildTextTrim("dataBase");
                integratedSecurity = tabla.getChildTextTrim("integratedSecurity");
                TrustServerCertificate = tabla.getChildTextTrim("TrustServerCertificate");
 
            //Se recorre la lista de campos
            
           System.out.println("jdbc:sqlserver://"+server+":"+puerto+";databasename="+dataBase+";integratedSecurity="+integratedSecurity+";TrustServerCertificate="+TrustServerCertificate+"");
        }
    }catch ( IOException io ) {
        System.out.println( io.getMessage() );
    }catch ( JDOMException jdomex ) {
        System.out.println( jdomex.getMessage() );
           
    }
        
       return "jdbc:sqlserver://"+server+":"+puerto+";databasename="+dataBase+";integratedSecurity="+integratedSecurity+";TrustServerCertificate="+TrustServerCertificate+"";
       
    }
    
    public static ResultSet ejecutarQueryConRS(String comandoSql) {
          
          Connection cn = null; // variable de conexion
          Statement st = null;  // variable de instruccion SQL
          ResultSet rs = null; // variable de registros o filas
          
          try {
            conexionDB objAppConfig = new conexionDB();
            String connectionUrl = objAppConfig.obtenerStringCon();
                 
          Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
               

                    cn = DriverManager.getConnection(connectionUrl);
                    st = cn.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE,
                            ResultSet.CONCUR_READ_ONLY);
        
            rs = st.executeQuery(comandoSql);
 
       /*
    String insertar = "INSERT INTO cliente(id,nombre,telefono) VALUES ('4','Marco vargas','69857477')";
   // st.executeUpdate(insertar);
 
  String update = "update cliente set nombre = 'Carlos Torres' where id = 2 ";
  //     st.executeUpdate(update);
 String del = "delete cliente where id = 3 ";
  //     st.executeUpdate(del);
      
      */
    }catch (Exception e)
    {
        System.out.println("Error: " + e.getMessage());
    }
        return rs;
    }
     
    public static void ejecutarQuery(String comandoSql){
         Connection cn = null; // variable de conexion
          Statement st = null;  // variable de instruccion SQL
          
          try {
            conexionDB objAppConfig = new conexionDB();
            String connectionUrl = objAppConfig.obtenerStringCon();
                 
          Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
               

                    cn = DriverManager.getConnection(connectionUrl);
                    st = cn.createStatement(ResultSet.TYPE_SCROLL_SENSITIVE,
                            ResultSet.CONCUR_READ_ONLY);
        
            st.executeQuery(comandoSql);
 
       /*
    String insertar = "INSERT INTO cliente(id,nombre,telefono) VALUES ('4','Marco vargas','69857477')";
   // st.executeUpdate(insertar);
 
  String update = "update cliente set nombre = 'Carlos Torres' where id = 2 ";
  //     st.executeUpdate(update);
 String del = "delete cliente where id = 3 ";
  //     st.executeUpdate(del);
      
      */
    }catch (Exception e)
    {
        System.out.println("Error: " + e.getMessage());
    }
        
    }
 
}
