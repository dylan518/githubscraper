package RegistraionClass;

public class RegClass {

    private String email;
    private String userName;
    private String password;

    public void setEmail(String email) {
        if(isValidEmail(email)) {
            this.email = email;
        } else {
            System.out.println("Invalid Email");
        }
    }

    public void setUserName(String userName) {
        if(isValidUserName(userName)) {
            this.userName = userName;
        } else {
            System.out.println("Invalid Username");
        }
    }

    public void setPassword(String password) {
        if(isValidPassword(password)) {
            this.password = password;
        } else {
            System.out.println("Invalid Password");
        }

    }

    private boolean isValidEmail(String email) {
        return email != null && email.endsWith("yahoo.com");
    }

    private boolean isValidUserName(String userName) {
        return userName != null && userName.length() > 6;
    }

    private boolean isValidPassword(String password) {
        return password != null && password.length() > 6 && !password.contains(userName);
    }

    public void displayInformation() {
        System.out.println("Registration Information: ");
        System.out.println("Username: " + userName);
        System.out.println("Email: " + email);
        System.out.println("Password: " + password);
    }

    public static void main(String[] args) {
        RegClass main = new RegClass();
        main.setEmail("alexk147@yahoo.com");
        main.setUserName("alexk147");
        main.setPassword("pass123");

        main.displayInformation();
    }
}
