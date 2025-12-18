package co.edu.cue.finalprojectbarber.model;

public class Barberq extends Person {

    public Barberq() {
        super();
    }
    private double earning;

    public double getEarning() {
        return earning;
    }

    public void setEarning(double earning) {
        this.earning = earning;
    }

    public Barberq(String name, String password,String email,double earning) {
        super(name,password,email);
        this.earning = earning;
    }
}
