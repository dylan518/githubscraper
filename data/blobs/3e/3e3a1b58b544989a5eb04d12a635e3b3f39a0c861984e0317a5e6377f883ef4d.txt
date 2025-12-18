package model;

public class ModelEuclide {


    private int dividende;
    private int diviseur;
    private int quotient;
    private int reste;

    public ModelEuclide() {
        this.dividende = 0;
        this.diviseur = 0;
        this.quotient = 0;
        this.reste = 0;
    }

    public void generate() {
        this.dividende = Model.random.nextInt(-Model.BOUND, Model.BOUND);
        this.diviseur = Model.random.nextInt(-Model.BOUND, Model.BOUND);
        if (abs(this.dividende) < abs(this.diviseur)) {
            int var = this.dividende;
            this.dividende = this.diviseur;
            this.diviseur = var;
        }

        if (this.diviseur == 0)
            this.diviseur ++;

        this.quotient = this.dividende/this.diviseur;

        this.reste = this.dividende - this.diviseur*this.quotient;

        while (this.reste < 0 || this.reste > abs(this.diviseur)) {
            if (this.quotient > 0)
                this.quotient += 1;
            else
                this.quotient -= 1;
            this.reste = this.dividende - this.diviseur*this.quotient;
        }
    }

    public int abs(int nb) {
        if (nb < 0)
            return -nb;
        return nb;
    }

    public boolean verifReponse(int quotient, int reste) {
        return this.quotient == quotient && this.reste == reste;
    }

    public int getDividende() {
        return this.dividende;
    }

    public int getDiviseur() {
        return this.diviseur;
    }

    public int getQuotient() {
        return this.quotient;
    }

    public int getReste() {
        return this.reste;
    }
}
