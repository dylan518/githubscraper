package modelos;

import java.time.LocalDate;
import java.util.Objects;

public class RegistrosDatosDia {

	
	private long id ; 
	private LocalDate fecha ; 
	private double tempMax ; 
	private double tempMin ; 
	private double tempMedia ;
	
	
	
	public RegistrosDatosDia() {
		super();
	}



	public RegistrosDatosDia(long id, LocalDate fecha, double tempMax, double tempMin, double tempMedia) {
		super();
		this.id = id;
		this.fecha = fecha;
		this.tempMax = tempMax;
		this.tempMin = tempMin;
		this.tempMedia = tempMedia;
	}



	/**
	 * @return the id
	 */
	public long getId() {
		return id;
	}



	/**
	 * @param id the id to set
	 */
	public void setId(long id) {
		this.id = id;
	}



	/**
	 * @return the fecha
	 */
	public LocalDate getFecha() {
		return fecha;
	}



	/**
	 * @param fecha the fecha to set
	 */
	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}



	/**
	 * @return the tempMax
	 */
	public double getTempMax() {
		return tempMax;
	}



	/**
	 * @param tempMax the tempMax to set
	 */
	public void setTempMax(double tempMax) {
		this.tempMax = tempMax;
	}



	/**
	 * @return the tempMin
	 */
	public double getTempMin() {
		return tempMin;
	}



	/**
	 * @param tempMin the tempMin to set
	 */
	public void setTempMin(double tempMin) {
		this.tempMin = tempMin;
	}



	/**
	 * @return the tempMedia
	 */
	public double getTempMedia() {
		return tempMedia;
	}



	/**
	 * @param tempMedia the tempMedia to set
	 */
	public void setTempMedia(double tempMedia) {
		this.tempMedia = tempMedia;
	}



	@Override
	public String toString() {
		return "RegistrosDatosDia [id=" + id + ", fecha=" + fecha + ", tempMax=" + tempMax + ", tempMin=" + tempMin
				+ ", tempMedia=" + tempMedia + "]";
	}



	@Override
	public int hashCode() {
		return Objects.hash(id);
	}



	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		RegistrosDatosDia other = (RegistrosDatosDia) obj;
		return id == other.id;
	} 
	
	
	
	
}

