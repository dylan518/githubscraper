/* 
 * Author: Sinthuja Jeevarajhan
 * Assignment 2: Wordle
 * Professor: Bryan Sarlo
 * Purpose: Program to simulate simple wordle game to allow users to guess a 'Mystery' Word
 */
public class ExtendedLetter extends Letter {
	// initialize variables and constants
	private String content;
	private int family;
	private boolean related;
	private static final int SINGLETON = -1;

	// ExtendedLetter constructor takes in parameter s
	public ExtendedLetter(String s) {
		super('c');
		// sets content to parameter s
		this.content = s;
		// sets related to false
		this.related = false;
		// sets family to constant singleton
		this.family = SINGLETON;
	}

	// Overrloaded ExtendedLetter method- parameter String s and int fam
	public ExtendedLetter(String s, int fam) {
		this(s);

		if (fam < 0) {
			return;
		}
		this.family = fam;

	}

	// equals method- returns true if return true if the instance variable content
	// of other is equal to the instance variable content of this object;
	public boolean equals(Object other) {
		// returns true if other is not of the class ExtendedLetter
		if (!(other instanceof ExtendedLetter)) {
			return false;
		}

		ExtendedLetter other_object = (ExtendedLetter) other;
		this.related = other_object.family == this.family && this.family >= 0;

		return other_object.content.equals(this.content);
	}

	// Overrides toString method; if this object is unusued and related it will
	// return .(content). else it will return (decorator)content(decorator)-
	// decorator return value
	public String toString() {
		if (isUnused() && related) {
			return ("." + content + ".");
		}

		else {
			return super.decorator() + content + super.decorator();
		}

	}

	// Returns array letters with content recieved as a parameter
	public static Letter[] fromStrings(String[] content, int[] codes) {
		Letter[] letters = new Letter[content.length];

		for (int i = 0; i < content.length; i++) {
			if (codes == null) {
				letters[i] = new ExtendedLetter(content[i]);
			} else {
				letters[i] = new ExtendedLetter(content[i], codes[i]);
			}
		}
		return letters;
	}

}
