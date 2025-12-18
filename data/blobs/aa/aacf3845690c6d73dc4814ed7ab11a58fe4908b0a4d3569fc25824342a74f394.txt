package br.edu.insper.desagil.aula13.view;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.LinkedList;

import javax.swing.BoxLayout;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

import br.edu.insper.desagil.aula13.model.Calculator;

public class View extends JPanel implements ActionListener {
	private static final long serialVersionUID = -8993461098644349719L;

	private final JComboBox<Calculator> menu;
	private CalculatorView calculatorView;

	public View(LinkedList<Calculator> model) {
		menu = new JComboBox<>();
		for (Calculator calculator : model) {
			menu.addItem(calculator);
		}

		setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));

		add(menu);
		addCalculatorView(0);

		menu.addActionListener(this);
	}

	private void addCalculatorView(int index) {
		Calculator calculator = menu.getItemAt(index);
		calculatorView = new CalculatorView(calculator);
		add(calculatorView);
	}

	@Override
	public void actionPerformed(ActionEvent event) {
		remove(calculatorView);
		int index = menu.getSelectedIndex();
		addCalculatorView(index);
		((JFrame) SwingUtilities.getRoot(this)).pack();
	}
}
