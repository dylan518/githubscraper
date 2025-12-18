package com.example.ga;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.LinearLayout;

public class About extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);
        WebView webView;
        LinearLayout back;


        back = findViewById(R.id.back);
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gohome();
            }
        });
        webView= findViewById(R.id.webview);
        webView.loadUrl("https://gai.polytech.gov.bd/site/page/bc3602e9-9f15-41dc-9f85-0da337e98c9d/-");


    }

    private void gohome() {
        Intent intent = new Intent(this, Home.class);
        startActivity(intent);
    }

}