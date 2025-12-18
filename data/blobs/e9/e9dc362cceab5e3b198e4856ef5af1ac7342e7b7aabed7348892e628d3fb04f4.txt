package com.example.unit_go;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

public class temperatureActivity extends AppCompatActivity {

    EditText input;
    Spinner unit;
    TextView celsius, fahrenheit, kelvin, rankine, reaumur;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_temperature);

        input = findViewById(R.id.input);
        unit = findViewById(R.id.unit);
        celsius = findViewById(R.id.celsius);
        fahrenheit = findViewById(R.id.fahrenheit);
        kelvin = findViewById(R.id.kelvin);
        rankine = findViewById(R.id.rankine);
        reaumur = findViewById(R.id.reaumur);

        String[] arr = {"C", "F", "K", "R", "Re"};
        unit.setAdapter(new ArrayAdapter(temperatureActivity.this, android.R.layout.simple_list_item_1, arr));

        unit.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                update();
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        input.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void afterTextChanged(Editable editable) {
                update();
            }
        });

    }

    private void update(){

        if(!input.getText().toString().equals("") && !unit.getSelectedItem().toString().equals("")){
            double in = Double.parseDouble(input.getText().toString());
            switch (unit.getSelectedItem().toString()) {
                case "C":
                    setKm(in);
                    break;
                case "F":
                    setKm((in-32)*5/9);
                    break;
                case "K":
                    setKm(in-273.15);
                    break;
                case "R":
                    setKm((in-491.67)*5/9);
                    break;
                case "Re":
                    setKm(in/0.8);
                    break;


            }
        }

    }

    private void setKm(double km_in) {
        celsius.setText(String.valueOf(km_in));
        fahrenheit.setText(String.valueOf((km_in*9/5)+32));
        kelvin.setText(String.valueOf(km_in+273.15));
        rankine.setText(String.valueOf(km_in*9/5+491.67));
        reaumur.setText(String.valueOf(km_in*0.8));


    }

}