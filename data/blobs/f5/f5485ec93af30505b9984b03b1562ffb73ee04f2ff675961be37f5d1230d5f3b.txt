package models;

import devlApi.RecordStudent;

import java.util.List;

public class Pufendies {
    private List<StudentPufendies> listStudent;

    public Pufendies(){ }

    public void setListStudent(List<StudentPufendies> listStudent) {
        this.listStudent = listStudent;
    }

    public List<StudentPufendies> getListStudent() {
        return listStudent;
    }

    public RecordStudent getMaxPersonalQualities(){

        int temp = 0;
        StudentPufendies student = null;

        for(var item : listStudent){
            if (item.getSumPersonalQualities()> temp){
                temp = item.getSumPersonalQualities();
                student = item;
            }
        }

        return new RecordStudent(student.getNameStudent(), student.getMagi(), student.getDistMagi());
    }

}
