package com.biybiruza.news.ui.home;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.util.Log;
import android.view.Display;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import com.biybiruza.news.R;
import com.biybiruza.news.data.Articles;
import com.biybiruza.news.data.Models;
import com.biybiruza.news.databinding.FragmentHomeBinding;
import com.biybiruza.news.networking.ApiClient;
import com.biybiruza.news.networking.ApiService;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class HomeFragment extends Fragment {

    private FragmentHomeBinding binding;
    private AdapterHome adapter;

    public HomeFragment() {
        super(R.layout.fragment_home);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        binding = FragmentHomeBinding.inflate(inflater, container, false);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        apiService();

        binding.etSearch.setOnFocusChangeListener((view1, hasFocus) -> {
            if (hasFocus) {
                NavController navController = Navigation.findNavController(requireActivity(), R.id.nav_host_fragment);
                navController.navigate(R.id.action_mainFragment_to_searchFragment);
            }
        });

    }

    private void apiService(){

        ApiService apiService = ApiClient.getClient().create(ApiService.class);

        Call<Models> getNews = apiService.getNewsList();
        getNews.enqueue(new Callback<Models>() {
            @Override
            public void onResponse(Call<Models> call, Response<Models> response) {
                if (response.isSuccessful()){
                    adapter = new AdapterHome(
                            response.body().getArticles(),
                            new AdapterHome.OnItemClickListener() {
                                @Override
                                public void onItemClick(String url) {
                                    Bundle bundle = new Bundle();
                                    bundle.putString("url",url);
                                    NavController navController = Navigation.findNavController(requireActivity(), R.id.nav_host_fragment);
                                    navController.navigate(R.id.action_mainFragment_to_detailsFragment, bundle);
                                }
                            });

                    RecyclerView.LayoutManager linearLayoutManager =
                            new LinearLayoutManager(requireContext(), LinearLayoutManager.VERTICAL, true);
                    binding.rvHome.setLayoutManager(linearLayoutManager);
                    binding.rvHome.setAdapter(adapter);

                    binding.progressBar.setVisibility(View.GONE);
                }
            }

            @Override
            public void onFailure(Call<Models> call, Throwable t) {
                Log.d("xato", "onFailure: "+t.getMessage());
                Toast.makeText(requireContext(), "xota: "+t.getMessage(), Toast.LENGTH_SHORT).show();
                binding.progressBar.setVisibility(View.GONE);
            }
        });
    }
}