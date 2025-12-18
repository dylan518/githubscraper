package com.example.mysqltest;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    EditText etUsername, etPassword, etDbase;
    EditText etSerialNo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        etUsername = (EditText)findViewById(R.id.etUserID);
        etPassword = (EditText)findViewById(R.id.etPassword);
        etDbase = (EditText) findViewById(R.id.etDBname);
        etSerialNo = (EditText) findViewById(R.id.etSerialNo);
    }

    public void OnLogin(View view) {
        String username = etUsername.getText().toString();
        String password = etPassword.getText().toString();
        String dbase = etDbase.getText().toString();
        String slno = etSerialNo.getText().toString();
        String type = "login";
        BackgroundWorker backgroundWorker = new BackgroundWorker(this);
        backgroundWorker.execute(type, username, password, dbase, slno, "GET");
    }
}