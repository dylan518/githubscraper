
package ch.hearc.dice.gui.controlinput;

import javax.swing.Box;
import javax.swing.BoxLayout;

import ch.hearc.c_gui.tools.decorateur.center.JCenterH;
import ch.hearc.dice.gui.controlinput.display.jcomponent.jtimer.JTimer;
import ch.hearc.dice.gui.controlinput.jcontrol.JControl;
import ch.hearc.dice.gui.controlinput.jinput.JInput;
import ch.hearc.dice.gui.utils.Settings;

public class JRightComponent extends Box
	{

	/*------------------------------------------------------------------*\
	|*							Constructeurs							*|
	\*------------------------------------------------------------------*/


	public JRightComponent()
		{
		super(BoxLayout.Y_AXIS);

		// Tools
			{
			this.jTimer = new JTimer();
			this.jControl = new JControl();
			this.jInput = new JInput();
			}

		geometry();
		control();
		appearance();
		}

	/*------------------------------------------------------------------*\
	|*							Methodes Public							*|
	\*------------------------------------------------------------------*/

	/*------------------------------*\
	|*				Get				*|
	\*------------------------------*/

	/*------------------------------------------------------------------*\
	|*							Methodes Private						*|
	\*------------------------------------------------------------------*/
	private void geometry()
		{
		add(jControl);
		add(jInput);

		add(new JCenterH(this.jTimer));
		add(new JCenterH(this.jInput));
		add(new JCenterH(this.jControl));
		add(Box.createVerticalStrut(Settings.MARGE));
		}

	private void control()
		{
		// rien
		}

	private void appearance()
		{
		// rien
		}

	/*------------------------------------------------------------------*\
	|*							Attributs Private						*|
	\*------------------------------------------------------------------*/

	//tools
	private JTimer jTimer;
	private JControl jControl;
	private JInput jInput;
	}


