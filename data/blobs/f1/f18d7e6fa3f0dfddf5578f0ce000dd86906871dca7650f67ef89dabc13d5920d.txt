package com.example.pmd_autocompletetextview;

import static com.example.pmd_autocompletetextview.R.id.campo_sugerencias;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        String [] opciones ={"Opción1","Opción2","Opción3","Opción4","Opción5"};
        AutoCompleteTextView textoLeido = (AutoCompleteTextView) findViewById(R.id.campo_sugerencias);
        ArrayAdapter<String> adaptador = new ArrayAdapter<String>(
                this, android.R.layout.simple_dropdown_item_1line,opciones);
        textoLeido.setAdapter(adaptador);

    }
}