package pages;

import pages.pageElements.ComboBox;
import pages.pageElements.ComboBoxBuilder;

import static com.codeborne.selenide.Selenide.$;

public class SettingsInvoiceTabPage extends ParametersInvoicePage{

/*
*     private static final String INPUT = ".//*[contains(@id,'InvoiceFormOptionsPanel') or " +
            "contains(@id,'InvoiceTCFormOptionsPanel') or " +
            "contains(@id,'SiteOrderFormOptionsPanel')]//*[contains(@id,'%s') and @name='%s']";
    private static final String PICKER = ".//*[contains(@id,'InvoiceFormOptionsPanel') or " +
            "contains(@id,'InvoiceTCFormOptionsPanel') or contains(@id,'SiteOrderFormOptionsPanel')]" +
            "//*[@name='%s']//parent::div//following-sibling::*[contains(@id,'picker')]";
    private static final By DRIVER = By.xpath(String.format(INPUT, "DriverCheckedComboBox", "userDriverId"));
    private static final By DRIVER_PICKER = By.xpath(String.format(PICKER, "userDriverId"));
    *
    * //*[contains(@id,'InvoiceFormOptionsPanel')//*[contains(@id,'DriverCheckedComboBox') and @name='userDriverId']
* */

    public ComboBox driverComboBox;
    public ComboBox collectorComboBox;

    public SettingsInvoiceTabPage() {
        checkPageComponentIsLoaded();
        initElements();
    }

    private void checkPageComponentIsLoaded() {
        System.out.println("SettingsInvoiceTabPage проверка страницы");
    }

    private void initElements() {
        String driverInput = String.format(INPUT_TEMPLATE, "InvoiceFormOptionsPanel_InvoiceFormOptionsPanel", "userDriverId");
        driverComboBox = new ComboBoxBuilder()
                .setInput(driverInput)
                .setPicker(driverInput + PICKER_TEMPLATE)
                .setOptionXpath(OPTION_TEMPLATE)
                .build();
        String collectorInput = String.format(INPUT_TEMPLATE, "InvoiceFormOptionsPanel_InvoiceFormOptionsPanel", "userCollectorId");
        collectorComboBox = new ComboBoxBuilder()
                .setInput(collectorInput)
                .setPicker(collectorInput + PICKER_TEMPLATE)
                .setOptionXpath(OPTION_TEMPLATE)
                .build();

    }

}
