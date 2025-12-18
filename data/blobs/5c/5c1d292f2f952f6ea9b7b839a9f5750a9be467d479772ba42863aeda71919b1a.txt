public class User {
    private final String firstName;
    private final String lastName;
    private final int age;
    private final String email;

    private User(Builder builder){
        this.firstName = builder.firstName;
        this.lastName = builder.lastName;
        this.age = builder.age;
        this.email = builder.email;
    }

    public static class Builder{
        private final String firstName;
        private  final String lastName;
        private int age;
        private String email;

        public Builder(String firstName, String lastName){
            this.firstName = firstName;
            this.lastName = lastName;
        }

        public Builder age(int age){
            this.age = age;
            return  this;
        }

        public Builder email(String email){
            this.email = email;
            return this;
        }

        public User build(){
            return  new User(this);
        }
    }
}
