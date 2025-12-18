package com.example.zorenka.view;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Spinner;

import com.example.zorenka.R;
import com.example.zorenka.adapter.ChildAdapter;
import com.example.zorenka.adapter.ReasonAdapter;
import com.example.zorenka.callback.CreateAttendanceCallback;
import com.example.zorenka.callback.SpinCallback;
import com.example.zorenka.server.HttpBuilder;
import com.example.zorenka.server.model.AttendanceCreateDto;
import com.example.zorenka.server.model.ChildrenEntity;
import com.example.zorenka.server.model.PersonEntity;
import com.example.zorenka.server.model.ReasonEntity;
import com.example.zorenka.server.repository.AttendanceRepository;
import com.example.zorenka.server.repository.ChildRepository;
import com.example.zorenka.server.repository.ReasonRepository;
import com.example.zorenka.view.dialog.MessageDialog;

import java.text.SimpleDateFormat;
import java.util.Date;

public class AddAttendanceActivity extends AppCompatActivity {

    private Spinner childSpinner;
    private Spinner reasonSpinner;
    private EditText markView;
    private DatePicker picker;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_attendance);

        childSpinner = findViewById(R.id.child);
        reasonSpinner = findViewById(R.id.reason);
        markView = findViewById(R.id.mark);
        final Button button = findViewById(R.id.save);
        picker = findViewById(R.id.picker);

        HttpBuilder builder = new HttpBuilder();

        ReasonRepository reasonRepository = builder.createRepository(ReasonRepository.class);
        ChildRepository childRepository = builder.createRepository(ChildRepository.class);

        SpinCallback<ChildrenEntity> childCallback = new SpinCallback<>(this);
        SpinCallback<ReasonEntity> reasonCallback = new SpinCallback<>(this);

        childCallback.onFetch(items -> {
            ArrayAdapter<ChildrenEntity> adapter = new ChildAdapter(this, items);
            childSpinner.setAdapter(adapter);
            childSpinner.setSelection(0);
        });

        reasonCallback.onFetch(items -> {
            ReasonEntity empty = new ReasonEntity();
            empty.setReason("Не выбран");
            empty.setId_reason(0);
            items.add(0, empty);
            ArrayAdapter<ReasonEntity> adapter = new ReasonAdapter(this, items);
            reasonSpinner.setAdapter(adapter);
        });

        reasonRepository.getAll().enqueue(reasonCallback);
        childRepository.getAll().enqueue(childCallback);
        button.setOnClickListener(this::trySaveChanges);
    }

    private void trySaveChanges(View v) {
        try {
            AttendanceCreateDto dto = checkFields();
            saveChanges(dto);
        } catch (Exception ex) {
            MessageDialog dialog = new MessageDialog(this);
            dialog.showDialog("Ошибка!", ex.getMessage());
            ex.printStackTrace();
        }
    }

    private AttendanceCreateDto checkFields() throws Exception {
        AttendanceCreateDto dto = new AttendanceCreateDto();
        Date date = new Date(picker.getYear() - 1900, picker.getMonth(), picker.getDayOfMonth());
        String mark = markView.getText().toString();
        ReasonEntity reason = (ReasonEntity) reasonSpinner.getSelectedItem();
        ChildrenEntity children = (ChildrenEntity) childSpinner.getSelectedItem();
        if (mark.isEmpty()) {
            throw new IllegalArgumentException("Введите пометку!");
        }

        if (children == null) {
            throw new IllegalArgumentException("Выберите ребенка!");
        }

        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
        dto.setDate(dateFormat.format(date));
        dto.setMark(mark);
        dto.setId_reason(reason.getId_reason() != 0 ? reason.getId_reason() : null);
        dto.setId_child(children.getId_children());
        return dto;
    }

    private void saveChanges(AttendanceCreateDto dto) {
        HttpBuilder builder = new HttpBuilder();
        AttendanceRepository repository = builder.createRepository(AttendanceRepository.class);

        repository.create(dto).enqueue(new CreateAttendanceCallback(this));
    }

}