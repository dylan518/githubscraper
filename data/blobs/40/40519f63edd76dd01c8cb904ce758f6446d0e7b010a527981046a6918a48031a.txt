package profile;

public enum Gender {

    MALE("Male"),
    FEMALE("Female");

    private String gender;

    Gender(String gender) {
        this.gender = gender;
    }

    @Override
    public String toString() {
        return gender;
    }

    public static Gender getFromString(String genderName) {
        for (Gender gender : Gender.values()) {
            if (gender.gender.equalsIgnoreCase(genderName)) {
                return gender;
            }
        }

        throw new IllegalArgumentException("No enum constant with genderName: " + genderName);
    }
}
