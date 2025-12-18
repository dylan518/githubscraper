package classes.oop;

public class Santuario {

    public static void main(String[] args){
        Animal[] jaula=new Animal[5];
        Caballo potro= new Caballo("mente fria", true);
        jaula[0]=potro;
        potro.galopa();
        potro.comer();
        Nutria.bucear();
        Animal perro=new Animal("Pepe", 5000);
        perro.nombre = "pepe2";
        System.out.println(perro.nombre);
        System.out.println("El animal" + perro.nombre+ " pesa: "+ perro.getWeight() + "gr");
        jaula[1]=perro;
        perro.comer();
        Nutria nutria=new Nutria("chispas");
        nutria.respirarDebajoDelAgua();
        jaula[2]=nutria;
        nutria.comer();
        jaula[3]=new Caballo("Amador", false);
        Nutria antonio=new Nutria("Antonio Recio");
        jaula[4]=antonio;
        antonio.llamamiento();
        for (int i=0;i<jaula.length;i++){
            System.out.println();
            jaula[i].llamamiento();
        }
    }
}
