


/**
 * 
 * <p>
 * This is a tools class. 
 *
 * </p>
 * 
 * @author Ajani Small, Alyssa Blades, Shane Foster
 */

public class Tools 
{
    private int data[], key[];
    private final int COLUMN_SIZE = 10;

    public Tools()
    {
        data = new int[ COLUMN_SIZE ];
        key = new int[ COLUMN_SIZE ];
    }

    
    /** 
     * Rounds an integer value
     * @param value
     * @return int
     */
    public int round(int value)
    {
        int placeValue = value % 10;   //Value in ones place
        int pivot = 5;                          

        //Change pivot if value is greater than 10 and unit value is zero
        if (value >= 10 && placeValue == 0){
            pivot = 50;
            placeValue = (value - placeValue);
        }
        
        //Round
        if (placeValue >= pivot){
            return value + 1;
        }else{
            return value - 1;
        }
        

    }

    
    /** 
     * Rounds all values in an array
     * @param values[]
     */
    public void round(int values[])
    {
        for (int i = 0; i < values.length; i++){
            values[i] = round(values[i]);
        }
       
    }

    
    /** 
     * Encrypts the values in an array using the modulus operator
     * @param values[]
     * @param mod
     * @return int
     */
    public int encrypt(int values[], int mod)
    {
        if(values.length != key.length) {
            key = new int[values.length];
        }
        for(int i = 0; i < values.length; i++){
            key[i] = (values[i] % mod);
            values[i] = (int)(values[i] / mod);
        }
        return 0;
    }

    
    /** 
     * Decrypts the values in an array using the modulus operator
     * @param values[]
     * @param mod
     * @return int
     */
    public int decrypt(int values[], int mod)
    {
        for(int i = 0; i < values.length; i++){
            values[i] = (values[i] * mod) + key[i];
        }
        return 0;
    }

    
    /** 
     * Sets all values in an array to 0 if any of three conditions are met
     * @param values[]
     * @param match
     */
    public void clear(int values[], int match)
    {   
        
        for(int  i = 0; i < values.length; i++){
            if (
                (match == 0)                   || 
                (match == -1 && values[i] < 0) ||
                (match == 1 && values[i] > 0)  ||
                (match > 0 && values[i] % match == 0)
            ){
                values[i] = 0;
            }
        }
        
    }

    
    /** 
     * Manually copies all the values in an array to the field, data.
     * @param values[]
     */
    public void copy(int values[])
    {
        if(values.length != data.length) {
            data = new int[values.length];
        }
        for(int i = 0; i < values.length; i++){
            data[i] = values[i];
        }
    }

    //---------- DO NOT MODIFY THE CODE BELOW ----------
    public void setData(int col, int value)
    {
        data[col] = value;
    }

    public int getData(int col)
    {
        return data[col];
    }

    public void setKey(int col, int value)
    {
        key[col] = value;
    }

    public int getKey(int col)
    {
        return key[col];
    }

    public void display()
    {
        System.out.print("Data: ");
        for(int i = 0; i < COLUMN_SIZE; i++)
        {
            System.out.print( data[ i ] + "\t");
        }
        System.out.println("");
        System.out.print("Key : ");
        for(int i = 0; i < COLUMN_SIZE; i++)
        {
            System.out.print( key[ i ] + "\t");
        }
        System.out.println("");
    }
}

