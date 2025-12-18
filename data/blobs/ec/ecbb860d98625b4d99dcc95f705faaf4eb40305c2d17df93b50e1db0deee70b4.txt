package com.example.gurushishyamobileapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

import com.example.gurushishyamobileapp.databinding.ActivityHomeBinding;

public class homeActivity extends AppCompatActivity {

    ActivityHomeBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        binding=ActivityHomeBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        replaceFrag(new samorFragment());
        binding.bottomNavigationView.setOnItemSelectedListener(item -> {
            switch (item.getItemId()){
                case R.id.home:
                    replaceFrag(new samorFragment());
                    break;
                case R.id.search:
                    replaceFrag(new searchFragment());
                    break;
                case R.id.account:
                    replaceFrag(new accFragment());
                    break;
            }
            return true;
        });
    }

    private void replaceFrag(Fragment fragment){
        FragmentManager fragmentManager=getSupportFragmentManager();
        FragmentTransaction fragmentTransaction=fragmentManager.beginTransaction();
        fragmentTransaction.replace(R.id.frame_layout,fragment);
        fragmentTransaction.commit();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu,menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        switch(item.getItemId()){
            case R.id.privacy:
                startActivity(new Intent(this,privacyActivity.class));
                break;
            case R.id.terms:
                startActivity(new Intent(this,termsActivity.class));
                break;
            case R.id.aboutus:
                startActivity(new Intent(this,aboutusActivity.class));
                break;
            case R.id.menuLogout:
                sharedpref.getInstance(this).logout();
                finish();
                startActivity(new Intent(this,loginActivity.class));
                break;
        }
        return true;
    }
}