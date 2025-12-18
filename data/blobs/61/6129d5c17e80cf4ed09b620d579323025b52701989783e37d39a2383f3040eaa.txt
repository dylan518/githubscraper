public class Person {
    private String surname;
    private String name;

    public Person(String surname, String name) {
        this.surname = surname;
        this.name = name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    @Override
    public String toString() {
        return surname + name;
    }
}
