package com.josecaro.lab_38.models;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import java.util.List;

@Entity
public class Association {

    @Id
    private int id;


    public Association() {

    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Chapter> getChapters() {
        return chapters;
    }

    public void setChapters(List<Chapter> chapters) {
        this.chapters = chapters;
    }

    public Association(int id, String name, List<Chapter> chapters) {
        this.id = id;
        this.name = name;
        this.chapters = chapters;
    }

    private String name;

    @OneToMany(mappedBy = "association")
    private List<Chapter> chapters;
}
