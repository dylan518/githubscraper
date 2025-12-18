package com.fiscal.codeGenerator.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "gi_nazioni")
public class Nation {
    @Id
    @Column(name = "sigla_nazione", nullable = false, unique = true)
    private String nationCode;
    @Column(name = "codice_belfiore", nullable = false)
    private String belfioreCode;
    @Column(name = "denominazione_nazione", nullable = false)
    private String nationName;
    @Column(name = "denominazione_cittadinanza", nullable = false)
    private String citizenship;

    public Nation() {
    }

    public Nation(String nationCode, String belfioreCode, String nationName, String citizenship) {
        this.nationCode = nationCode;
        this.belfioreCode = belfioreCode;
        this.nationName = nationName;
        this.citizenship = citizenship;
    }

    public String getNationCode() {
        return nationCode;
    }

    public void setNationCode(String nationCode) {
        this.nationCode = nationCode;
    }

    public String getBelfioreCode() {
        return belfioreCode;
    }

    public void setBelfioreCode(String belfioreCode) {
        this.belfioreCode = belfioreCode;
    }

    public String getNationName() {
        return nationName;
    }

    public void setNationName(String nationName) {
        this.nationName = nationName;
    }

    public String getCitizenship() {
        return citizenship;
    }

    public void setCitizenship(String citizenship) {
        this.citizenship = citizenship;
    }

    @Override
    public String toString() {
        return "Nation{" +
                "nationCode='" + nationCode + '\'' +
                ", belfioreCode='" + belfioreCode + '\'' +
                ", nationName='" + nationName + '\'' +
                ", citizenship='" + citizenship + '\'' +
                '}';
    }
}
