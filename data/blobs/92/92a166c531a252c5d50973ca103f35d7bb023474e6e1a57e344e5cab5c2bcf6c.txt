package com.fdx.api.model46.modelimpl;

import java.util.Objects;

import javax.validation.Valid;

import com.fasterxml.jackson.annotation.JsonProperty;

import io.swagger.annotations.ApiModelProperty;

/**
 * Tax1098MaAllOf
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2021-05-31T16:14:56.890768600+05:30[Asia/Calcutta]")
public class Tax1098MaAllOf   {
  @JsonProperty("filerNameAddress")
  private NameAddressPhone filerNameAddress;

  @JsonProperty("filerTin")
  private String filerTin;

  @JsonProperty("homeownerTin")
  private String homeownerTin;

  @JsonProperty("homeownerNameAddress")
  private NameAddress homeownerNameAddress;

  @JsonProperty("accountNumber")
  private String accountNumber;

  @JsonProperty("totalMortgagePayments")
  private Double totalMortgagePayments;

  @JsonProperty("mortgageAssistancePayments")
  private Double mortgageAssistancePayments;

  @JsonProperty("homeownerMortgagePayments")
  private Double homeownerMortgagePayments;

  public Tax1098MaAllOf filerNameAddress(NameAddressPhone filerNameAddress) {
    this.filerNameAddress = filerNameAddress;
    return this;
  }

  /**
   * Get filerNameAddress
   * @return filerNameAddress
  */
  @ApiModelProperty(value = "")

  @Valid

  public NameAddressPhone getFilerNameAddress() {
    return filerNameAddress;
  }

  public void setFilerNameAddress(NameAddressPhone filerNameAddress) {
    this.filerNameAddress = filerNameAddress;
  }

  public Tax1098MaAllOf filerTin(String filerTin) {
    this.filerTin = filerTin;
    return this;
  }

  /**
   * FILER'S TIN
   * @return filerTin
  */
  @ApiModelProperty(value = "FILER'S TIN")


  public String getFilerTin() {
    return filerTin;
  }

  public void setFilerTin(String filerTin) {
    this.filerTin = filerTin;
  }

  public Tax1098MaAllOf homeownerTin(String homeownerTin) {
    this.homeownerTin = homeownerTin;
    return this;
  }

  /**
   * HOMEOWNER'S TIN
   * @return homeownerTin
  */
  @ApiModelProperty(value = "HOMEOWNER'S TIN")


  public String getHomeownerTin() {
    return homeownerTin;
  }

  public void setHomeownerTin(String homeownerTin) {
    this.homeownerTin = homeownerTin;
  }

  public Tax1098MaAllOf homeownerNameAddress(NameAddress homeownerNameAddress) {
    this.homeownerNameAddress = homeownerNameAddress;
    return this;
  }

  /**
   * Get homeownerNameAddress
   * @return homeownerNameAddress
  */
  @ApiModelProperty(value = "")

  @Valid

  public NameAddress getHomeownerNameAddress() {
    return homeownerNameAddress;
  }

  public void setHomeownerNameAddress(NameAddress homeownerNameAddress) {
    this.homeownerNameAddress = homeownerNameAddress;
  }

  public Tax1098MaAllOf accountNumber(String accountNumber) {
    this.accountNumber = accountNumber;
    return this;
  }

  /**
   * Account number
   * @return accountNumber
  */
  @ApiModelProperty(value = "Account number")


  public String getAccountNumber() {
    return accountNumber;
  }

  public void setAccountNumber(String accountNumber) {
    this.accountNumber = accountNumber;
  }

  public Tax1098MaAllOf totalMortgagePayments(Double totalMortgagePayments) {
    this.totalMortgagePayments = totalMortgagePayments;
    return this;
  }

  /**
   * Box 1, Total State HFA (Housing Finance Agency) and homeowner mortgage payments
   * @return totalMortgagePayments
  */
  @ApiModelProperty(value = "Box 1, Total State HFA (Housing Finance Agency) and homeowner mortgage payments")


  public Double getTotalMortgagePayments() {
    return totalMortgagePayments;
  }

  public void setTotalMortgagePayments(Double totalMortgagePayments) {
    this.totalMortgagePayments = totalMortgagePayments;
  }

  public Tax1098MaAllOf mortgageAssistancePayments(Double mortgageAssistancePayments) {
    this.mortgageAssistancePayments = mortgageAssistancePayments;
    return this;
  }

  /**
   * Box 2, State HFA (Housing Finance Agency) mortgage assistance payments
   * @return mortgageAssistancePayments
  */
  @ApiModelProperty(value = "Box 2, State HFA (Housing Finance Agency) mortgage assistance payments")


  public Double getMortgageAssistancePayments() {
    return mortgageAssistancePayments;
  }

  public void setMortgageAssistancePayments(Double mortgageAssistancePayments) {
    this.mortgageAssistancePayments = mortgageAssistancePayments;
  }

  public Tax1098MaAllOf homeownerMortgagePayments(Double homeownerMortgagePayments) {
    this.homeownerMortgagePayments = homeownerMortgagePayments;
    return this;
  }

  /**
   * Box 3, Homeowner mortgage payments
   * @return homeownerMortgagePayments
  */
  @ApiModelProperty(value = "Box 3, Homeowner mortgage payments")


  public Double getHomeownerMortgagePayments() {
    return homeownerMortgagePayments;
  }

  public void setHomeownerMortgagePayments(Double homeownerMortgagePayments) {
    this.homeownerMortgagePayments = homeownerMortgagePayments;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Tax1098MaAllOf tax1098MaAllOf = (Tax1098MaAllOf) o;
    return Objects.equals(this.filerNameAddress, tax1098MaAllOf.filerNameAddress) &&
        Objects.equals(this.filerTin, tax1098MaAllOf.filerTin) &&
        Objects.equals(this.homeownerTin, tax1098MaAllOf.homeownerTin) &&
        Objects.equals(this.homeownerNameAddress, tax1098MaAllOf.homeownerNameAddress) &&
        Objects.equals(this.accountNumber, tax1098MaAllOf.accountNumber) &&
        Objects.equals(this.totalMortgagePayments, tax1098MaAllOf.totalMortgagePayments) &&
        Objects.equals(this.mortgageAssistancePayments, tax1098MaAllOf.mortgageAssistancePayments) &&
        Objects.equals(this.homeownerMortgagePayments, tax1098MaAllOf.homeownerMortgagePayments);
  }

  @Override
  public int hashCode() {
    return Objects.hash(filerNameAddress, filerTin, homeownerTin, homeownerNameAddress, accountNumber, totalMortgagePayments, mortgageAssistancePayments, homeownerMortgagePayments);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Tax1098MaAllOf {\n");
    
    sb.append("    filerNameAddress: ").append(toIndentedString(filerNameAddress)).append("\n");
    sb.append("    filerTin: ").append(toIndentedString(filerTin)).append("\n");
    sb.append("    homeownerTin: ").append(toIndentedString(homeownerTin)).append("\n");
    sb.append("    homeownerNameAddress: ").append(toIndentedString(homeownerNameAddress)).append("\n");
    sb.append("    accountNumber: ").append(toIndentedString(accountNumber)).append("\n");
    sb.append("    totalMortgagePayments: ").append(toIndentedString(totalMortgagePayments)).append("\n");
    sb.append("    mortgageAssistancePayments: ").append(toIndentedString(mortgageAssistancePayments)).append("\n");
    sb.append("    homeownerMortgagePayments: ").append(toIndentedString(homeownerMortgagePayments)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

