package entity;

import javax.persistence.*;
import java.util.Collection;
import java.util.List;
import java.util.Set;

@Entity
public class Customer {
    @Id
    private String contact;
    private String mail;
    private String name;
    public Customer() {
    }

    public Customer(String contact, String mail, String name) {
        this.contact = contact;
        this.mail = mail;
        this.name = name;
    }

    public String getId() {
        return contact;
    }

    public void setId(String id) {
        this.contact = contact;
    }

    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }

}
