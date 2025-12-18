package com.example.randomchoicehelperapplicationapp.view;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.randomchoicehelperapplicationapp.R;

public class WordGroupViewHolder extends RecyclerView.ViewHolder{
    private final TextView wordGroupItemView;

    private WordGroupViewHolder(View itemView) {
        super(itemView);
        wordGroupItemView = itemView.findViewById(R.id.textView);
    }

    public void bind(String text) {
        wordGroupItemView.setText(text);
    }

    static  WordGroupViewHolder create(ViewGroup parent){
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.recyclerview_item, parent, false);
        return new WordGroupViewHolder(view);
    }
}
