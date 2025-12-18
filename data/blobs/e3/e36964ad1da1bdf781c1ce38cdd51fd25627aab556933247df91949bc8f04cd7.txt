package Examinations;

import javax.swing.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.time.LocalDate;

public class MRIExamination extends Examination {
    private String urlMRI;
    private int magneticFieldStrength;

    public MRIExamination(String urlMRI, LocalDate date, int magneticFieldStrength){
        super(date);
        this.urlMRI = urlMRI;
        this.magneticFieldStrength = magneticFieldStrength;
    }

    public String getDisplayText(){
        return urlMRI;
    }


    public String getConsoleText(){
        return "MRI: " + magneticFieldStrength + " Tesla, " + date.toString()+", ";
    }

}
