package decorator;

public class SideDecorator extends Decorator{
    private Character ch;

    public SideDecorator(Printer printer, Character ch) {
        super(printer);
        this.ch = ch;
    }

    @Override
    public int getLinesCount() {
        return printer.getLinesCount();
    }

    @Override
    public int getMaxLength() {
        return printer.getMaxLength() + 2;
    }

    @Override
    public int getLength(int index) {
        return printer.getLength(index) + 2;
    }

    @Override
    public String getString(int index) {
        return ch + printer.getString(index) + ch;
    }
}
