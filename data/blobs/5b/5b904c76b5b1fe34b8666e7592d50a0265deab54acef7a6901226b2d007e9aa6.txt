package com.example.bottomlayout;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentResultListener;
import androidx.navigation.NavDirections;
import androidx.navigation.fragment.NavHostFragment;

import com.example.bottomlayout.databinding.FragmentChooseBinding;

public class ChooseFragment extends Fragment {
    private FragmentChooseBinding binding;
    private TextView txtOrder;


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        binding = FragmentChooseBinding.inflate(inflater);
        return binding.getRoot();
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        txtOrder = view.findViewById(R.id.txt_order);

        getParentFragmentManager().setFragmentResultListener("selectedValue", this, new FragmentResultListener() {
            @Override
            public void onFragmentResult(@NonNull String requestKey, @NonNull Bundle result) {
                // Menerima hasil dari CheckoutFragment
                String selectedValue = result.getString("selectedValue");

                // Mengatur nilai TextView dengan nilai yang diterima
                if (selectedValue != null) {
                    txtOrder.setText("Your Ticket" + " " + selectedValue + " " + "Successfully booked!");
                }
            }
        });

        // Tambahkan listener untuk menangani peristiwa klik pada TextView
        txtOrder.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Pindah ke CheckoutFragment
                NavDirections action = ChooseFragmentDirections.actionChooseFragmentToCheckoutFragment();
                NavHostFragment.findNavController(ChooseFragment.this).navigate(action);
            }
        });
    }
}
