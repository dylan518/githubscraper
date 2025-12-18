
public class Printer {
	private int tonerLevel;
	private int pagesPrinted;
	private boolean duplex;
	

	public Printer() {}

	public Printer(int tonerLevel, boolean duplex) {
		this.tonerLevel = tonerLevel;
		this.pagesPrinted = 0;
		this.duplex = duplex;
	}
	
	public int addToner(int tonerAmount) {
		int tempTonerLevel = tonerLevel + tonerAmount ;
		
		if(tempTonerLevel >100 || tempTonerLevel < 0) { // i can put it at our constructor
			tonerLevel = tempTonerLevel;
		}else {
			tonerLevel = -1;
		}
		return tonerLevel;
	}
	
	public int printPages(int pagesToPrint) {
		int sheets;
		if(duplex) {
			System.out.println("We have a duplex printer");
			sheets = pagesToPrint;
		}else{
			System.out.println("We don't have a duplex printer");
			sheets = 2*pagesToPrint;
		}
		return sheets;
	}
}
