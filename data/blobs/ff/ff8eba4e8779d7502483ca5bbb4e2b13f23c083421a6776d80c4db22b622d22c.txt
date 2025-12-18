 
package ebrahimmohamed2051710975;

import java.awt.Image;
import javafx.application.Application;
 import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.layout.GridPane;
import javafx.geometry.Insets;
//import javafx.geometry.VPos;
//import javafx.geometry.HPos;
import javafx.geometry.Pos;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.control.Label;
import javafx.scene.control.ToggleGroup;
import javafx.fxml.FXML;
import javafx.geometry.HPos;
import javafx.scene.control.Button;

public class GUI extends Application {
    
    public void start  (Stage st){
        GridPane pane =new GridPane();
        pane.setStyle("-fx-background-color: #f4eee2; -fx-padding: 20; -fx-font-size: 20;");
        pane.setAlignment(Pos.CENTER);
        
        
        pane.add(new Label("Name"), 0, 0);
        TextField tfName = new TextField();
        pane.add(tfName, 1, 0);
        
        
        pane.add(new Label("ID"), 0, 1);
        TextField tfID = new TextField();
        pane.add(tfID, 1, 1);
        
        
        pane.add(new Label("Age"), 0, 2);
        TextField tfAge = new TextField();
        pane.add(tfAge, 1, 2);
        
        
        pane.add(new Label("Gender"), 0, 3);
        TextField tfGender = new TextField();
        pane.add(tfGender, 1, 3);
        
        
        RadioButton tMarriage = new RadioButton(" YES"); 
        RadioButton fMarriage = new RadioButton("NO");
        ToggleGroup marraigeGroup = new ToggleGroup();// to can select one radio you should create toggelgroup
        tMarriage.setToggleGroup(marraigeGroup);
        fMarriage.setToggleGroup(marraigeGroup);
        pane.add(new Label("are yolu marriage?"), 0, 4);
        pane.add(tMarriage, 1, 4);
        pane.add(fMarriage, 2, 4);
         
        
        Button add = new Button("ADD");
        pane.add(add,0,5);
        pane.setHalignment(add, HPos.RIGHT);
        
        
        
        add.setOnAction(e->{
        String name = tfName.getText();
        String id = tfID.getText();
        Integer age = Integer.parseInt(tfAge.getText());
        String gender = tfGender.getText();
        if(tMarriage.isResizable()){
            MainOperations.add_new_citizen_to_list(name,id,age,gender,true);
            
        }
        else{
            MainOperations.add_new_citizen_to_list(name,id,age,gender,false);
        }
    });
         Scene scene = new Scene(pane, 650, 300);
 
    st.setTitle("ShowFlowPane"); // Set the stage title
    st.setScene(scene); // Place the scene in the stage
    
    st.show(); // Display the stage

        
        
        
        
        
        
        
        
        
        
        
        
        
        //Image earth = new Image( "earth.png" ) ;
        
        
    }
    
    
}
