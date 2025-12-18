public class SignUpForm {
    private TextBox usernameTextBox = new TextBox();
    private TextBox passwordTextBox = new TextBox();
    private CheckBox checkBox = new CheckBox();
    private Button signUpButton = new Button();

    public SignUpForm() {
        usernameTextBox.addEventHandler(this::enableButton);
        passwordTextBox.addEventHandler(this::enableButton);
        checkBox.addEventHandler(this::enableButton);
        signUpButton.addEventHandler(this::logCredentials);
    }

    private Boolean isFormValid() {
        return !usernameTextBox.getContent().isEmpty()
                && !passwordTextBox.getContent().isEmpty()
                && checkBox.isChecked();
    }

    private void enableButton() {
        if (!isFormValid())
            return;
        signUpButton.setEnabled(true);
    }

    private void logCredentials() {
        System.out.println("Credentials Logged:");
        System.out.println("usernameTextBox: " + usernameTextBox.getContent());
        System.out.println("passwordTextBox: " + passwordTextBox.getContent());
        System.out.println("checkBox: " + checkBox.isChecked());
        System.out.println("signUpButton: " + signUpButton.isEnabled());
    }

    public void simulateInteraction() {
        usernameTextBox.setContent("Usf3md");
        passwordTextBox.setContent("Pasword 123");
        checkBox.setChecked(true);
    }
}
