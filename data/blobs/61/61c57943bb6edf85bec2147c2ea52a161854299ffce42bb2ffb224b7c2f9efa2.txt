package com.example.imageapp.activity;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;
import androidx.recyclerview.widget.StaggeredGridLayoutManager;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.example.imageapp.R;
import com.example.imageapp.adapter.PinterestAdapter;
import com.example.imageapp.event.ImageEvent;
import com.example.imageapp.model.Pinterest;

import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

import java.util.ArrayList;
import java.util.List;

public class ProfileActivity extends AppCompatActivity {
    private List<Pinterest> pinterestList = new ArrayList<>();
    TextView tvUsername;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        getUser();

        //Data
        initData();

        //Adapter
        PinterestAdapter pinterestAdapter =new PinterestAdapter(this,pinterestList);

        //Layout Manager
        RecyclerView.LayoutManager layoutManager = new StaggeredGridLayoutManager(2,StaggeredGridLayoutManager.VERTICAL);

        //Recycle view
        RecyclerView rvPinterest =findViewById(R.id.rvPinterest);
        rvPinterest.setLayoutManager(layoutManager);
        rvPinterest.setAdapter(pinterestAdapter);
    }

    private void getUser() {
        SharedPreferences pref = getSharedPreferences("USER", MODE_PRIVATE);
        String username = pref.getString("username", null);
        tvUsername= findViewById(R.id.tvUsername);
        tvUsername.setText(username);

    }

    private void initData() {
        for (int i = 0; i < 50; i++) {
            pinterestList.add(new Pinterest("https://i.pinimg.com/564x/f3/76/8c/f3768c928125401cca765cda29359e23.jpg","Hình nền galaxy siêu đẹp"));
            pinterestList.add(new Pinterest("https://i.pinimg.com/236x/d9/e2/df/d9e2df1a999b3035320322b5eaae760c.jpg","Hình nền galaxy siêu đẹp"));
            pinterestList.add(new Pinterest("https://i.pinimg.com/564x/e3/3c/b2/e33cb20565b43ab4b5280b240d4f1660.jpg","Hình nền galaxy siêu đẹp"));
            pinterestList.add(new Pinterest("https://i.pinimg.com/236x/03/83/f5/0383f53d9e2331288237081d00de15a9.jpg","Hình nền galaxy siêu đẹp"));
            pinterestList.add(new Pinterest("https://i.pinimg.com/564x/6c/31/32/6c31322f234c97107f1d38d0f4c4fa2f.jpg","Hình nền galaxy siêu đẹp"));
            pinterestList.add(new Pinterest("https://i.pinimg.com/236x/15/20/ac/1520acd3382022250548f227357ad139.jpg","Hình nền galaxy siêu đẹp"));
            pinterestList.add(new Pinterest("https://i.pinimg.com/564x/9a/0b/b9/9a0bb9754b10e73444a5be0b8011855c.jpg","Hình nền galaxy siêu đẹp"));
            pinterestList.add(new Pinterest("https://i.pinimg.com/236x/2e/e7/5e/2ee75e26c3e9152d00f9c829771665c4.jpg","Hình nền galaxy siêu đẹp"));
            pinterestList.add(new Pinterest("https://i.pinimg.com/564x/61/c1/aa/61c1aaad9557346fb2d47feb12037461.jpg","Hình nền galaxy siêu đẹp"));
            pinterestList.add(new Pinterest("https://i.pinimg.com/564x/21/bb/cc/21bbcc993c100ff79f4c42c580ce8a08.jpg","Hình nền galaxy siêu đẹp"));
        }
    }
    @Override
    public void onStart() {
        super.onStart();
        EventBus.getDefault().register(this);
    }

    @Override
    public void onStop() {
        super.onStop();
        EventBus.getDefault().unregister(this);
    }
    private void goToDetail(Pinterest pinterest) {
        Intent intent = new Intent(this, DetailActivity.class);
        intent.putExtra("PINTEREST", pinterest);
        startActivity(intent);
    }

    @Subscribe(threadMode = ThreadMode.MAIN)
    public void onImageEvent(ImageEvent.PinterestEvent pinterestEvent) {
        Pinterest pinterest = pinterestEvent.getPinterest();
        Log.d("TAG", "onImageEvent: "+pinterest.getContent());
        goToDetail(pinterest);
    }
}