package controlador;

import vista.*;

import javax.swing.JFrame;

//import com.mysql.cj.x.protobuf.MysqlxDatatypes.Scalar.String;
//esta clase da un error de com/google/...

import modelo.*;

public class Main {
	public static void main(String[] args) {
		Controlador miControlador = new Controlador();
		Modelo miModelo = new Modelo();
		Vistas[] misVistas = new Vistas[8];

		misVistas[0] = new _00_Login();
		misVistas[1] = new _01_Registro();
		misVistas[2] = new _02_Hoyos();
		misVistas[3] = new _03_Admin();
		misVistas[4] = new _04_Admin_Panel();
		misVistas[5] = new _05_Ajuste();
		misVistas[6] = new _06_Contactanos_Panel();
		misVistas[7] = new _07_Preguntas_Panel();

		miModelo.setVistas(misVistas);

		miControlador.setVista(misVistas);
		miControlador.setModelo(miModelo);

		for (Vistas vista : misVistas) {
			vista.setModelo(miModelo);
			vista.setControlador(miControlador);
		}

		((JFrame) misVistas[0]).setVisible(true);

	}

}
