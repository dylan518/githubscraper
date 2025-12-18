package com.example.myweathernew;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.MediaController;
import android.widget.TextView;
import android.widget.VideoView;

public class MainActivity5 extends AppCompatActivity {

    public TextView feedBackBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main5);

        WebView webView = findViewById(R.id.webView);
        String videoUrl = "https://www.youtube.com/embed/iXuc7SAyk2s";

        webView.getSettings().setJavaScriptEnabled(true);

        webView.loadUrl(videoUrl);

        feedBackBtn = findViewById(R.id.feedBackBtn);

        feedBackBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity5.this, MainActivity6.class));
            }
        });
    }
}