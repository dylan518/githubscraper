package com.showcase.activitycheckplugin;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class ActivityStringResources extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Задаем макет для этой активити. Макет определяет структуру пользовательского интерфейса активити
        setContentView(R.layout.activity_string_resources);

        // Ищем TextView в макете по его ID. Это тот же ID, который мы указали в макете XML
        TextView textView = (TextView) findViewById(R.id.text_view);

        // Устанавливаем текст для TextView. R.string.message это ссылка на строковый ресурс в файле ресурсов
        textView.setText(R.string.message);

        // Ищем Button в макете по его ID. Это тот же ID, который мы указали в макете XML
        Button closeButton = (Button) findViewById(R.id.close_button);

        // Устанавливаем ивент. Когда пользователь нажмет кнопку, будет вызван этот метод
        closeButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Закрываем активити. Это означает, что активити будет удалена из стека активити и пользователь вернется к предыдущей активити
                finish();
            }
        });
    }
}
