package com.example.androidprojectcollection;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.util.Random;

public class MenuExercise extends AppCompatActivity {
    Button btnChanger;
    int[] colors = {Color.RED, Color.YELLOW, Color.BLUE, Color.CYAN, Color.MAGENTA, Color.GREEN, Color.WHITE, Color.BLACK};
    String[] greetings = {"Hello!", "Good Morning!", "Good Afternoon!", "Good Evening!", "Good Day!", "Goodbye!", "Hi!"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu_exercise);

        btnChanger = findViewById(R.id.btnTransformer);
        setDefault(btnChanger);

    }

    private void setDefault(Button b) {
        b.setText("Hello!");
        b.setTextColor(Color.WHITE);
        b.setBackgroundColor(Color.RED);
        b.setWidth(1000);
        b.setHeight(1000);
//        b.setMaxWidth(250);
//        b.setMaxHeight(250);
        b.setVisibility(View.VISIBLE);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_menuexercise, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        if (item.getItemId() == R.id.mItemChange) {
            Toast.makeText(this, "Editing Button...", Toast.LENGTH_SHORT).show();

        } else if (item.getItemId() == R.id.mItemColor) { //1
            int rand1 = new Random().nextInt(colors.length);
            btnChanger.setBackgroundColor(colors[rand1]);
            Toast.makeText(this, "Color Updated", Toast.LENGTH_SHORT).show();

        } else if (item.getItemId() == R.id.mItemSize) { //2
            btnChanger.setWidth(500);
            btnChanger.setHeight(500);
            Toast.makeText(this, "Size Updated", Toast.LENGTH_SHORT).show();

        } else if (item.getItemId() == R.id.mItemTextColor) { //3
            int rand2 = new Random().nextInt(colors.length);
            btnChanger.setTextColor(colors[rand2]);
            Toast.makeText(this, "Text Color Updated", Toast.LENGTH_SHORT).show();

        } else if (item.getItemId() == R.id.mItemGreeting) { //4
            int rand3  = new Random().nextInt(greetings.length);
            btnChanger.setText(greetings[rand3]);
            Toast.makeText(this, "Greetings Updated", Toast.LENGTH_SHORT).show();

        } else if (item.getItemId() == R.id.mItemVisibility) { //5
            if (btnChanger.getVisibility() == View.VISIBLE) {
                btnChanger.setVisibility(View.INVISIBLE);
            } else {
                btnChanger.setVisibility(View.VISIBLE);
            }
            Toast.makeText(this, "Visibility Updated", Toast.LENGTH_SHORT).show();

        }
        else if (item.getItemId() == R.id.mItemReset) {
            Toast.makeText(this, "Button is Reset", Toast.LENGTH_SHORT).show();
            setDefault(btnChanger);
        } else if (item.getItemId() == R.id.mitemExit) {
            finish();
        }

        return true;
    }
}