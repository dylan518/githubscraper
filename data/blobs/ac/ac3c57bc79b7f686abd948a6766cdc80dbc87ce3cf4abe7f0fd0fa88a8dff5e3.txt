package com.example.livelocation;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.tasks.OnSuccessListener;

import java.io.IOException;
import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    FusedLocationProviderClient fusedLocationProviderClient;
    TextView log,lati,address,city,country;
    private final static int REQUEST_CODE=100;
    Button getLocation;

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if(requestCode==REQUEST_CODE){
            if(grantResults.length>0 && grantResults[0]==PackageManager.PERMISSION_GRANTED){
               getLocation();
            }
            else {
                Toast.makeText(this, "Please Provide Permission", Toast.LENGTH_SHORT).show();
            }
        }


        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    }

    private void getLocation() {
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        log=findViewById(R.id.log);
        lati=findViewById(R.id.lat);
        address=findViewById(R.id.address);
        city=findViewById(R.id.city);
        country=findViewById(R.id.country);
        getLocation=findViewById(R.id.getLocation);
        fusedLocationProviderClient = LocationServices.getFusedLocationProviderClient(this);



        if(ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.ACCESS_FINE_LOCATION)== PackageManager.PERMISSION_GRANTED){

            fusedLocationProviderClient.getLastLocation()
                    .addOnSuccessListener(new OnSuccessListener<Location>() {
                        @Override
                        public void onSuccess(Location location) {
                            if(location!=null){
                                Geocoder geocoder=new Geocoder(MainActivity.this, Locale.getDefault());
                                List<Address> addresses=null;

                                try {
                                    addresses=geocoder.getFromLocation(location.getLatitude(),location.getLongitude(),1);
                                    log.setText("Longitude  : "+addresses.get(0).getLongitude());
                                    lati.setText("Latitude  : "+addresses.get(0).getLatitude());
                                    country.setText("Country  : "+addresses.get(0).getCountryName());
                                    address.setText("Address  : "+addresses.get(0).getAddressLine(0));
                                    city.setText("City  : "+addresses.get(0).getLocality());

                                }
                                catch (IOException e){
                                    e.printStackTrace();
                                }

                            }
                        }
                    });
        }

        else {
            askpermission();
        }

//
    }

    private void askpermission() {


        ActivityCompat.requestPermissions(MainActivity.this,new String[]{Manifest.permission.ACCESS_FINE_LOCATION},REQUEST_CODE);

    }



//        getLocation();
//        getLocation.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                getLocation();
//            }
//
//            public void getLocation() {
//
//                if(ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.ACCESS_FINE_LOCATION)== PackageManager.PERMISSION_GRANTED){
//
//                    fusedLocationProviderClient.getLastLocation()
//                            .addOnSuccessListener(new OnSuccessListener<Location>() {
//                                @Override
//                                public void onSuccess(Location location) {
//                                    if(location!=null){
//                                        Geocoder geocoder=new Geocoder(MainActivity.this, Locale.getDefault());
//                                        List<Address> addresses=null;
//
//                                        try {
//                                            addresses=geocoder.getFromLocation(location.getLatitude(),location.getLongitude(),1);
//                                            log.setText("Longitude  : "+addresses.get(0).getLongitude());
//                                            lati.setText("Latitude  : "+addresses.get(0).getLatitude());
//                                            country.setText("Country  : "+addresses.get(0).getCountryName());
//                                            address.setText("Address  : "+addresses.get(0).getAddressLine(0));
//                                            city.setText("City  : "+addresses.get(0).getLocality());
//
//                                        }
//                                        catch (IOException e){
//                                            e.printStackTrace();
//                                        }
//
//                                    }
//                                }
//                            });
//                }
//
//                else {
//                    askpermission();
//                }
//            }
//
//            private void askpermission() {
//
//
//                ActivityCompat.requestPermissions(MainActivity.this,new String[]{Manifest.permission.ACCESS_FINE_LOCATION},REQUEST_CODE);
//
//            }
//        });



    }
