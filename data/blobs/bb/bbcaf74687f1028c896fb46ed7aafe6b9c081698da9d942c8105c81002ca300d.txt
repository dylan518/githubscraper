package ss5_access_modifier;

public class Staff {
    // dùng từ khoá private để tạo các thuộc tính.
    // ngăn chặn sự truy cập và thay đổi trực tiếp đến các thông tin đó
    private String name;
    private long numberPhone;
    private String workingParts;
    private String companyName;

    public Staff() {
    }

    //  contructor từ khoá pulic dùng cho toàn bộ project;
    public Staff(String name, long numberPhone, String workingParts, String companyName) {
        this.name = name;
        this.numberPhone = numberPhone;
        this.workingParts = workingParts;
        this.companyName = companyName;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public long getNumberPhone() {
        return numberPhone;
    }

    public void setNumberPhone(long numberPhone) {
        this.numberPhone = numberPhone;
    }

    public String getWorkingParts() {
        return workingParts;
    }

    public void setWorkingParts(String workingParts) {
        this.workingParts = workingParts;
    }

    public String getCompanyName() {
        return companyName;
    }

    public void setCompanyName(String companyName) {
        this.companyName = companyName;
    }

    @Override
    public String toString() {
        return "Staff{" +
                "name='" + name + '\'' +
                ", numberPhone=" + numberPhone +
                ", workingParts='" + workingParts + '\'' +
                ", companyName='" + companyName + '\'' +
                '}';
    }
}
