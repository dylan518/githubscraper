package com.example.apexlegendsinfo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;
import android.view.Gravity;

public class ar extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ar);
    }
    public void goBack(View v) {
        Intent intent = new Intent(this, guns.class);
        startActivity(intent);
    }
    public void goMain(View v) {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
    public void havoc(View view){
        Toast toast = Toast.makeText(this, "Энергетическое оружие Хаос", Toast.LENGTH_SHORT);
        toast.show();
    }
    public void flat(View view){
        Toast toast = Toast.makeText(this, "Тяжелое оружие Флэтлайн", Toast.LENGTH_SHORT);
        toast.show();
    }
    public void hem(View view){
        Toast toast = Toast.makeText(this, "Тяжелое оружие Хемлок", Toast.LENGTH_SHORT);
        toast.show();
    }
    public void r301(View view){
        Toast toast = Toast.makeText(this, "Легкое оружие R-301", Toast.LENGTH_SHORT);
        toast.show();
    }
    public void nemesis(View view){
        Toast toast = Toast.makeText(this, "Энергетическое оружие Возмездие", Toast.LENGTH_SHORT);
        toast.show();
    }
}