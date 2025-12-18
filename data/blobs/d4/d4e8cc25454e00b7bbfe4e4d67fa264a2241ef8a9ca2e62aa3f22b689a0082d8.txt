package CuentaBancaria;

public class CuentaBancaria {
    //atributo de la clase
    private double saldoCuentaCorriente;
    private double saldoAhorros;
    public static int cantidadCuentasCreadas = 0;
    private double totalEntreSaldos;

    
    public CuentaBancaria(){
        //atributos de objeto
        this.saldoCuentaCorriente = 0;
        this.saldoAhorros = 0;
        this.totalEntreSaldos = 0;
        cantidadCuentasCreadas++;
    }

    public CuentaBancaria(double saldoCuentaCorriente, double saldoAhorros){
        //atributos de objeto
        this.saldoCuentaCorriente = saldoCuentaCorriente;
        this.saldoAhorros = saldoAhorros;
        this.totalEntreSaldos = saldoAhorros + saldoCuentaCorriente;
        cantidadCuentasCreadas++;
    }

    public double getsaldoCuentaCorriente(){
        return this.saldoCuentaCorriente;
    }

    public double getSaldoCuentaAhorros(){
        return this.saldoAhorros;
    }

    public void depositarDinero(String cuenta, double deposito){
        this.totalEntreSaldos =+ deposito;
        if(cuenta.equals("corriente")){
            this.saldoCuentaCorriente += deposito;
        }
        else if(cuenta.equals("ahorros")){
            this.saldoAhorros += deposito;
        }
    }

    public void retirarDinero(String cuenta, double retiro){
        this.totalEntreSaldos -= retiro;
        if(cuenta.equals("corriente")){
            this.saldoCuentaCorriente -= retiro;
        }
        else if(cuenta.equals("ahorros")){
            this.saldoAhorros -= retiro;
        }
    }

    public void totalSaldo(){
        System.out.println("Tu saldo actual es: "+"$" this.totalEntreSaldos);
    }

}
