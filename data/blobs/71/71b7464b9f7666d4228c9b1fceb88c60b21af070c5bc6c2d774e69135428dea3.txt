package com.jaydip.fancyfontskeyboard;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.jaydip.fancyfontskeyboard.adapters.FancyFontsAdapter;
import com.jaydip.fancyfontskeyboard.util.AdManager;
import com.jaydip.fancyfontskeyboard.util.KeyDataHolder;
import com.jaydip.fancyfontskeyboard.util.KeyboardSupport;

public class FancyFontActivity extends AppCompatActivity {
    ImageView backIV;
    public FancyFontsAdapter fancyFontsAdapter;
    private RecyclerView fancyFontsRV;
    public KeyDataHolder keyDataHolder;


    @Override
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_fancy_font);
        backIV= (ImageView) findViewById(R.id.backIV);
        backIV.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                onBackPressed();
            }
        });
        this.keyDataHolder = new KeyDataHolder(this);
        fancyFontsRV= (RecyclerView) findViewById(R.id.gradientThemeRV);
        fancyFontsRV.setLayoutManager(new GridLayoutManager(this, 2));
        fancyFontsAdapter= new FancyFontsAdapter(this, new FancyFontsAdapter.OnFontInstall() {
            @Override
            public void onFontInstall(String str) {
                keyDataHolder.putBoolean("font_" + str, true);
                fancyFontsAdapter.notifyItemRangeChanged(0, fancyFontsAdapter.getItemCount());
                if (!KeyboardSupport.INSTANCE.isThisKeyboardSetAsDefaultIME(FancyFontActivity.this)) {
                    Toast.makeText(getApplicationContext(), "Please set this keyboard as default to use this font.", 1).show();
                }
                navigate(null, 0);
            }
        });
        this.fancyFontsRV.setAdapter(fancyFontsAdapter);

    }

    public void navigate(Intent intent, int i) {
        AdManager.startActivity(this, intent, i);

    }
}
