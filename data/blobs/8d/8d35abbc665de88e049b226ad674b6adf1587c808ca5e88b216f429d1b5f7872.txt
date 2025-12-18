package frames;

import java.lang.*;
import javax.swing.*;
import java.awt.event.*;
import entities.*;
import repositories.*;

public class SignUpFrame extends JFrame implements ActionListener
{
	private JLabel userIdLabel,nameLabel, emailLabel, phoneNoLabel, genderLabel, ageLabel, addressLabel, securityQuesLabel, securityAnsLabel, passLabel;
	private JTextField userTF, nameTF, emailTF, phoneNoTF, ageTF, addressTF, securityAnsTF;
	private JPasswordField passPF;
	private JRadioButton maleRB, femaleRB;
	private ButtonGroup bg;
	private JButton addBtn, backBtn;
	
	private JPanel panel;
	
	
	
	
	public SignUpFrame()
	{
		super("Admin Operation Frame");
		this.setSize(800,600);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		this.panel=new JPanel();
		this.panel.setLayout(null);
		
		this.userIdLabel=new JLabel("User Id:");
		this.userIdLabel.setBounds(50,50,60,30);
		this.panel.add(userIdLabel);
		
		this.userTF=new JTextField();
		this.userTF.setBounds(120,50,100,30);
		this.panel.add(userTF);
		
		this.nameLabel=new JLabel("Name:");
		this.nameLabel.setBounds(50,100,60,30);
		this.panel.add(nameLabel);
		
		this.nameTF=new JTextField();
		this.nameTF.setBounds(120,100,100,30);
		this.panel.add(nameTF);
		
		this.emailLabel=new JLabel("email:");
		this.emailLabel.setBounds(50,150,60,30);
		this.panel.add(emailLabel);
		
		this.emailTF=new JTextField();
		this.emailTF.setBounds(120,150,100,30);
		this.panel.add(emailTF);
		
		this.phoneNoLabel=new JLabel("phone No:");
		this.phoneNoLabel.setBounds(50,200,60,30);
		this.panel.add(phoneNoLabel);
		
		this.phoneNoTF=new JTextField();
		this.phoneNoTF.setBounds(120,200,100,30);
		this.panel.add(phoneNoTF);
		
		this.genderLabel=new JLabel("Gender:");
		this.genderLabel.setBounds(50,250,60,30);
		this.panel.add(genderLabel);
		
		this.maleRB=new JRadioButton("Male");
		this.maleRB.setBounds(120,250,60,30);
		this.panel.add(maleRB);
		
		this.femaleRB=new JRadioButton("Female");
		this.femaleRB.setBounds(190,250,80,30);
		this.panel.add(femaleRB);
		
		this.bg=new ButtonGroup();
		bg.add(maleRB);
		bg.add(femaleRB);
		
		this.ageLabel=new JLabel("Age:");
		this.ageLabel.setBounds(50,300,60,30);
		this.panel.add(ageLabel);
		
		this.ageTF=new JTextField();
		this.ageTF.setBounds(120,300,100,30);
		this.panel.add(ageTF);
		
		this.addressLabel=new JLabel("Address:");
		this.addressLabel.setBounds(280,50,60,30);
		this.panel.add(addressLabel);
		
		this.addressTF=new JTextField();
		this.addressTF.setBounds(350,50,100,30);
		this.panel.add(addressTF);
		
		this.securityQuesLabel=new JLabel("Security Ques: What is your pet name?:");
		this.securityQuesLabel.setBounds(280,100,300,30);
		this.panel.add(securityQuesLabel);
		
		this.securityAnsLabel=new JLabel("Security Ans:");
		this.securityAnsLabel.setBounds(280,150,100,30);
		this.panel.add(securityAnsLabel);
		
		this.securityAnsTF=new JTextField();
		this.securityAnsTF.setBounds(390,150,100,30);
		this.panel.add(securityAnsTF);
		
		this.passLabel=new JLabel("Password:");
		this.passLabel.setBounds(280,200,100,30);
		this.panel.add(passLabel);
		
		this.passPF=new JPasswordField();
		this.passPF.setBounds(390,200,100,30);
		this.panel.add(passPF);
		
		
		this.addBtn=new JButton("Submit");
		this.addBtn.setBounds(50,350,100,30);
		this.addBtn.addActionListener(this);
		this.panel.add(addBtn);
		
		
		this.backBtn=new JButton("back");
		this.backBtn.setBounds(160,350,100,30);
		this.backBtn.addActionListener(this);
		this.panel.add(backBtn);
		
		
		this.add(panel);

		
	}
	
	public void actionPerformed(ActionEvent ae)
	{
		String command=ae.getActionCommand();
		
		if(command.equals(addBtn.getText()))
		{
			String userId,name,email,phoneNo,gender,address,securityAns,pass;
			int age;
			//validating every field has data or not
			if((!userTF.getText().isEmpty()) && (!nameTF.getText().isEmpty()) && (!emailTF.getText().isEmpty()) && (!phoneNoTF.getText().isEmpty()) &&((maleRB.isSelected()) || (femaleRB.isSelected())) && (!ageTF.getText().isEmpty()) && (!addressTF.getText().isEmpty())&& (!securityAnsTF.getText().isEmpty()) && (!passPF.getText().isEmpty()))
			{
				//storing userTF (userID) in userId variable
				userId=userTF.getText();
				//creating a UserRepo object to perform operation in the user.txt file where we stored user login information
				UserRepo urp=new UserRepo();
				//checking whether the provide user id is unique or already assign to another user.
				User user=urp.searchUserByUserId(userId);
				// if the provided userId is unique, no User type object will be found in the user.txt file.
				//if no user if assign with the userId then we can use the userId for creating new admin.
				if(user==null)
				{
					//using try catch block, so that, any type of exception can be handled. here we have a age value, which is expected to be integer.
					//but user can put string value to age varible which might cause exception.
					//to handle such exception we are using try catch block.
					try
					{
						//asign nameTF textfField value to a name variable.
						name=nameTF.getText();
						//asign emailTF textfField value to a email variable.
						email=emailTF.getText();
						//asign phoneNoTF textfField value to a phoneNo variable.
						phoneNo=phoneNoTF.getText();
						// to get gender, we use RadioButton. now to know which radioButton is selected,
						//we are applying conditions if maleRB is selected, gender variable will be assigned as maleRB's value.
						//if femaleRB is selected, gender variable will be assigned as femaleRB's value.
						//or by default maleRB's value will be assigned.
						if(maleRB.isSelected())
						{
							gender=maleRB.getText();
						}
				
						else if(femaleRB.isSelected())
						{
							gender=femaleRB.getText();
						}
				
						else
						{
							gender=maleRB.getText();
						}
						//asign ageTF textfField value to a age variable. But before assigning we have to convert the ageTF value to integer as our age varibale's expected value is integer.
						age=Integer.parseInt(ageTF.getText());
						//asign addressTF textfField value to a address variable.
						address=addressTF.getText();
						//asign role. As all the Student will have the same role, we won't have to take this value from user.
						//For admin the role will be 1.
						int role=3;
						//asign securityAnsTF textfField value to a securityAns variable.
						securityAns=securityAnsTF.getText();
						//asign passPF PassField value to a pass variable.
						pass=passPF.getText();
						
						//Creating a Student type variable with all the values that we get from the fields. when a new student admit, he/she has 0 completed credit, and 0.0 cgpa.
						//thats why we dont need to take user input as all new student has 0 completed credit and 0.0 cgpa.
						Client c=new Client(userId,name,email,phoneNo,gender,age,address,role,securityAns,pass,"new");
						//to add Student's user id, security ans, role and pass information in the user.txt file. as without data in the user.txt file, no user will be able to login in.
						//passing student type object to a userRepo. here polymorphic behaviour of object is used.
						urp.addUser(c);
						//creating a StudentRepo object to perform operation in the student.txt file where we stored admins information
						ClientRepo crp=new ClientRepo();
						//to add Student's information in the student.txt file. because all the students information will be stored there.
						crp.addClient(c);
						//After successful add operation a confirmation message will be shown.
						JOptionPane.showMessageDialog(this,"Client signed up Successfully");
					}
					catch(Exception e)
					{
						//if any exception occured in the above operation, it is beacuse of string to int convertion.
						JOptionPane.showMessageDialog(this,"provide valid age");
					}
				}
				
				else
				{
					//if the provided userId is already assign to any user, this message will be shown.
					JOptionPane.showMessageDialog(this,"User Id already exists.");
				}
		
			}
			else
			{
				//if any of the field is empty, this message will be shown.
				JOptionPane.showMessageDialog(this,"please fill up all the field properly");
			}
			
		}
		
		
		
		
		
		
		if(command.equals(backBtn.getText()))
		{
			//back button will take you to login page.
			LoginFrame adf=new LoginFrame();
			this.setVisible(false);
			adf.setVisible(true);
		}
	}
	
}