
package model;

import java.io.Serializable;
import java.util.Date;



public class Director implements Serializable{
  public static final long serialVersionUID = -5936344695567639948L;
    private Integer directorId;
    
    private String dirName;
    
    private Date dob;
   
    private String contact;
    
    private Company company;

    public Director() {
    }

    public Director(Integer directorId) {
        this.directorId = directorId;
    }

    public Director(Integer directorId, String dirName, Date dob, String contact, Company company) {
        this.directorId = directorId;
        this.dirName = dirName;
        this.dob = dob;
        this.contact = contact;
        this.company = company;
    }

    public Integer getDirectorId() {
        return directorId;
    }

    public void setDirectorId(Integer directorId) {
        this.directorId = directorId;
    }

    public String getDirName() {
        return dirName;
    }

    public void setDirName(String dirName) {
        this.dirName = dirName;
    }

    public Date getDob() {
        return dob;
    }

    public void setDob(Date dob) {
        this.dob = dob;
    }

    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }

    public Company getCompany() {
        return company;
    }

    public void setCompany(Company company) {
        this.company = company;
    }

    @Override
    public String toString() {
        return dirName;
    }

    
    
}


