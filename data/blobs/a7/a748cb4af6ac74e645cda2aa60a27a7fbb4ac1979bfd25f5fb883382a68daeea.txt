package com.demoqa.pages;

import com.codeborne.selenide.SelenideElement;
import static com.codeborne.selenide.Condition.text;
import static com.codeborne.selenide.Condition.visible;
import static com.codeborne.selenide.Selenide.$x;


public class TextBoxPage {
    SelenideElement fullName = $x("//input[@id='userName']");
    SelenideElement email = $x("//input[@id='userEmail']");
    SelenideElement currentAddress = $x("//textarea[@placeholder='Current Address']");
    SelenideElement permanentAddress = $x("//textarea[@id='permanentAddress']");
    SelenideElement submitButton = $x("//button[@id='submit']");


    public void scrollTo(String value){
        $x(value).scrollTo();
    }

    public TextBoxPage setFullname(String value) {
        fullName.setValue(value);
        return this;
    }

    public TextBoxPage setEmail(String value) {
        email.sendKeys(value);
        return this;
    }

    public TextBoxPage setCurrentAddress(String value) {
        currentAddress.sendKeys(value);
        return this;
    }

    public TextBoxPage setPermanentAddress(String value) {
        permanentAddress.sendKeys(value);
        return this;
    }

    public TextBoxPage clickSubmitButton() {
        submitButton.click();
        return this;
    }

    public void checkResultFormTextBox(String name, String email, String currentAddress,
                                       String pernamentaddress) {
        $x("//div[@id='output']").shouldBe(visible);
        $x("//div[@id='output']").$("#name").shouldHave(text(name));
        $x("//div[@id='output']").$("#email").shouldHave(text(email));
        $x("//div[@id='output']").$("#currentAddress").shouldHave(text(currentAddress));
        $x("//div[@id='output']").$("#permanentAddress").shouldHave(text(pernamentaddress));

    }


}
