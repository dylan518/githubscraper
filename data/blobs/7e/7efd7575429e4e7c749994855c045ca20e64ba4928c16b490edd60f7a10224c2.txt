package CorpNetApp.pom.test.testCompany.TestCases_Pay_Order;

import CorpNetApp.pom.base.BaseTest;
import CorpNetApp.pom.page.LoginPage.CompanyUsersLoginPage;
import CorpNetApp.pom.page.corpnet_Company_MenuPages.company_Maker_MenuPages.BulkPayOrderTransactionPageByComMaker;
import CorpNetApp.pom.util.GeneralUtil;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class TC_PO_Many_Many_Bulk_TransactionByMaker extends BaseTest {
    BulkPayOrderTransactionPageByComMaker bulkPayOrderTransactionPageByComMaker;

    public TC_PO_Many_Many_Bulk_TransactionByMaker() {
        super();
    }

    @BeforeMethod
    public void setUp() {
        initialization();
        bulkPayOrderTransactionPageByComMaker = new CompanyUsersLoginPage().CompMCUserLogin(getTranMCUser(), getMakerPass()).clickPOBulkMenu();
    }

    @Test
    public void initiateSingleBulkPayOrderTransactionSuccess() throws InterruptedException {
        bulkPayOrderTransactionPageByComMaker = bulkPayOrderTransactionPageByComMaker
                .fileUpload()
                .fillRemarks()
                .selectBearer(1)
                .selectDeliveryLocation(1)
                .clickDebitModeMultiBtn()
                .clickUploadBtn()
                .clickConfirmBtn();

        Thread.sleep(10000);
    }

    @AfterMethod
    public void TearDown() {
        GeneralUtil.waitForDomStable();
        driver.quit();
    }

}
