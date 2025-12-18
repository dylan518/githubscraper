package sv.edu.utec.recicleview;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
RecyclerView mrecyclerView;
Adaptador adaptador;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    mrecyclerView = findViewById(R.id.rvPeliculas);
    mrecyclerView.setLayoutManager(new LinearLayoutManager(this));
        adaptador = new Adaptador(this, getListado());
    mrecyclerView.setAdapter(adaptador);

        /*mrecyclerView.setOnClickListener(new View.OnClickListener() {
                                             @Override
                                             public void onClick(View v) {
                                                 Toast.makeText(getApplicationContext(), "prueba",Toast.LENGTH_LONG).show();
                                             }
                                         });
*/
        mrecyclerView.setOnHoverListener(new View.OnHoverListener() {
            @Override
            public boolean onHover(View v, MotionEvent event) {
                Toast.makeText(getApplicationContext(),"Selecionar",Toast.LENGTH_SHORT).show();
                return false;
            }
        });

      /*  adaptador.set (new AdapterView.OnItemClickListener() {
                                             @Override
                                             public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                                                 Toast.makeText(parent.getContext(),"seleccionar",Toast.LENGTH_LONG).show();
                                             }
                                         });
*/

    }
    private ArrayList<Modelo> getListado(){
        ArrayList<Modelo> modelos=new ArrayList<>();
        Modelo modelista = new Modelo();
        modelista.setNombrePeli("Ex-Maquina");
        modelista.setDirectorPeli("Juan Perez");
        modelista.setGeneroPeli("Ciencia ficcion");
        modelista.setImgPeli(R.drawable.ex_maquina);
        modelista.setClasificar(3.45);
        modelista.setDuracionPeli("108 min");
        modelista.setAnioPeli("1999");
        modelos.add(modelista);


        modelista = new Modelo();
        modelista.setNombrePeli("La LLegada");
        modelista.setDirectorPeli("Juan Perez");
        modelista.setGeneroPeli("Ciencia ficcion");
        modelista.setImgPeli(R.drawable.la_llegada);
        modelista.setClasificar(3.45);
        modelista.setDuracionPeli("108 min");
        modelista.setAnioPeli("1999");
        modelos.add(modelista);

        modelista = new Modelo();
        modelista.setNombrePeli("Jumanji");
        modelista.setDirectorPeli("Juan Perez");
        modelista.setGeneroPeli("Ciencia ficcion");
        modelista.setImgPeli(R.drawable.jumanji);
        modelista.setClasificar(3.45);
        modelista.setDuracionPeli("108 min");
        modelista.setAnioPeli("1999");
        modelos.add(modelista);

        modelista = new Modelo();
        modelista.setNombrePeli("Inter Estelar");
        modelista.setDirectorPeli("Juan Perez");
        modelista.setGeneroPeli("Ciencia ficcion");
        modelista.setImgPeli(R.drawable.interestelar);
        modelista.setClasificar(3.45);
        modelista.setDuracionPeli("108 min");
        modelista.setAnioPeli("1999");
        modelos.add(modelista);

        modelista = new Modelo();
        modelista.setNombrePeli("Forma de Agua");
        modelista.setDirectorPeli("Juan Perez");
        modelista.setGeneroPeli("Ciencia ficcion");
        modelista.setImgPeli(R.drawable.forma_agua);
        modelista.setClasificar(3.45);
        modelista.setDuracionPeli("108 min");
        modelista.setAnioPeli("1999");
        modelos.add(modelista);

        modelista = new Modelo();
        modelista.setNombrePeli("Extraordinario");
        modelista.setDirectorPeli("Juan Perez");
        modelista.setGeneroPeli("Ciencia ficcion");
        modelista.setImgPeli(R.drawable.extraordinario);
        modelista.setClasificar(3.45);
        modelista.setDuracionPeli("108 min");
        modelista.setAnioPeli("1999");
        modelos.add(modelista);

        return modelos;
    }


}