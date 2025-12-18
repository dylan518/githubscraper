package Takip;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSpinner;
import javax.swing.border.EmptyBorder;

import Helpers.DBConnection;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.Font;

public class guncelle extends JFrame {

	private JPanel contentPane;

	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					guncelle frame = new guncelle();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	JLabel[] label = new JLabel[20];
	JSpinner[] spinner = new JSpinner[20];
	String[] name=new String[20];
	int[] stok=new int[20];
	int[] tut=new int[20];
	int indexsi;
	public guncelle() {
		setFont(new Font("Impact", Font.PLAIN, 35));
		setTitle("Night Lords Stok");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(-1, -1, 1368, 768);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btnguncel = new JButton("Güncelle");
		btnguncel.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				for(int i=0; i<indexsi;i++)
				{
					
					tut[i]=stok[i]+(int)spinner[i].getValue();
					
				}
				
				 try {
						
						DBConnection conn=new DBConnection();
				        Connection con=conn.connDb();
				        Statement st=con.createStatement();	
				       
				        	
				        
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[0]+"' where id='1' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[1]+"' where id='2' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[2]+"' where id='3' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[3]+"' where id='4' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[4]+"' where id='5' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[5]+"' where id='6' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[6]+"' where id='7' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[7]+"' where id='8' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[8]+"' where id='9' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[9]+"' where id='10' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[10]+"' where id='11' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[11]+"' where id='12' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[12]+"' where id='13' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[13]+"' where id='14' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[14]+"' where id='15' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[15]+"' where id='16' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[16]+"' where id='17' ");
				        	st.executeUpdate("Update soguk_icecekler SET  number_of_pieces='"+tut[17]+"' where id='18' ");
				        	
				        	
				        	
	                  }
	                  catch(SQLException e1) 
					    {

				            e1.printStackTrace();
				        }	
				 guncelle f1=new guncelle();
				 f1.setVisible(true);
				 dispose();
				 
			}
		});
		btnguncel.setBounds(1108, 11, 117, 31);
		contentPane.add(btnguncel);
		
		JButton btnNewButton = new JButton("Masalar");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Night_Lords_Takip f4=new Night_Lords_Takip();
				f4.setVisible(true);
				dispose();
			}
		});
		btnNewButton.setBounds(1235, 11, 117, 31);
		contentPane.add(btnNewButton);
		
		try {
			DBConnection conn=new DBConnection();
	        Connection con=conn.connDb();
	        Statement st=con.createStatement();			       	        
	        ResultSet rs =st.executeQuery("select*from soguk_icecekler ");
	      
	        while(rs.next()) 
	        {	        	
	        	indexsi++;	
	            name[indexsi-1]=rs.getString("product_name");	            
	            stok[indexsi-1]=rs.getInt("number_of_pieces");
	            
	        }
	        rs.close();
			}
			catch(SQLException e1) {

	            e1.printStackTrace();
	        }
		
		int six=10,siy=109;
		int sisx=250,sisy=105;		
		for (int i = 0; i <indexsi ; i++) 
		{		
			
		    label[i] = new JLabel("");
		    label[i].setText(name[i]+"  "+"Stokta"+"  "+stok[i]+" adet");
		    label[i].setBounds(six, siy, 250, 24);		    
		    contentPane.add( label[i]);
		    
		    spinner[i] = new JSpinner();
	    	spinner[i].setBounds(sisx, sisy, 40, 40);
	    	contentPane.add(spinner[i]);
	    	
	    	
		    six+=420;
		    if(six>1200)
		    {
		    	six=10;
		    	siy+=110;
		    		
		    }
		    
		    
			sisx+=420;		
	    	if(sisx>1200)
	    	 {
	    	 sisx=250;
	    	 sisy+=109;
	    	    		    		
	    	 }   
		    
		}
		
	}
}
