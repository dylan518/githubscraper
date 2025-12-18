package com.example.employeesystem;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

public class updating extends AppCompatActivity {
    EditText editt1,editt2,editt3,editt4,editt5;
    mydatabasehelper mds;
    String gender = "";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_updating);
        mds = new mydatabasehelper(this);

        editt1 = findViewById(R.id.edt1);
        editt2 = findViewById(R.id.edt2);
        editt3 = findViewById(R.id.edt3);
        editt4 = findViewById(R.id.edt4);
        editt5 = findViewById(R.id.edt5);

        Button btn =findViewById(R.id.button1);

        RadioGroup rbt=findViewById(R.id.radiog);
        RadioButton rgk=findViewById(R.id.radio_female);
        RadioButton rgl=findViewById(R.id.radio_male);

        rbt.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {

                if (checkedId == R.id.radio_male) {
                    gender = "male";
                    rgl.setCompoundDrawablesWithIntrinsicBounds(0, R.drawable.ic_baseline_radio_button_checked_24, 0, 0);
                    rgk.setCompoundDrawablesWithIntrinsicBounds(0, R.drawable.ic_baseline_radio_button_unchecked_24, 0, 0);
                } else if (checkedId == R.id.radio_female) {
                    gender = "female";
                    rgk.setCompoundDrawablesWithIntrinsicBounds(0, R.drawable.ic_baseline_radio_button_checked_24, 0, 0);
                    rgl.setCompoundDrawablesWithIntrinsicBounds(0, R.drawable.ic_baseline_radio_button_unchecked_24, 0, 0);
                }
            }
        });

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ng3();
            }
        });


    }

    public void ng3()
    {
        int id = Integer.parseInt(editt1.getText().toString());
        String firstname = editt2.getText().toString();
        String middlename = editt3.getText().toString();
        String salary = editt4.getText().toString();
        String department = editt5.getText().toString();

        jamualem updatedJamualem = new jamualem(id, firstname, middlename,gender,salary, department);
        boolean isSuccess = mds.updatedata(updatedJamualem);

        if (isSuccess == true) {
            Toast.makeText(getApplicationContext(), "Update successful", Toast.LENGTH_LONG).show();
        } else {
            Toast.makeText(getApplicationContext(), "Please fill all fields correctly!", Toast.LENGTH_LONG).show();
        }
    }





}