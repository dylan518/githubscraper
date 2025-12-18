package com.example.lab2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText editHoTen, editMSSV, editTuoi;
    RadioGroup radioGroup;
    RadioButton radiobtnNam, radiobtnNu;
    CheckBox checkboxBong, checkBoxGame;
    Button btnSave;
    TextView textViewResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editHoTen = findViewById(R.id.editHoTen);
        editMSSV = findViewById(R.id.editMSSV);
        editTuoi = findViewById(R.id.editTuoi);
        radioGroup = findViewById(R.id.radioGroup2);
        radiobtnNam = findViewById(R.id.radiobtnNam);
        radiobtnNu = findViewById(R.id.radiobtnNu);
        checkboxBong = findViewById(R.id.checkboxBong);
        checkBoxGame = findViewById(R.id.checkBoxGame);
        btnSave = findViewById(R.id.btnSave);
        textViewResult = findViewById(R.id.textView4);

        btnSave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String hoTen = editHoTen.getText().toString();
                String mssv = editMSSV.getText().toString();
                String tuoi = editTuoi.getText().toString();
                String gioiTinh = (radiobtnNam.isChecked()) ? "Nam" : "Nữ";
                boolean daBong = checkboxBong.isChecked();
                boolean choiGame = checkBoxGame.isChecked();

                String message = "Họ tên: " + hoTen +
                        "\nMSSV: " + mssv +
                        "\nTuổi: " + tuoi +
                        "\nGiới tính: " + gioiTinh +
                        "\nSở thích: " +
                        (daBong ? "Đá Bóng" : "") +
                        (choiGame ? "Chơi Game" : "");

                textViewResult.setText(message);
                Toast.makeText(MainActivity.this, "Thông tin đã được lưu", Toast.LENGTH_SHORT).show();
            }
        });
    }
}