package com.geektech.hw3_numbers;

import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class NumberViewHolder extends RecyclerView.ViewHolder {
    private TextView tvNumber;
    public NumberViewHolder(@NonNull View itemView) {
        super(itemView);
        tvNumber=itemView.findViewById(R.id.number);
    }
    public void bind(String number){
        tvNumber.setText(number);
    }
}
