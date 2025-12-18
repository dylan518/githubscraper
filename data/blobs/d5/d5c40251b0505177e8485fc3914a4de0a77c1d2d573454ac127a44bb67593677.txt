package ListProject;

import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import javax.swing.*;

import org.json.*;

/**
 * This class is where the main frame of the 'To Do List' program is initialized and where all the components of the "To Do List" together are 
 * assembled and given functionality.
 * 
 * @author  Prantik Roy
 * @version 1.0
 * @since   2023 December 22th
 * 
 * title A JPanel that holds the title of the "To Do List"
 * 
 * list A JPanel that holds all the note panels with their own individual tasks
 * 
 * controls A JPanel that holds all the general controls of the list shown at the bottom
 * 
 * storage The JSONObject that stores information about all the tasks of the "To Do List" in a JSON file for future use
 * 
 * PATH Stores The directions to the JSON file used to initialize and save the data in storage 
 * 
 * unsavedTexts A hashmap that temporarily stores the texts of all the unsaved tasks to be shown again when the tasks are 
 * 				redrawn after initialize() is called. This collection is deleted once the program is closed or when all 
 * 				the tasks are saved.
 *              
 * scrollBar The scroll bar thats generated in the list JPanel once the number of notes exceeds the visual limit later
 * 
 * currentID The variable used to generate the address of a new task
 * 
 * @throws IOException Thrown when a JSON file isn't found
 */

public class Frame extends JFrame{
	private Title title; 
	private List list; 
	private Controls controls;
	private JSONObject storage = new JSONObject();
	private final String PATH = "src/ListProject/To_Do_List.json";
	private Map<Integer, String> unsavedTexts = new HashMap<Integer, String>();
	private JScrollPane scrollBar;
	private int currentID = 0;
	
	// Constructor for initializing the JFrame and its fields
	public Frame() throws IOException {
		
		// Setting the size of the frame
		this.setSize(600, 700);
		
		// Sets the program to be terminated once the upper right close button is clicked
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// Tells the frame to show all its components
		this.setVisible(true);
		
		// Tells the frame that it can be resized
		this.setResizable(true);
		
		// Initializes the title of the "To Do List" and puts it at the top of the frame
		title = new Title();
		this.add(title, BorderLayout.NORTH);
		
		// Initializes the control panels and puts it on the bottom of the frame
		controls = new Controls();
		this.add(controls, BorderLayout.SOUTH);
		
		/* Initializes the panel that shows the list of tasks and puts it inbetween the title and the control panel in the 
		 * center of the frame and adds a vertical scroll bar to it when its contents get out of view*/
		list = new List();
		scrollBar = new JScrollPane(list, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
		
		/* Initializes the JSONObject used to store all the information about the tasks of the "To Do List" with updated 
		 * information about the previously saved tasks that was stored in the JSON file that can be found in PATH.*/ 
		String contents = new String(Files.readAllBytes(Paths.get(PATH)));
		storage = new JSONObject(contents);
		
		// Initializes the currentID
		initializeCount();
		// Gives functionality to all the buttons in the control panel
		ActionListener();
		
		/* Initializes all the individual panels that contain the tasks of the "To Do List" using the information stored in the 
		 * JSONObject of storage and gives their buttons functionality */
		initialize();
	}
	
	
	/**
	 * This class initializes the currentID with most recent ID used, the IDs are updated numerically from 1, 2, 3, 4, ...
	 * with the first task added to the "To Do List" having a an id of 1, the next having an id of 2, etc... 
	 */
	public void initializeCount() {
		// Since tasks can be deleted the most recent id would be the one with the highest number
		int max = 0;
		
		// Gets id with the highest number from all the information of the the tasks stored in the JSON file
		for (Iterator key=storage.keys(); key.hasNext();) {
			int id = Integer.parseInt(key.next().toString());
			if (id > max) {
				max = id;
			}
		}
		
		this.currentID = max;
	}
	
	/**
	 * This class gives functionality to all the buttons of the control panel
	 * 
	 * @throws IOException Thrown when a JSON file isn't found
	 */
	public void ActionListener() throws IOException {
		controls.getAddNote().addMouseListener(new MouseAdapter () {
			
			/**
			 * This method gives the "Add Note" button the ability to make a new note for the "To Do List"
			 * @throws IOException
			 */
			@Override
			public void mousePressed(MouseEvent e) {
				int id = ++currentID; // updates the ID for the new task to be added
				
				String newNote = id + "//false"; /* Information about the newly added note containing 
														an updated ID, default text, & default state of the task 
														Separated by '/'*/
				
				storage.put(Integer.toString(id), newNote); // Stored the information about the newly make task in the JSONObject
				
				try {
					save(); // updates the JSON file with the information from the JSONObject
					initialize(); // redraws the window based on the information from the updated JSON file 
				} catch (IOException e1) {
					e1.printStackTrace();
				}
				
			}
			
		});
		
		controls.getclearNotes().addMouseListener(new MouseAdapter() {
			/**
			 * This method gives the "Clear Notes" button the ability to delete every note in the "To Do List"
			 * 
			 * @throws IOException
			 */
			@Override
			public void mousePressed(MouseEvent e) {
				try {
					unsavedTexts = new HashMap<Integer, String>();
					storage = new JSONObject();
					currentID = 0;
					
					save(); // updates the JSON file with the information from the JSONObject
					initialize(); // redraws the window based on the information from the updated JSON file
				} catch (IOException e1) {
					e1.printStackTrace();
				}
			}
		});

		controls.getSave().addMouseListener(new MouseAdapter() {
			/**
			 * This method updates text information of all the tasks stored in the JSON file with the current text written in the 
			 * text areas of the tasks shown in the window
			 * 
			 * @throws IOException
			 */
			@Override
			public void mousePressed(MouseEvent e) {
				try {
					/* goes through all the Note objects that were added in the frame and uses their information to update the 
					 * tasks in the JSON file (The id numbers are used to identify which objects are updated in the JSON file) */
					for (Component note: list.getComponents()) {
						if (note instanceof Note) {
							int id = ((Note) note).getID(); // gets the tasks address
							String text = ((Note) note).getTextArea().getText(); // gets the text information of the task
							boolean state = ((Note) note).getState(); // determines weather the task is completed or not
							storage.put(Integer.toString(id), Integer.toString(id) + "/" + text + "/" + state); // Updates the task with this 'id'
						}
					}
					
					// updates the indicator at the bottom right to say that the tasks are all saved
					controls.getCheckIfSaved().setText("Saved");
					// updates the unsavedTexts to be empty since all the text information of the tasks are saved
					unsavedTexts.clear();
					
					save(); // updates the JSON file with the information from the JSONObject
					initialize(); // redraws the window based on the information from the updated JSON file
				} catch (IOException e1) {
					e1.printStackTrace();
				}
			}
		});
	}
	
	/**
	 * This method saves all the contents in the JSONObject of "storage" into the JSON file
	 * @throws IOException
	 */
	public void save() throws IOException {
		// updates the JSON file with the contents of storage
		FileWriter file = new FileWriter(PATH);
		file.write(storage.toString());
		file.close();
	}
	
	/**
	 * Redraws all the tasks using the saved task information stored in the JSON file. This allows tasks made in previous program 
	 * call to be redrawn in the current program call.
	 * 
	 * @throws IOException
	 */
	public void initialize() {
		// Removes the previous list from the frame & makes a new list & scroll bar based based on the updated task information of the JSON file
		this.remove(scrollBar);
		list = new List();
		scrollBar = new JScrollPane(list, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
				
		// goes through all the data of each task stored in the JSON file to re-draw their JPanels
		for (Iterator key=storage.keys(); key.hasNext();) {
			// Gets the information about of a task and separates them into the task's id, text information, & weather its completed or not 
			String[] output = storage.get(key.next().toString()).toString().split("/"); 
			int id = Integer.parseInt(output[0]);
			String text = output[1];
			boolean state = Boolean.parseBoolean(output[2]);
			
			// Makes the Note object form the task (Note is the JPanel that contains all the information about a tasks and its functions)
			Note note;
			
			/* Updates the Note object with the unsaved text written in the text area  
			 * said unsaved text from disappearing when redrawing the task by calling the initialize() function again */  
			if (unsavedTexts.containsKey(id)) {
				note = new Note(id, unsavedTexts.get(id), state);
			}
			else {
				note = new Note(id, text, state);
			}
			
			// adds the JPanel representing the task into the list JPanel
			list.add(note);
			
			note.getCompleted().addMouseListener(new MouseAdapter() {
				/**
				 * This method updates the task information stored in the JSON file of the current Note object by changing the state
				 * of the task to be 'complete' if 'uncompleted' or 'uncompleted' if 'complete' when the 'Completed' of the Note object 
				 * is clicked
				 * 
				 * @throws IOException
				 */
				public void mousePressed(MouseEvent e) {
					try {
						/* check the current state of the task, if the task if complete then change its state to false, and if the 
						 * task is uncompleted then change its state to true */
						if (state) {
							storage.put(Integer.toString(id), id + "/" + text + "/false");
						}
						else {
							storage.put(Integer.toString(id), id + "/" + text + "/true");
						}
						
						
						save(); // updates the JSON file with the information from the JSONObject
						initialize(); // redraws the window based on the information from the updated JSON file
					} catch (IOException e1) {
						e1.printStackTrace();
					}
				}
			});
			
			note.getDelete().addMouseListener(new MouseAdapter() {
				/**
				 * This method deletes the task information stored in the JSON file of the current Note object when the delete button 
				 * of the Note Object is clicked
				 * 
				 * @throws IOException
				 */
				public void mousePressed(MouseEvent e) {
					try {
						// removes this task from the JSON file so that it can't be redrawn again when the initialize() function is called
						storage.remove(Integer.toString(id));
						// removes any unsaved texts this task may've had
						unsavedTexts.remove(id);
						
						save(); // updates the JSON file with the information from the JSONObject
						initialize(); // redraws the window based on the information from the updated JSON file
					} catch (IOException e1) {
						e1.printStackTrace();
					}
				}
			});
			
			note.getTextArea().addKeyListener(new KeyAdapter() {
				/**
				 * This methods updates the notification at the bottom right in the control panel telling weather all the tasks are saved 
				 * or not.
				 * 
				 * @throws IOException
				 */
				@Override
				public void keyPressed(KeyEvent e) {
					/* If the text area of the Note Objects representing the tasks are modified in anyway, the notification in 
					 * the control panel is changed to 'Unsaved'. Only when the Save button in the control panel is checked will 
					 * that notification be turned back to 'saved' */
					String thisText = note.getTextArea().getText(); // gets the text from the text area of this Note object
					controls.getCheckIfSaved().setText("Unsaved"); // changes the notification in the control panel to 'Unsaved'
					unsavedTexts.put(id, thisText); // stores the unsaved text in a temporary map to redraw when initialize() is called again
				}
			});
	     }     
		
		/* Adds the new List object filled with Note objects representing all the tasks stored in the JSON file into the frame to 
		 * redraw/update the 'To Do List' window */
		scrollBar = new JScrollPane(list, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_NEVER); // A vertical scroll bar is added to the fram if it overfills
		this.add(scrollBar);
		revalidate(); // repaints the window screen with the updated frame object
	}
}

