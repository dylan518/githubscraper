package Interface_Utilisateur;
import java.util.Scanner;
import Command.Commande;
import Command.CommandeCarre;
import Command.CommandeCercle;
import Command.CommandeMove;
import Command.CommandeQuit;
import Command.CommandeRectangle;
import Command.CommandeSave;
import Command.CommandeTriangle;
import Command.Interpreter;
import Exception.CommandeIncorrectException;
import Exception.DrawingNotFoundException;
import Exception.ParametresIncorrectsException;
import Exception.RectangleLongueurLargeurException;
import Forme_Graphique.FormeGraphique;

/**
 * Cette classe communique avec la classe DrawingApp
 * et permet d'executer les commandes des utilisateurs
 *
 */
public class DrawingTUI {

	  private Interpreter interprete = new Interpreter();
	  
	  /**
	   * Méthode qui permet de recuperer la saisie de l'utilisateur
	   * elle est utilisée pour recupérer la reponse de l'utilisateur 
	   * quant à la sauvegarde des données
	   * @return
	   */
	  public String reponseUtilisateur() {
		  Scanner sc = new Scanner(System.in);
		  System.out.println("Do you want to save this form y/n?");
		  String in = sc.nextLine();
		  return in;
	  }
 /**
  * Méthode nextCommande charger d'executer les commandes des utilisateurs
  * @param saisieUser
  * @return
  * @throws ParametresIncorrectsException
  * @throws CommandeIncorrectException
  * @throws DrawingNotFoundException
 * @throws RectangleLongueurLargeurException 
  */
	  public Commande nextCommande(String saisieUser) throws ParametresIncorrectsException, CommandeIncorrectException, DrawingNotFoundException, RectangleLongueurLargeurException{
		  Double a, b;
		  String reponseUser = null;
		  String[] chaine = saisieUser.replaceAll("[()=,;]","").split(" "); //permet de supprimer les parenthèses, les égalités,les virgules,les espaces et 
		  String nom=null;
		  if(chaine.length > 1) {
			   nom=chaine[1];
		  }else {
			  nom = chaine[0];
		 }
			   	
	
			  if(nom.contentEquals("Carre")) {
				  if(chaine.length == 5) {
				  interprete.parametresCommande(new String[]{chaine[0], chaine[2], chaine[3],chaine[4]});
					  CommandeCarre commandeCarre = new CommandeCarre(interprete);
					    commandeCarre.execute();
					    for (FormeGraphique form : interprete.Liste_FormeGraphique) {
							  form.printForme();
						}
//					    reponseUser = reponseUtilisateur();
//					    if(reponseUser.contentEquals("y") || reponseUser.contentEquals("Y") || reponseUser.contentEquals("yes")) {
//							 CommandeSave save = new CommandeSave(interprete);
//							 save.execute(); 
//					    }
				  }else {
					  throw new ParametresIncorrectsException();
				  }
			  }else if(nom.contentEquals("Cercle")) {
				  if(chaine.length == 5) {
					  interprete.parametresCommande(new String[]{chaine[0], chaine[2], chaine[3],chaine[4]});
					  CommandeCercle commandeCercle = new CommandeCercle(interprete);
					    commandeCercle.execute();
					    for (FormeGraphique form : interprete.Liste_FormeGraphique) {
							  form.printForme();
						}
//					    reponseUser = reponseUtilisateur();
//					    if(reponseUser.contentEquals("y") || reponseUser.contentEquals("Y") || reponseUser.contentEquals("yes")) {
//							 CommandeSave save = new CommandeSave(interprete);
//							 save.execute(); 	 
//					       }
					    }else {
					    	throw new ParametresIncorrectsException();
					    }
			 
			  }else if(nom.contentEquals("Rectangle")) {
				  
				  if(chaine.length == 6) {
			
					  interprete.parametresCommande(new String[]{chaine[0], chaine[2], chaine[3],chaine[4], chaine[5] });
					  CommandeRectangle commandeRectangle = new CommandeRectangle(interprete);
					    commandeRectangle.execute();
					    for (FormeGraphique form : interprete.Liste_FormeGraphique) {
							  form.printForme();
						}
//					    reponseUser = reponseUtilisateur();
//					    if(reponseUser.contentEquals("y") || reponseUser.contentEquals("Y") || reponseUser.contentEquals("yes")) {
//							 CommandeSave save = new CommandeSave(interprete);
//							 save.execute(); 
//					    }
				  	}else {
				  		throw new ParametresIncorrectsException();
				  	}
				  }else if(nom.contentEquals("Triangle")) {
					  if(chaine.length == 8) {
					  interprete.parametresCommande(new String[]{chaine[0],chaine[2], chaine[3], chaine[4],chaine[5], chaine[6], chaine[7] });
					  CommandeTriangle commandeTriangle = new CommandeTriangle(interprete);
					    commandeTriangle.execute();
					    for (FormeGraphique form : interprete.Liste_FormeGraphique) {
							  form.printForme();
						}
//					    reponseUser = reponseUtilisateur();
//					    if(reponseUser.contentEquals("y") || reponseUser.contentEquals("Y") || reponseUser.contentEquals("yes")) {
//							 CommandeSave save = new CommandeSave(interprete);
//							 save.execute(); 
//					    }
					  
					  }else {
						  throw new ParametresIncorrectsException();
					  }
				  }else if(chaine[0].contentEquals("move")){
					  if(chaine.length == 4) {
			         	if (chaine[1].contentEquals("all")) {
							for (FormeGraphique form : interprete.Liste_FormeGraphique) {
								  a = Double.parseDouble(chaine[2]);
						          b = Double.parseDouble(chaine[3]);
								form.move(a, b);
								
							}
							System.out.println("deplacement de" + interprete.Liste_FormeGraphique +"reussie!!!");
						} else {
							interprete.parametresCommande(new String[]{chaine[1], chaine[2], chaine[3]});
						 	CommandeMove commandeMove = new CommandeMove(interprete);
						 	commandeMove.execute();
						 
						}
					  }else {
						  throw new ParametresIncorrectsException();
					  }
				  }else if (chaine[0].contentEquals("view")) {
					  if(chaine.length == 2) {
						 if (chaine[1].contentEquals("all")) {
							 for (FormeGraphique form : interprete.Liste_FormeGraphique) {
								  form.printForme();
							}
						 }
						 else {
							 DrawingTUI afficheView = new DrawingTUI();
							 afficheView.printDrawing(interprete,chaine[1]);
						 }
					  }
					  else {
						  throw new ParametresIncorrectsException();
					  }
				  }else if (chaine[0].contentEquals("quit")){
						 CommandeQuit quitter = new CommandeQuit(interprete);
						 quitter.execute();
				  }else {
					  throw new CommandeIncorrectException();
				  }
		return null;
			  
       }
	  
  /**
   * Méthode qui permet d'afficher les commandes effectuées par les utilisateurs
   * @param interprete
   * @param name
   * @throws DrawingNotFoundException
   */
	  public void printDrawing(Interpreter interprete,String name) throws DrawingNotFoundException{
		 
		  CommandeMove m = new CommandeMove(interprete);
		  FormeGraphique f =  m.findFormeGraphique(name);
		  f.printForme();
	  }  
	}