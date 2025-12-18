package es.studium.myavatar;

import android.widget.Toast;
import android.app.Dialog;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.ArrayAdapter;

import androidx.annotation.NonNull;
import androidx.fragment.app.DialogFragment;

public class DialogoProfesion extends DialogFragment {

    private String nombre;
    private String especie;

    // Constructor con nombre y especie
    public DialogoProfesion(String nombre, String especie) {
        this.nombre = nombre;
        this.especie = especie;
    }

    @NonNull
    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        // Usamos un inflater para inflar el layout del diálogo
        LayoutInflater inflater = getActivity().getLayoutInflater();
        View view = inflater.inflate(R.layout.dialogo_profesion, null);

        Spinner profesionSpinner = view.findViewById(R.id.profesionSpinner);
        Button aceptarButton = view.findViewById(R.id.aceptarButton);

        // Crear un ArrayAdapter para llenar el Spinner
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(
                getActivity(),
                R.array.profesiones_array, // Referencia al array de profesiones
                android.R.layout.simple_spinner_item // Layout para cada ítem
        );
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item); // Estilo del dropdown
        profesionSpinner.setAdapter(adapter);

        // Acción al hacer click en el botón de aceptar
        aceptarButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String profesionSeleccionada = profesionSpinner.getSelectedItem().toString();

                // Validar que no se haya seleccionado la opción predeterminada
                if (!profesionSeleccionada.equals("Selecciona una profesión")) {
                    MainActivity mainActivity = (MainActivity) getActivity();
                    String genero = mainActivity.getAvatar().getGenero();

                    mainActivity.actualizarAvatar(nombre, genero, especie, profesionSeleccionada);
                    dismiss();  // Cerrar el diálogo
                } else {
                    // Mostrar un Toast si no se ha seleccionado una profesión válida
                    Toast.makeText(getActivity(), "Por favor, selecciona una profesión válida.", Toast.LENGTH_SHORT).show();
                }
            }
        });

        return new android.app.AlertDialog.Builder(getActivity())
                .setView(view)
                .create();
    }
}
