package com.example.unitconverter;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.example.unitconverter.R;

public class MainActivity extends AppCompatActivity {

    private EditText editText1, editText2;
    private Spinner spinner1, spinner2;
    private Button convertButton;

    private double conversionRate = 1.0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editText1 = findViewById(R.id.editText1);
        editText2 = findViewById(R.id.editText2);
        spinner1 = findViewById(R.id.spinner1);
        spinner2 = findViewById(R.id.spinner2);
        convertButton = findViewById(R.id.convertButton);

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                R.array.spinner_items, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner1.setAdapter(adapter);
        spinner2.setAdapter(adapter);

        spinner1.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                calculateConversionRate();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
            }
        });

        spinner2.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                calculateConversionRate();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
            }
        });

        convertButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String value1 = editText1.getText().toString().trim();
                String value2 = editText2.getText().toString().trim();

                if (value1.isEmpty() && value2.isEmpty()) {
                    Toast.makeText(MainActivity.this, "Please enter a value to convert.", Toast.LENGTH_SHORT).show();
                } else if (spinner1.getSelectedItemPosition() == spinner2.getSelectedItemPosition()) {
                    Toast.makeText(MainActivity.this, "Please select different units to convert.", Toast.LENGTH_SHORT).show();
                } else if (!value1.isEmpty()) {
                    double inputValue = Double.parseDouble(value1);
                    double result = inputValue * calculateConversionRate();
                    editText2.setText(String.valueOf(result));
                }
            }
        });
    }

//    private double calculateConversionRate() {
//        int selectedUnit1 = spinner1.getSelectedItemPosition();
//        int selectedUnit2 = spinner2.getSelectedItemPosition();
//
//        // Conversion factors for kg, gram, meter, and centimeter with respect to kg (base unit)
//        double kgToGram = 1000.0;
//        double MeterToCentimeter = 100.0;
//        double GramToKg = 0.001;
//        double CentimeterToMeter = 0.01;
//
//        double conversionRate = 1.0;
//
//        // Calculate the conversion rate based on the selected units
//        if (selectedUnit1 == selectedUnit2) {
//            conversionRate = 1.0; // Same units, no conversion needed
//        } else if (selectedUnit1 == 0 && selectedUnit2 == 1) {
//            conversionRate = kgToGram; // Convert from kg to gram
//        } else if (selectedUnit1 == 0 && selectedUnit2 == 2) {
//            Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show(); // Convert from kg to meter
//        } else if (selectedUnit1 == 0 && selectedUnit2 == 3) {
//            Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show(); // Convert from kg to centimeter
//        } else if (selectedUnit1 == 1 && selectedUnit2 == 0) {
//            conversionRate = GramToKg; // Convert from gram to kg
//        } else if (selectedUnit1 == 1 && selectedUnit2 == 2) {
//            Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show(); // Convert from gram to meter
//        } else if (selectedUnit1 == 1 && selectedUnit2 == 3) {
//            Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show(); // Convert from gram to centimeter
//        } else if (selectedUnit1 == 2 && selectedUnit2 == 0) {
//            Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show(); // Convert from meter to kg
//        } else if (selectedUnit1 == 2 && selectedUnit2 == 1) {
//            Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show(); // Convert from meter to gram
//        } else if (selectedUnit1 == 2 && selectedUnit2 == 3) {
//            conversionRate = MeterToCentimeter; // Convert from meter to centimeter (fixed conversion rate)
//        } else if (selectedUnit1 == 3 && selectedUnit2 == 0) {
//            Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show(); // Convert from centimeter to kg
//        } else if (selectedUnit1 == 3 && selectedUnit2 == 1) {
//            Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show(); // Convert from centimeter to gram
//        } else if (selectedUnit1 == 3 && selectedUnit2 == 2) {
//            conversionRate = CentimeterToMeter; // Convert from centimeter to meter (fixed conversion rate)
//        }
//
//        return conversionRate;
//    }

    private double calculateConversionRate() {
        int selectedUnit1 = spinner1.getSelectedItemPosition();
        int selectedUnit2 = spinner2.getSelectedItemPosition();

        // Conversion factors for kg, gram, meter, and centimeter with respect to kg (base unit)
        double kgToGram = 1000.0;
        double meterToCentimeter = 100.0;
        double gramToKg = 0.001;
        double centimeterToMeter = 0.01;

        double conversionRate = 1.0;

        // Calculate the conversion rate based on the selected units using switch-case
        switch (selectedUnit1) {
            case 0: // kg
                switch (selectedUnit2) {
                    case 1: // gram
                        conversionRate = kgToGram;
                        break;
                    case 2: // meter
                        Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show();;
                        break;
                    case 3: // centimeter
                        Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show();;
                        break;
                }
                break;
            case 1: // gram
                switch (selectedUnit2) {
                    case 0: // kg
                        conversionRate = gramToKg;
                        break;
                    case 2: // meter
                        Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show();
                        break;
                    case 3: // centimeter
                        Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show();
                        break;
                }
                break;
            case 2: // meter
                switch (selectedUnit2) {
                    case 0: // kg
                        Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show();
                        break;
                    case 1: // gram
                        Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show();
                        break;
                    case 3: // centimeter
                        conversionRate = meterToCentimeter;
                        break;
                }
                break;
            case 3: // centimeter
                switch (selectedUnit2) {
                    case 0: // kg
                        Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show();
                        break;
                    case 1: // gram
                        Toast.makeText(MainActivity.this, "invalid conversion.", Toast.LENGTH_SHORT).show();
                        break;
                    case 2: // meter
                        conversionRate = centimeterToMeter;
                        break;
                }
                break;
        }

        return conversionRate;
    }


}


