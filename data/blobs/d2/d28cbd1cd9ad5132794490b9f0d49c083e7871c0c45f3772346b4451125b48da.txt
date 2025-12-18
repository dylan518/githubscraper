package com.example.trabalhogrupon2;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.FirebaseDatabase;

public class Cadastro extends AppCompatActivity implements View.OnClickListener{

    private EditText editNome, editIdade, editEmail, editSenha;
    private Button botaoCadastrar;
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cadastro_usuario);

        mAuth = FirebaseAuth.getInstance();

        botaoCadastrar = findViewById(R.id.btCadastrar);
        botaoCadastrar.setOnClickListener(this);

        editNome = (EditText) findViewById(R.id.etNome);
        editIdade = (EditText) findViewById(R.id.etIdade);
        editEmail = (EditText) findViewById(R.id.etEmail);
        editSenha = (EditText) findViewById(R.id.etSenha);



    }

    @Override
    public void onClick(View view) {
        switch(view.getId()){
            case R.id.btCadastrar:
                registrarUsuario();
                break;
        }
    }

    private void registrarUsuario(){
        String email = editEmail.getText().toString().trim();
        String senha = editSenha.getText().toString().trim();
        String nome = editNome.getText().toString().trim();
        String idade = editIdade.getText().toString().trim();

        if(nome.isEmpty()){
            editNome.setError("Nome é obrigatório!");
            editNome.setError("Nome é obrigatório!");
            return;
        }

        if(idade.isEmpty()){
            editIdade.setError("Idade é obrigatório!");
            editIdade.setError("Idade é obrigatório!");
            return;
        }

        if(email.isEmpty()){
            editEmail.setError("Email é obrigatório!");
            editEmail.setError("Email é obrigatório!");
            return;
        }

        if(senha.isEmpty()){
            editSenha.setError("Senha é obrigatório!");
            editSenha.setError("Senha é obrigatório!");
            return;
        }

        mAuth.createUserWithEmailAndPassword(email, senha)
            .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                @Override
                public void onComplete(@NonNull Task<AuthResult> task) {
                    if(task.isSuccessful()) {
                        UsuarioModel usuario = new UsuarioModel(nome, idade, email);

                        FirebaseDatabase.getInstance().getReference("Users")
                                .child(FirebaseAuth.getInstance().getCurrentUser().getUid())
                                .setValue(usuario).addOnCompleteListener(new OnCompleteListener<Void>() {
                            @Override
                            public void onComplete(@NonNull Task<Void> task) {
                                if(task.isSuccessful()) {
                                    Toast.makeText(Cadastro.this, "Usuário cadastrado com sucesso!", Toast.LENGTH_LONG).show();

                                }else {
                                    Toast.makeText(Cadastro.this, "Falha ao cadastrar usuário.", Toast.LENGTH_LONG).show();
                                }
                            }
                        });
                    }
                }
            });

        }
    }