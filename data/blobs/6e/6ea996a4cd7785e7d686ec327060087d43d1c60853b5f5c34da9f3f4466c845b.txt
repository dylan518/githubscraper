package com.example.calculadoraimc;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Menu extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //ASSOCIAR O BOTAO PARA SAIR
        Button btnsair;

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        btnsair = findViewById(R.id.btnSair);

        btnsair.setOnClickListener(new View.OnClickListener() {
            //UMA DAS FORMAS DE METER UM BOTAO A TRABALHAR
            @Override
            public void onClick(View view) {
                finish();
            }
        });
    }
public void vaiParaCalculoIMC(View v){
            Intent it = new Intent(Menu.this, CalculoIMC.class);
            startActivity(it);
            finish();
    }
 public void vaiParaConversor(View v){
            Intent it = new Intent(Menu.this, Conversor.class);
            startActivity(it);
            finish();
    }

}