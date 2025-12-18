package bean;

/**
 * @Description: MedicationProvider Bean
 * @author: Weikang
 * @version: 1.0
 * @date: 29/09/2022 10:49
 */

public class MedicationProvider extends Actor{
    private String org;

    public MedicationProvider() {
    }

    public MedicationProvider(String username, String password, String address, double latitude, double longitude, String tel, String org) {
        super(username, password, address, latitude, longitude, tel);
        this.org = org;
    }

    public String getOrg() {
        return org;
    }

    public void setOrg(String org) {
        this.org = org;
    }

    @Override
    public String toString() {
        return "MedicationProvider{" +
                "org='" + org + '\'' +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                ", address='" + address + '\'' +
                ", latitude=" + latitude +
                ", longitude=" + longitude +
                ", tel='" + tel + '\'' +
                '}';
    }
}
