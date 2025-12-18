package Presentation;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import Metier.*;
import Metier.Gestionnaire.*;
import Persistance.*;

	public class modifierprojet extends JFrame {
		
		Daoetudiant dao ;
		JRadioButton bRouge = new JRadioButton ("pfe") ;
		JRadioButton bVert = new JRadioButton ("pfa") ;
		JRadioButton bRose = new JRadioButton ("Doctora") ;
		
		ButtonGroup groupe = new ButtonGroup() ;
		
		private JLabel labelInscrption;
		private JLabel labeltitre;
		private JButton labelPrenom;
		private JLabel labellabo;
		private JLabel labelEntrprs;
		private JLabel Deja;
		private JTextField textprojet;
		private JTextField textdate_debut;
		private JLabel etudiant;
		private JLabel prof;
		private JLabel prof2;
		
		private JComboBox jc1;
		private JComboBox jc2;
		private JComboBox jc3;
	    
		private String s1,s2;
	   
		private JComboBox<String>  lduree  = new JComboBox<String>();
		private String s[];
		
		private JTextField textlabo;
		private JTextField textEntrprs;
		private JButton inscrire;
		private Integer id_projet;
		private String ss;
		private Controleur controleur;
		
		public modifierprojet(Controleur controleur) {
			this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			this.setTitle("projet");
			this.setSize(550, 650);
			try {
				this.initialiser(controleur);
			} catch (ClassNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			this.dessinner();
			this.executer();
			this.execute2();  		
			
			this.setVisible(true);
		}
	
		public modifierprojet(projet prj, Controleur controleur)  {
			this(controleur);
			this.id_projet=prj.getId_projet();
			this.textprojet.setText(prj.getTitre()); 
			this.textdate_debut.setText(prj.getDate_debut() ); 
			
			jc1.addItem(prj.getId());
			
		if(prj.getType()=="pfe") {
				bRose.setSelected(true);
			}
			if(prj.getType()=="pfa") {
				bVert.setSelected(true);
							
			}
			if(prj.getType()=="Doctora") {
				bRose.setSelected(true);
                 }
			
		//	this.textlabo.setInt(prj.get(7));
	//		this.textEntrprs.setText(prj.getPassword());
			lduree.addItem(prj.getDuree());
		   if(prj.getId_labo()==-1) {
		   textEntrprs.setText(prj.getId_Es().toString());
		   textlabo.setText(" ");
		     }
		   if(prj.getId_Es()==-1) {
		   textlabo.setText(prj.getId_labo().toString());
		   textEntrprs.setText(" ");
		   }
		}
		  
		
		private void initialiser(Controleur controleur) throws ClassNotFoundException {
			groupe.add(bRouge) ;
			groupe.add(bVert) ;
			groupe.add(bRose);
			etudiant= new JLabel("etudiant: ");
			prof = new JLabel("encadrant: ");
			prof2 = new JLabel("encadrant2: ");
			
			jc1 =new JComboBox();
			jc2 =new JComboBox();
			jc3 =new JComboBox();
			
			Gestionnairetudiante dao = new Gestionnairetudiante();
			ArrayList<Integer> l = dao.getnewetudient();
			for(Integer e : l){
				    jc1.addItem(e.toString());
				    }
			Daoprofesseur daop = new Daoprofesseur();
			ArrayList<professeur> l1 = daop.getAll();
			for(professeur p : l1){
				jc2.addItem(p.getId_prof().toString());
				    }
			Daoprofesseur dao2 = new Daoprofesseur();
			ArrayList<professeur> l2 = daop.getAll();
			for(professeur p : l2){
				jc3.addItem(p.getId_prof().toString());
				    }
			
			
			labelInscrption=new JLabel("Titre projet :");
			labeltitre = new JLabel("date_debut");
			labelPrenom = new JButton("dure");
			
			labellabo = new JLabel("laboratoire");
			 labelEntrprs = new JLabel("entreprise");
			Deja = new JLabel("<-retour en arrier"); ;
			
			this.textprojet= new JTextField(30);
			this.textdate_debut = new JTextField(30);
			this.textlabo= new JTextField(30);
			this.textEntrprs = new JTextField(30);
			
			this.inscrire = new JButton("inscrire");
			this.controleur=controleur;
		}
		
		private void dessinner() {
			this.setLayout(new BorderLayout());
		//insciption et nom et prenom dans north lkbir
			
			JPanel north = new JPanel();
			north.setLayout(new GridLayout(4,3, 3,40));
			Container contenaireKhawiLfo9 = new Container();
			contenaireKhawiLfo9.setPreferredSize(new Dimension(50,50));
			
			Container cont = new Container();
			cont.setPreferredSize(new Dimension(50,50));
			
			
			north.add(labelInscrption);
			north.add(textprojet);
			north.add(contenaireKhawiLfo9);
			north.add(bRouge);
		    north.add(bVert);
		    north.add(bRose);
		    north.add(labeltitre);
		    north.add(textdate_debut);
		    north.add(new Container());
		    north.add(labelPrenom);
		    north.add(lduree);
			
		   
			this.add(north, BorderLayout.NORTH);
		// adresse et mot pass et confirmed motpass
			
			JPanel centre = new JPanel();
			centre.setLayout(new GridLayout(4,1));
			centre.add(labellabo);
			centre.add(textlabo);
			centre.add(labelEntrprs);
			centre.add(textEntrprs);
		
			this.add(centre, BorderLayout.CENTER);
			//
			
			JPanel south = new JPanel();
			south.setLayout(new BorderLayout());
			
			
			
		// 2 radio 	wlita7tha
			
			
			JPanel centre2 = new JPanel();
			centre2.setLayout(new GridLayout(3,2));
			
			JPanel south2 = new JPanel();
			south2.setLayout(new GridLayout(2,3));
			
			
			
			centre2.add(etudiant);
			centre2.add(jc1);
			centre2.add(prof);
			centre2.add(jc2);
			centre2.add(prof2);
			centre2.add(jc3);
			
			south2.add(new Container());//inscrire button
			south2.add(inscrire);//inscrire button
			
			south2.add(new Container());//inscrire button
			
			//inscrire et deja 
			south2.add(Deja);
			south2.add(new Container());//inscrire button
			
		
			//south.add(north2, BorderLayout.NORTH);
			
		
			south.add(centre2, BorderLayout.CENTER);
			
			
			south.add(south2, BorderLayout.SOUTH);
			//suath glob
			
			this.add(south, BorderLayout.SOUTH);
			
			
		}
		private void colsing() {
			this.dispose();
		}
		private void execute2() {
			// TODO Auto-generated method stub
			Deja.addMouseListener((MouseListener) new MouseAdapter() {
				@Override
				public void mouseClicked(MouseEvent e) {
					super.mouseClicked(e);
					try {
						controleur.gestionprojet();
					} catch (ClassNotFoundException e1) {
						// TODO Auto-generated catch block
						e1.printStackTrace();
					}
					colsing();
					}
			});
			
			
		}
		private void executer() {
			labelPrenom.addActionListener(
					new ActionListener() {

						@Override
						public void actionPerformed(ActionEvent e) {
     if(bRouge.isSelected()) { 
    	 	lduree.removeAllItems();
			lduree.addItem("5mois");
			lduree.addItem("6 mois");
			textdate_debut.setText("fevrier");
			labelEntrprs.setVisible(true);
			textEntrprs.setVisible(true);
			prof2.setVisible(false);
			jc3.setVisible(false);
			ss=bRouge.getText();
				
     }
		else if(bVert.isSelected()) {
			ss=bVert.getText();
			lduree.removeAllItems();;
			lduree.addItem("2mois");
			textdate_debut.setText("juin");
			labelEntrprs.setVisible(true);
			textEntrprs.setVisible(true);
			prof2.setVisible(false);
			jc3.setVisible(false);
			
		}
		else if (bRose.isSelected()){
			ss=bRose.getText();
			lduree.removeAllItems();
			lduree.addItem("3 ans");
			lduree.addItem("6 ans");
			textdate_debut.setText("Octobre");
			labelEntrprs.setVisible(false);
			textEntrprs.setVisible(false);
			prof2.setVisible(true);
			jc3.setVisible(true);
		}
         
						}				
					});
		
			
		inscrire.addMouseListener((MouseListener) new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e){
				super.mouseClicked(e);
				try {
				if((textlabo.getText().compareTo(" ")==0)&& ((ss=="pfe")||(ss=="pfa"))) {
				System.out.println("hsdjh");
					controleur.inscrprojet(id_projet,textprojet.getText(),textdate_debut.getText(),lduree.getSelectedItem().toString(),ss,Integer.parseInt(jc1.getSelectedItem().toString()),Integer.parseInt(jc2.getSelectedItem().toString()),-1,Integer.parseInt(textEntrprs.getText()),-1);
				
				}
				if((textEntrprs.getText().compareTo(" ")==0)&& ((ss=="pfe")||(ss=="pfa"))) {
					System.out.println("hsdjh");
					controleur.inscrprojet(id_projet,textprojet.getText(),textdate_debut.getText(),lduree.getSelectedItem().toString(),ss,Integer.parseInt(jc1.getSelectedItem().toString()),Integer.parseInt(jc2.getSelectedItem().toString()),Integer.parseInt(textlabo.getText()),-1,-1);
				
				}	
				if(ss=="Doctora") {
					System.out.println("hsdjh");
							controleur.inscrprojet(id_projet,textprojet.getText(),textdate_debut.getText(),lduree.getSelectedItem().toString(),ss,Integer.parseInt(jc1.getSelectedItem().toString()) ,Integer.parseInt(jc2.getSelectedItem().toString()),Integer.parseInt(textlabo.getText()),-1,Integer.parseInt(jc3.getSelectedItem().toString()));
				}}
				catch(Exception ex1){
					ex1.printStackTrace();
				}
					
				System.out.println(textlabo.getText());System.out.println(textEntrprs.getText());
				System.out.println(ss);
				colsing();
			}
		});
	}
		
}