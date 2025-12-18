package com.example.bv;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;


public class Cityguide extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cityguide);
        getSupportActionBar().setBackgroundDrawable(new ColorDrawable(Color.TRANSPARENT));

        ImageView image1 = findViewById(R.id.ivCity1);
        ImageView image2 = findViewById(R.id.ivCity2);
        ImageView image3 = findViewById(R.id.ivCity3);
        ImageView image4 = findViewById(R.id.ivCity4);
        Button button = findViewById(R.id.button);

        final int[] currentImage = {1};

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                switch (currentImage[0]) {
                    case 1:
                        image1.setVisibility(View.GONE);
                        image2.setVisibility(View.VISIBLE);
                        currentImage[0] = 2;
                        break;
                    case 2:
                        image2.setVisibility(View.GONE);
                        image3.setVisibility(View.VISIBLE);
                        currentImage[0] = 3;
                        break;
                    case 3:
                        image3.setVisibility(View.GONE);
                        image4.setVisibility(View.VISIBLE);
                        currentImage[0] = 4;
                        break;
                    case 4:
                        image4.setVisibility(View.GONE);
                        image1.setVisibility(View.VISIBLE);
                        currentImage[0] = 1;
                        break;
                }
            }
        });
    }
}