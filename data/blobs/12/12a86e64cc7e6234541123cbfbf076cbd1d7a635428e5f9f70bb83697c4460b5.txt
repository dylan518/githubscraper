package CONTROLLER;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JOptionPane;

import CONFIGURATION.Connexion;
import MODEL.CategorieI;
import MODEL.ChambreI;
import VIEW.ViewI;

public class Manager2 {

	ChambreI chambre ;
	CategorieI categorie ;
	ViewI view ;
	Connexion cnx= new Connexion();
	
	public Manager2(ChambreI ch , CategorieI cat , ViewI view)
	{
		chambre=ch ;
		categorie = cat ;
		this.view= view ;
	}
	
	public void initController()
	{
		view.getBtnAjouter().addActionListener(new ActionListener()
				{
					public void actionPerformed(ActionEvent e) {
					Ajouter();
						
					}
					});
		view.getLblQuitter().addMouseListener(new MouseAdapter()
				{
				public void mouseClicked(MouseEvent e) {
	        
					 quitter();
	    }});
		
		view.getBtnAnnuler().addActionListener(e ->annuler());
	
		}
	
	
	private void Ajouter()
	{
		
		
		
		if((int)view.getTxtEtage().getValue()<=0 ||  (int)view.getTxtEtage().getValue()>10)
		{
			JOptionPane.showMessageDialog(view,"Etage invalide !!", "Ajouter chambre",JOptionPane.WARNING_MESSAGE);
			view.getTxtEtage().setValue(0);
			view.getTxtEtage().setBorder(BorderFactory.createLineBorder(Color.RED));
			view.getTxtEtage().setFocusable(true);
			view.getTxtEtage().requestFocus();
			//requestFocusInWindow();
			
			if((int)view.getTxtNbrlit().getValue()<=0 ||  (int)view.getTxtNbrlit().getValue()>5)
			{
				JOptionPane.showMessageDialog(view," vous avez deppaser le nombre maximun des lits !!", "Ajouter chambre",JOptionPane.WARNING_MESSAGE);
				view.getTxtNbrlit().setValue(0);
				view.getTxtNbrlit().setBorder(BorderFactory.createLineBorder(Color.RED));
				view.getTxtEtage().setFocusable(true);
				view.getTxtNbrlit().requestFocus();
			
		}
			}
		else 
		{
			
		
		chambre.setEtage((int)view.getTxtEtage().getValue());
		chambre.setNbLits((int)view.getTxtNbrlit().getValue());
		String nomCat= (String)view.getCategorieSelect().getSelectedItem();
		cnx.InsererChambre(chambre, nomCat);
		categorie.getListeChambre().add(chambre);
		JOptionPane.showMessageDialog(view,"chambre ajouter avec succes ", "Ajouter chambre",JOptionPane.INFORMATION_MESSAGE);
		}
	}
	private void quitter()
	{
		int rep =JOptionPane.showConfirmDialog(view, " vous voulez vraiment quitter ?", "Quitter", JOptionPane.YES_NO_OPTION);
		if(rep==JOptionPane.YES_OPTION)
			//cnx.desconnected();
			System.exit(0);
	}
	private void annuler()
	{
		view.getTxtEtage().setValue(0);;
		view.getTxtNbrlit().setValue(0);;
		view.getCategorieSelect().setSelectedItem(null);
	}
	
}
