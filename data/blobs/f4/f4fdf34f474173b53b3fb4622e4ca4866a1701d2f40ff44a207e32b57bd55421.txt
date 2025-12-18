package com.example.fragment;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import com.example.fragment.R;
import com.example.fragment.HealthCareFragment;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Check if the fragment is already added
        if (savedInstanceState == null) {
            // Initialize the fragment
            HealthCareFragment healthCareFragment = new HealthCareFragment();

            // Get the FragmentManager
            FragmentManager fragmentManager = getSupportFragmentManager();

            // Begin a transaction
            FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();

            // Add the fragment to the container
            fragmentTransaction.add(R.id.container_view, healthCareFragment);

            // Commit the transaction
            fragmentTransaction.commit();
        }
    }
}