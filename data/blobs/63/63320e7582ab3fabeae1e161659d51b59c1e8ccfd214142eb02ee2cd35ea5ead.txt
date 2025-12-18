package com.example.lishe;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import android.os.Bundle;
import android.widget.Adapter;

public class UlajiUnaofaa extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ulaji_unaofaa);

        ViewPager viewPager = findViewById(R.id.viewpager_ulaji_unaofaa);

        UlajiUnaofaaAdapter adapter = new UlajiUnaofaaAdapter(this);
        viewPager.setAdapter(adapter);

    }
}