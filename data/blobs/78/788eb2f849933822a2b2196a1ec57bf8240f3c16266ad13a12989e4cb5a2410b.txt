package Model;

import java.awt.Color;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Vector;

import javax.swing.JComponent;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.event.ListSelectionListener;
import javax.swing.table.DefaultTableModel;

import DAO.DaoImpl;
import View.CustomerPanel;
import View.ProductPanel;

public class CustomerTableModel extends DefaultTableModel {
	
	
	CustomerPanel view;
	ArrayList<Customer> allCustomers;
	

      public CustomerTableModel(CustomerPanel customerPanel) {

		view  = customerPanel;
		DaoImpl dao = new DaoImpl();
		try {
			allCustomers = dao.getAllCustomers();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}


	public JScrollPane addTable() {
		
		String data[][] = new String[allCustomers.size()][6];
		String column[] = { "Customer_ID", "Customer_Name", "Email", "Phone", "Credit_Rating", "Address" };
		
		for (int i = 0; i < allCustomers.size(); i++) {
			// ID in data
			data[i][0] = String.valueOf(allCustomers.get(i).getCustomer_id());
			// Name in data	
			data[i][1] = allCustomers.get(i).getCustomer_name();
			// Email in data
			data[i][2] = String.valueOf(allCustomers.get(i).getEmail());
			// Phone in data
			data[i][3] = String.valueOf(allCustomers.get(i).getPhone());
			// Credit_Rating in data
			data[i][4] = String.valueOf(allCustomers.get(i).getCredit_rating());
			// Address in data
			data[i][5] = String.valueOf(allCustomers.get(i).getAddress());
			
		
		}

		JTable jt = new JTable(data, column);
		jt.setBackground(Color.LIGHT_GRAY);
		JScrollPane sp = new JScrollPane(jt);
		sp.setBounds(21, 242, 842, 193);	
		sp.setViewportView(jt);
		return sp;

		
	}



}

