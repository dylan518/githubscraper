package arbolbinario;

public class ClienteMain {
    public static void main(String[] args) {
        ArbolBinario ab= new ArbolBinario();
        //crear un arbol
        Nodo nodoA= new Nodo("A");
        Nodo nodoB= new Nodo("B");
        Nodo nodoC= new Nodo("C");
        Nodo nodoD= new Nodo("D");
        Nodo nodoE= new Nodo("E");
        Nodo nodoF= new Nodo("F");
        Nodo nodoG= new Nodo("G");
        ab.setRaiz(nodoA);
        ab.getRaiz().setIzquierdo(nodoB);
        ab.getRaiz().setDerecho(nodoC);
        nodoB.setDerecho(nodoE);
        nodoB.setIzquierdo(nodoD);
        nodoC.setIzquierdo(nodoF);
        nodoC.setDerecho(nodoG);
        //Imprimir los recorridos
        System.out.println("Preorden");
        ab.preorden();
        System.out.println("\nPreorden Iterativo");
        ab.preordenIterativo();

        System.out.println("\nInOrden");
        ab.inorden();
        System.out.println("\nInOrden Iterativo");
        ab.inordenIterativa();

        System.out.println("\nPostOrden");
        ab.postorden();

        System.out.println("\nPostOrdenIterativo");
        ab.recorridoPorNiveles();
    }
}
