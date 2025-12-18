package com.example.calculator;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private Button bt_0;
    private Button bt_1;
    private Button bt_2;
    private Button bt_3;
    private Button bt_4;
    private Button bt_5;
    private Button bt_6;
    private Button bt_7;
    private Button bt_8;
    private Button bt_9;

    private Button bt_point;
    private Button bt_equal;
    private Button bt_plus;
    private Button bt_minus;
    private Button bt_multiply;
    private Button bt_divide;
    private Button bt_backspace;
    private Button bt_clear;

    private TextView inputText;
    private TextView outputText;
    private final char ADD = '+';
    private final char SUB = '-';
    private final char MUL = '*';
    private final char DIV = '/';
    private final char EQU = '=';
    private char ACT;
    private double val1 = Double.NaN;
    private double val2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setup();

        bt_0.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "0");
        });

        bt_1.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "1");
        });

        bt_2.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "2");
        });

        bt_3.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "3");
        });

        bt_4.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "4");
        });

        bt_5.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "5");
        });

        bt_6.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "6");
        });

        bt_7.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "7");
        });

        bt_8.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "8");
        });

        bt_9.setOnClickListener(view -> {
            ifErrorOnOutput();
            inputText.setText(inputText.getText().toString() + "9");
        });

        bt_point.setOnClickListener(view -> inputText.setText(inputText.getText().toString() + "."));

        bt_plus.setOnClickListener(view -> {
            if (inputText.getText().length() > 0) {
                ACT = ADD;
                operation();
                if (ifReallyDecimal()) {
                    outputText.setText(val1 + "+");
                } else {
                    outputText.setText((int) val1 + "+");
                }
                outputText.setText(null);
            } else {
                outputText.setText("Error");
            }
        });

        bt_minus.setOnClickListener(view -> {
            if (inputText.getText().length() > 0) {
                ACT = SUB;
                operation();
                if (inputText.getText().length() > 0)
                    if (ifReallyDecimal()) {
                        outputText.setText(val1 + "-");
                    } else {
                        outputText.setText((int) val1 + "-");
                    }
                inputText.setText(null);
            } else {
                outputText.setText("Error");
            }
        });

        bt_multiply.setOnClickListener(view -> {
            if (inputText.getText().length() > 0) {
                ACT = MUL;
                operation();
                if (inputText.getText().length() > 0)
                    if (ifReallyDecimal()) {
                        outputText.setText(val1 + "×");
                    } else {
                        outputText.setText((int) val1 + "×");
                    }
                inputText.setText(null);
            } else {
                outputText.setText("Error");
            }
        });

        bt_divide.setOnClickListener(view -> {
            if (inputText.getText().length() > 0) {
                ACT = DIV;
                operation();
                if (inputText.getText().length() > 0)
                    if (ifReallyDecimal()) {
                        outputText.setText(val1 + "÷");
                    } else {
                        outputText.setText((int) val1 + "÷");
                    }
                inputText.setText(null);
            } else {
                outputText.setText("Error");
            }
        });

        bt_equal.setOnClickListener(view -> {
            if (inputText.getText().length() > 0) {
                operation();
                ACT = EQU;
                if (ifReallyDecimal()) {
                    inputText.setText(String.valueOf(val1));
                } else {
                    inputText.setText(String.valueOf((int) val1));
                }
                outputText.setText(null);
            } else {
                outputText.setText("Error");
            }
        });

        bt_backspace.setOnClickListener(view -> {
            if (inputText.getText().length() > 0) {
                CharSequence name = inputText.getText().toString();
                inputText.setText(name.subSequence(0, name.length() - 1));
            } else {
                val1 = Double.NaN;
                val2 = Double.NaN;
                inputText.setText("");
                outputText.setText("");
            }
        });

        bt_clear.setOnClickListener(view -> {
            val1 = Double.NaN;
            val2 = Double.NaN;
            inputText.setText("");
            outputText.setText("");
        });

    }

    private void setup() {
        bt_0 = findViewById(R.id.bt_0);
        bt_1 = findViewById(R.id.bt_1);
        bt_2 = findViewById(R.id.bt_2);
        bt_3 = findViewById(R.id.bt_3);
        bt_4 = findViewById(R.id.bt_4);
        bt_5 = findViewById(R.id.bt_5);
        bt_6 = findViewById(R.id.bt_6);
        bt_7 = findViewById(R.id.bt_7);
        bt_8 = findViewById(R.id.bt_8);
        bt_9 = findViewById(R.id.bt_9);

        bt_point = findViewById(R.id.bt_point);
        bt_equal = findViewById(R.id.bt_equal);
        bt_plus = findViewById(R.id.bt_plus);
        bt_minus = findViewById(R.id.bt_minus);
        bt_multiply = findViewById(R.id.bt_multiply);
        bt_divide = findViewById(R.id.bt_divide);
        bt_backspace = findViewById(R.id.bt_backspace);
        bt_clear = findViewById(R.id.bt_clear);

        inputText = findViewById(R.id.tx_in);
        outputText = findViewById(R.id.tx_out);
    }

    private void operation() {
        if (!Double.isNaN(val1)) {
            if (outputText.getText().toString().charAt(0) == '-') {
                val1 = (-1) * val1;
            }
            val2 = Double.parseDouble(inputText.getText().toString());

            switch (ACT) {
                case ADD:
                    val1 = val1 + val2;
                    break;
                case SUB:
                    val1 = val1 - val2;
                    break;
                case MUL:
                    val1 = val1 * val2;
                    break;
                case DIV:
                    val1 = val1 / val2;
                    break;
                case EQU:
                    break;
            }
        } else {
            val1 = Double.parseDouble(inputText.getText().toString());
        }
    }

    // Remove error message that is already written there.
    private void ifErrorOnOutput() {
        if (outputText.getText().toString().equals("Error")) {
            outputText.setText("");
        }
    }

    // Whether value if a double or not
    private boolean ifReallyDecimal() {
        return val1 != (int) val1;
    }

}