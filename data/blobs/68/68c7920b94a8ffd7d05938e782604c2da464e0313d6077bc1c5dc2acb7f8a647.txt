package com.lunar.allbdtickets;

import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

public class usBangla extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_us_bangla);

        WebView usBangla = (WebView) findViewById(R.id.usBangla);


        WebSettings websettings =usBangla.getSettings();
        websettings.setJavaScriptEnabled(true);

        usBangla.loadUrl("https://usbair.com/");

        usBangla.setScrollBarStyle(View.SCROLLBARS_OUTSIDE_OVERLAY);

        usBangla.getSettings().setBuiltInZoomControls(true);
        usBangla.getSettings().setUseWideViewPort(true);
        usBangla.getSettings().setLoadWithOverviewMode(true);

        ProgressDialog progressDialog = new ProgressDialog(usBangla.this);
        progressDialog.setMessage("Loading...");
        progressDialog.show();

        usBangla.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                if (progressDialog.isShowing()) {
                    progressDialog.dismiss();
                }
            }

            @Override
            public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {
                Toast.makeText(usBangla.this, "Error:" + description, Toast.LENGTH_SHORT).show();

            }
        });
    }
}