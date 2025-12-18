package flixnet;

/**
 * Class: Serie
 * * Inherits from class Contenido and adds new features such as attributes to 
 * store the number of seasons and if it's finished
 * @author Néstor M
 */
public class Serie extends Contenido{
//ATTRIBUTES    
    private int nTemporadas;
    private boolean finalizada;
    
//CONSTRUCTOR
/**
 * Constructor
 * @param titulo Title of the series
 * @param productora Publisher of the series
 * @param anio Year of publication
 * @param nTemporadas Number of seasons
 * @param finalizada Boolean to stablish if it's finished
 */    
    public Serie(String titulo, String productora, int anio,
            int nTemporadas, boolean finalizada) {
            super(titulo, productora, anio);
        try{    
            this.setNTemporadas(nTemporadas);
            this.finalizada = finalizada;
        }catch(Exception e){
            System.err.println("ERROR: El número de temporadas no puede "
                    + "ser negativo.");
        }
    }
        
    
//GETTERS & SETTERS
    /**
     * Getter
     * @return Number of seasons
     */
    public int getNTemporadas() {
        return nTemporadas;
    }
    /**
     * Setter
     * @param nTemporadas Number of seasons
     * @throws Exception If the number of seasons is less than 0
     */
    public void setNTemporadas(int nTemporadas) throws Exception{
        if(nTemporadas <= 0) {
            throw new Exception("ERROR: El número de temporadas no puede "
                    + "ser negativo.");
        }
        this.nTemporadas = nTemporadas;
    }
    /**
     * Getter
     * @return Boolean of the status of the series (finished or not)
     */
    public boolean isFinalizada() {
        return finalizada;
    }
}