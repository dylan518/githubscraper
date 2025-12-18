package Repositorio;

import Dominio.Usuario;
import Persistencia.UsuarioJpaController;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.swing.JOptionPane;

public class UsuarioRepositorio {

    public static UsuarioJpaController repositorio = new UsuarioJpaController();

    public void crear(Usuario usuario) {

        try {
            if (encontrarUsuario(usuario.getUsuario()) != null) {
                throw new Exception("El usuario ya ase encuentra en la BD");
            }
            repositorio.create(usuario);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error: " + e.getMessage());
        }
    }

    public void editar(Usuario usuario) {
        try {
            if (encontrarUsuario(usuario.getUsuario()) == null) {
                throw new Exception("El usuario no se encuentra en la BD");
            }
            repositorio.edit(usuario);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error: " + e.getMessage());
        }
    }

    public void destruir (String usuario) {
        Usuario encontrado = encontrarUsuario(usuario);
        try {
            if ( encontrado == null) {
                throw new Exception("El usuario no se encuentra en la BD");
            }
            repositorio.destroy(encontrado.getId());
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error: " + e.getMessage());
        }
    }

    public Usuario buscar(String usuario) {
        Usuario encontrado = encontrarUsuario(usuario);
        try {
            if (encontrado == null) {
                throw new Exception("El usuario no se encuentra en la BD");

            }
            return repositorio.findUsuario(encontrado.getId());
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Error: " + e.getMessage());
            return null;
        }        
        
    }

    public List<Usuario> buscarTodo() {
        return repositorio.findUsuarioEntities();
    }
    
    public int contarTodoUsuario(){        
        return repositorio.getUsuarioCount();
    }

    public Usuario encontrarUsuario(String codigo) {
        Usuario encontrado = null;

        List<Usuario> lista = buscarTodo();

        Map<String, Usuario> listaUsuarios = new HashMap<>();

        for (Usuario entry : lista) {
            listaUsuarios.put(entry.getUsuario(), entry);
        }

        encontrado = listaUsuarios.get(codigo);

        if (encontrado != null) {
            return encontrado;
        } else {
            return null;
        }
    }

    public Usuario IniciarSesion(String usuario, String passwd) throws Exception {

        try {
            Usuario usr = encontrarUsuario(usuario);

            if (usr == null) {
                throw new Exception("No se encontro el Usuario");
            }

            System.out.println(usr.toString());

            if (!(passwd.equals(usr.getContrasena()))) {
                throw new Exception("La clave es incorrecta");
            }

            return usr;

        } catch (Exception e) {

            JOptionPane.showMessageDialog(null, "Error: " + e.getMessage());
            System.out.println("Error: " + e.getMessage());
            return null;
        }
        
        
    }
    
    public Usuario validarContraseña(String usuario,String contrasena){
        List<Usuario> listaUsuarios = buscarTodo();

        Map<String,Usuario> map = new HashMap<>();

        for (Usuario op: listaUsuarios){
            map.put(op.getUsuario(), op);
        }

       Usuario buscar = map.get(usuario);

        if (contrasena.equals(buscar.getContrasena())) {
            return buscar;
        }else{
        return null;
        } 
    }

}
