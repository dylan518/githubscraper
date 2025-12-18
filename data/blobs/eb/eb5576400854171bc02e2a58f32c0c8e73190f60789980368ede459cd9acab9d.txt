package models;

import static org.junit.jupiter.api.Assertions.*;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class EnvioTest {
	
	private Envio envio1;
	private Envio envio2;
	
	private Producto producto1;
	private Producto producto2;
	private Producto producto3;
	
	private List<Producto> lista1;
	
	private Donacion donacion1;
	
	private Volumen volumen1;
	
	private ResumenEnvio resumen1;
	private ResumenEnvio resumen2;
	private ResumenEnvio resumen3;
	private ResumenEnvio resumen4;
	private ResumenEnvio resumen5;
	
	private List<ResumenEnvio> listaResumen1;
	
	private LocalDate fechaDisponible1;
	private LocalDate fechaDisponible2;
	private LocalDate fechaDisponible3;
	
	private DescripcionDetallada detallada1;
	private DescripcionDetallada detallada2;
	private DescripcionGeneral general1;
	
	
	@BeforeEach
	public void setup() {
		producto1=new Producto("pan", 48);
		producto2=new Producto("chorizo", 64);
		producto3=new Producto("huevo", 135);
		//----------------------------------------------
		lista1=new ArrayList<Producto>();
		//productos con final par
		lista1.add(producto1);
		lista1.add(producto2);
		lista1.add(producto3);
		
		//----------------------------------------------donaciones---
		fechaDisponible1= LocalDate.of(2022, 10, 23);
		detallada1=new DescripcionDetallada(lista1);
		donacion1=new Donacion("estado", fechaDisponible1,detallada1);
		
		general1=new DescripcionGeneral(volumen1,"caracteristicas");
		donacion1=new Donacion("estado", fechaDisponible3,general1);
		//--------------------------------------------resumen--------
		resumen1=new ResumenEnvio("pan", 15.3);
		resumen2=new ResumenEnvio("chorizo", 4.0);
		resumen3=new ResumenEnvio("huevo",6.0);
		//-------------------------------listados de resumenes ------
		listaResumen1=new ArrayList<ResumenEnvio>();
		//----------------
		listaResumen1.add(resumen1);
		listaResumen1.add(resumen2);
		//-------------------
		listaResumen1.add(resumen3);
		//-------------------
		volumen1=new Volumen(2.0, 3.0, 9.0);
		
		//lista productos/productos--/donacion/volumen/lista resumenEnvio
		envio1=new Envio(lista1, donacion1, volumen1, listaResumen1);
	

	}

	@Test
	public void testCambiarEstado(){
		assertEquals(envio1.getEstado(),"pendiente de retiro");
		envio1.cambiarEstado("otroEstado");
		assertEquals(envio1.getEstado(), "otroEstado");
	}
	
	@Test
	public void testObtenerElPesoDelEnvio(){
		assertEquals(envio1.obtenerElPesoDelEnvio(),25.3);
		
	}
	
	@Test
	public void testId() {
		assertEquals(this.envio1.getId(), 1);
		this.envio2 = new Envio(lista1, donacion1, volumen1, listaResumen1);
		assertEquals(this.envio2.getId(), 2);
	}

}
