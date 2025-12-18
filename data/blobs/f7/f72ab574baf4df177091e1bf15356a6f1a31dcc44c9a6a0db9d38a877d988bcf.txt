package jobs;

public enum Config {
    VALID(1, "Valid Configuration"),
    INVALID(2, "Invalid Configuration");

    Config(int code, String description) {
        this.code = code;
        this.jobDesc = description;
    }
    private final int code;
    private final String jobDesc;

}
