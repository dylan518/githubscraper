/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

package conexionBD.clasesDAO.clasesObjetivosDAO;

/**
 * 
 * @author Sammy Guergachi <sguergachi at gmail.com>
 */
public class UsuarioRegPesoDAO {
    private int idUsuarioRegPeso;
    private int idRegistroPeso;
    private int idUsuario;

    public UsuarioRegPesoDAO() {
    }

    public UsuarioRegPesoDAO(int idUsuarioRegPeso) {
        this.idUsuarioRegPeso = idUsuarioRegPeso;
    }

    public UsuarioRegPesoDAO(int idUsuarioRegPeso, int idRegistroPeso, int idUsuario) {
        this.idUsuarioRegPeso = idUsuarioRegPeso;
        this.idRegistroPeso = idRegistroPeso;
        this.idUsuario = idUsuario;
    }

    public String insertar() {
        return "INSERT INTO usuario_reg_peso(idUsuarioRegPeso, idRegistroPeso, idUsuario) VALUES(" + this.idUsuarioRegPeso + ", " + this.idRegistroPeso + ", " + this.idUsuario + ")";
    }

    public String consultar() {
        return "SELECT * FROM usuario_reg_peso WHERE idUsuarioRegPeso = " + this.idUsuarioRegPeso;
    }

    public String actualizar() {
        return "UPDATE usuario_reg_peso SET idRegistroPeso = " + this.idRegistroPeso + ", idUsuario = " + this.idUsuario + " WHERE idUsuarioRegPeso = " + this.idUsuarioRegPeso;
    }

    public String eliminar() {
        return "DELETE FROM usuario_reg_peso WHERE idUsuarioRegPeso = " + this.idUsuarioRegPeso;
    }
}
