package HomeWork3.Task3;

public class Money {

    private String name;
    private Integer convertToRub;

    public Money(String name, Integer convertToRub) {
        this.name = name;
        this.convertToRub = convertToRub;
    }

    public String getName() {
        return name;
    }

    public Integer getConvertToRub() {
        return convertToRub;
    }
}
