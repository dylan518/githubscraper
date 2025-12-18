package com.przybylski.vaadindemo.gui;


import com.przybylski.vaadindemo.menager.CarManager;
import com.przybylski.vaadindemo.model.Car;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.dialog.Dialog;
import com.vaadin.flow.router.Route;
import com.vaadin.flow.router.RouterLink;
import org.springframework.beans.factory.annotation.Autowired;

import java.awt.*;

@Route("add-car")
public class CarAdderGui extends VerticalLayout {

    private CarManager carManager;

    @Autowired
    public CarAdderGui(CarManager carManager) {
        this.carManager = carManager;

        TextField textFieldMark = new TextField();
        textFieldMark.setLabel("Mark");
        TextField textFieldModel = new TextField("Model");
        Button buttonAdd = new Button("add Car");

        buttonAdd.addClickListener(event ->  {
                    Car car = new Car(textFieldMark.getValue(), textFieldModel.getValue());
                    carManager.addCar(car);

                    carManager.getCarList().forEach(System.out::println);
                    textFieldMark.clear();
                    textFieldModel.clear();
            RouterLink routerLink = new RouterLink("Przekierowanie", CarShowGui.class);
                    add(routerLink);

            }
        );

        add(textFieldMark, textFieldModel, buttonAdd);
    }


    }

