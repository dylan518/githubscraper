package packetePila;

public class clsPilaArr {



    private int pila[];
    private int tope;
    private int tamPila;
    private int cant;
    private String pilastr[];
    private char pilachar[];

    clsPilaArr(int tamPila) {
            this.tamPila = tamPila;
            this.pilastr = new String[this.tamPila];
            limpiaPila();
    }

    clsPilaArr(int tamPila, int cod) {
            this.tamPila = tamPila;
            this.pilastr = new String[this.tamPila];
            limpiaPila();
    }

    clsPilaArr(int tamPila, String cod) {
            this.tamPila = tamPila;
            this.pilachar = new char[this.tamPila];
            limpiaPila();
    }

    public int get_tampila() {
            return this.tamPila;
    }

    public void limpiaPila() {
            this.tope = -1;
    }

    public boolean pilaLlena() {
            return (this.tope == this.tamPila - 1);
    }

    public boolean pilaVacia() {
            return (this.tope == -1);
    }

    private void incrementaTope() {
            this.tope++;
    }

    private void decrementaTope() {
            this.tope--;
    }

    void restablecertope(int tope) {
            this.tope = tope;
    }

    int sacar() {
            int elemento = -9999;
            if (!pilaVacia()) {
                    elemento = this.pila[this.tope];
                    decrementaTope();
            } else {
                    System.out.println("Error. Pila vacia...");
            }
            return elemento;
    }

    public int getCant() {
            return cant;
    }

    String get_ultimostr() {
            String elemento = "";
            if (!pilaVacia()) {
                    elemento = this.pilastr[this.tope];
            } else {
                    System.out.println("Error. Pila vacia...");
            }
            return elemento;
    }

    int get_ultimoint() {
            int elemento = -9999;
            if (!pilaVacia()) {
                    elemento = this.pila[this.tope];
            } else {
                    System.out.println("Error. Pila vacia...");
            }
            return elemento;
    }

    String sacarstr() {
            String elemento = "";
            if (!pilaVacia()) {
                    elemento = this.pilastr[this.tope];
                    decrementaTope();
            } else {
                    System.out.println("Error. Pila vacia...");
            }
            return elemento;
    }

    char sacarchar() {
            char elemento = (char) -9999;
            if (!pilaVacia()) {
                    elemento = this.pilachar[this.tope];
                    decrementaTope();
            } else {
                    System.out.println("Error. Pila vacia...");
            }
            return elemento;
    }

    public void mostrarPila() {
            int i=tamPila;
            while (!pilaVacia()) {
                    int elemAux = sacar();
                    if (elemAux!=-99999) {
                            System.out.println("La pila contiene: " + elemAux);
                    }
            }
    }

    boolean palindroma(String palabra) {
            String pal_reves = "";
            for (int i = 0; i < this.pilastr.length; i++) {	
                    pal_reves = pal_reves + this.sacarstr();
            }
            return (palabra.equals(pal_reves));
    }

    void quitar_pares(clsPilaArr pila) {
            int nro;
            for (int i = this.tope; i>=0 ;i--){
                    nro = this.sacar();
                    if ((i%2)!=0) {
                            pila.poner(nro);
                    }
            }
    }

    void invertir(clsPilaArr pila, int tam) {
            int num;
            for (int i = 0; i < tam;i++) {
                    num = this.sacar();
                    pila.poner(num);
            }
    }

    void invertirstr(clsPilaArr pila, int tam) {
            String caracter;
            for (int i = 0; i < tam;i++) {
                    caracter = this.sacarstr();
                    pila.ponerstr(caracter);
            }
    }

    void poner(int elemento) {
            if (!pilaLlena()) {
                    incrementaTope();
                    this.pila[this.tope] = elemento;
            } else {
                    System.out.println("Error. Pila llena...");
            }
    }

    void ponerstr(String elemento){
            if (!pilaLlena()){
                    incrementaTope();	
                    this.pilastr[this.tope] = elemento;					
            } else {
                    System.out.println("Error. Pila llena...");
            }	
    }

    void ponerchar(char elemento){
            if (!pilaLlena()){
                    incrementaTope();	
                    this.pilachar[this.tope] = elemento;					
            } else {
                    System.out.println("Error. Pila llena...");
            }	
    }

    public boolean validar_eq(clsPilaArr pila) {
            String palabra = "", letra = "";
            for (int i = 0; i < this.tamPila ;i++) {
                    letra = this.sacarstr();
                    palabra = palabra + letra;
            }
            for (int i = 0; i < palabra.length() ;i++) {
                    if (String.valueOf(palabra.charAt(i)).equals("(") || String.valueOf(palabra.charAt(i)).equals("[") || String.valueOf(palabra.charAt(i)).equals("{")) {
                            pila.ponerstr(String.valueOf(palabra.charAt(i)));
                    } else {
                            if (String.valueOf(palabra.charAt(i)).equals(")")) {
                                    if (!pila.sacarstr().equals("(")) {
                                            return false;
                                    }
                            } else {
                                    if (String.valueOf(palabra.charAt(i)).equals("]")){
                                            if(!pila.sacarstr().equals("[")) {
                                                    return false;
                                            }
                                    }else {
                                            if (String.valueOf(palabra.charAt(i)).equals("}")) {
                                                    if (!pila.sacarstr().equals("{")) {
                                                            return false;
                                                    }

                                            }
                                    }
                            }
                    }
            }
            return pila.pilaVacia();
    }
}
