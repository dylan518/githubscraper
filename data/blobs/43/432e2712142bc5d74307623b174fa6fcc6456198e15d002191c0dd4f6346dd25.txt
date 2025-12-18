public class Problem2 {
    public static class Person{
        private String SSN;
        private String name;
        private String gender;
        private Person spouse = null;

        public Person(String SSN, String name, String gender) {
            this.SSN = SSN;
            this.name = name;
            this.gender = gender;
        }

        public void display(){
            if (this != null) {
                System.out.println(SSN);
                System.out.println(name);
                System.out.println(gender);
            }
        }

        public void marry(Person Y){
            if (this.gender != Y.gender &&
                this.spouse == null &&
                Y.spouse == null &&
                this != Y)
            {
                this.spouse = Y;
                Y.spouse = this;
            }
        }

        public void divorce(){
            if (this.spouse != null){
                Person Y = this.spouse;
                this.spouse = null;
                Y.spouse = null;
            }
        }

        public void displaySpouse(){
            if (spouse != null) {
                spouse.display();
            }
            else {
                System.out.println("There is no spouse");
            }
        }
    }

    public static void main(String[] args) {
        Person X = new Person("77", "Alice", "F");
        Person Y = new Person("39", "Bob", "M");
        Person Z = new Person("55", "Carol", "F");

        System.out.println("Part 1: ");
        X.display();

        System.out.println("\nPart 2.1: ");
        X.marry(Z);
        X.displaySpouse();

        System.out.println("\nPart 2.2: ");
        X.marry(Y);
        Y.displaySpouse();

        System.out.println("\nPart 2.3: ");
        Y.divorce();
        Y.marry(Z);
        Z.displaySpouse();
    }
}
