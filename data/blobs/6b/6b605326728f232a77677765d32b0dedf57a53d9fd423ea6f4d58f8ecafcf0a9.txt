package com.juaracoding;

import com.juaracoding.pages.ManagementPendaftaranSendiriPage;
import com.juaracoding.pages.ManagementUserPage;
import com.juaracoding.utils.Constants;
import com.relevantcodes.extentreports.ExtentTest;
import com.relevantcodes.extentreports.LogStatus;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;


public class TestManagementPendaftaranSendiri {

    static WebDriver driver;
    static ExtentTest extentTest;
    static ManagementPendaftaranSendiriPage managementPendaftaranSendiriPage = new ManagementPendaftaranSendiriPage();

    public TestManagementPendaftaranSendiri() {
        driver = Hooks.driver;
        extentTest = Hooks.extentTest;
    }

    @When("User click button pendaftaran sendiri")
    public void user_click_button_pendaftaran_sendiri() {
        Hooks.delay(Constants.DETIK);
        managementPendaftaranSendiriPage.BtnPendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User click button pendaftaran sendiri");
    }
    @And("User click button view data pendaftaran sendiri")
    public void user_click_button_view_data_pendaftaran_sendiri() {
        Hooks.delay(Constants.DETIK);
        managementPendaftaranSendiriPage.BtnViewDataPendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User click button view data pendaftaran sendiri");
    }
    @And("User edit valid divisi pendaftaran sendiri")
    public void user_edit_valid_divisi_pendaftaran_sendiri() {
        Hooks.delay(3);
        managementPendaftaranSendiriPage.InputDivisiPendafataranSendiri("Business Development");
        Hooks.delay(3);
        managementPendaftaranSendiriPage.TestInputDivisiPendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User edit valid divisi pendaftaran user");
    }
    @And("User edit valid unit pendaftaran sendiri")
    public void user_edit_valid_unit_pendaftaran_sendiri() {
        Hooks.delay(3);
        managementPendaftaranSendiriPage.InputUnitPendafataranSendiri("Chef");
        Hooks.delay(3);
        managementPendaftaranSendiriPage.TestInputUnitPendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User edit valid unit pendaftaran sendiri");
    }
    @And("User edit valid tipe kontrak pendaftaran sendiri")
    public void user_edit_valid_tipe_kontrak_pendaftaran_sendiri() {
        Hooks.delay(3);
        managementPendaftaranSendiriPage.InputTipeKontrakPendafataranSendiri();
        Hooks.delay(3);
        managementPendaftaranSendiriPage.TestInputTipeKontrakPendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User edit valid tipe kontrak pendaftaran sendiri");
    }
    @And("User edit valid posisi kerja pendaftaran sendiri")
    public void user_edit_valid_posisi_kerja_pendaftaran_sendiri() {
        Hooks.delay(3);
        managementPendaftaranSendiriPage.InputPosisiKerjaPendafataranSendiri();
        Hooks.delay(3);
        managementPendaftaranSendiriPage.TestInputPosisiKerjaPendaftaranUser();
        extentTest.log(LogStatus.PASS, "User edit valid posisi kerja pendaftaran sendiri");
    }
    @And("User edit valid jabatan pendaftaran sendiri")
    public void user_edit_valid_jabatan_pendaftaran_sendiri() {
        Hooks.delay(3);
        managementPendaftaranSendiriPage.InputJabatanPendafataranSendiri();
        Hooks.delay(3);
        managementPendaftaranSendiriPage.TestInputJabatanPendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User edit valid jabatan pendaftaran sendiri");
    }
    @And("User edit valid lokasi kerja pendaftaran sendiri")
    public void user_edit_valid_lokasi_kerja_pendaftaran_sendiri() {
        Hooks.delay(3);
        managementPendaftaranSendiriPage.InputLokasiKerjaPendafataranSendiri("DIKA Batam");
        Hooks.delay(3);
        managementPendaftaranSendiriPage.TestInputLokasiKerjaPendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User edit valid lokasi kerja pendaftaran sendiri");
    }
    @And("User edit valid jadwal kerja pendaftaran sendiri")
    public void user_edit_valid_jadwal_kerja_pendaftaran_sendiri() {
        Hooks.delay(3);
        managementPendaftaranSendiriPage.InputJadwalKerjaPendafataranSendiri();
        Hooks.delay(3);
        managementPendaftaranSendiriPage.TestInputJadwalKerjaPendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User edit valid jadwal kerja pendaftaran sendiri");
    }
    @And("User edit valid selfie pendaftaran sendiri")
    public void user_edit_valid_selfie_pendaftaran_sendiri() {
        Hooks.delay(3);
        managementPendaftaranSendiriPage.DropdownSelfiePendaftaranSendiri();
        Hooks.delay(3);
        managementPendaftaranSendiriPage.SelectSelfiePendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User edit valid selfie pendaftaran sendiri");
    }
    @And("User edit valid jumlah cuti pendaftaran sendiri")
    public void user_edit_valid_jumlah_cuti_pendaftaran_sendiri() {
        Hooks.delay(3);
        managementPendaftaranSendiriPage.InputJumlahCutiPendafataranSendiri("5");
        extentTest.log(LogStatus.PASS, "User edit valid jumlah cuti pendaftaran sendiri");
    }
    @And("User submit valid data pendaftaran sendiri")
    public void user_submit_valid_data_pendaftaran_sendiri() {
        Hooks.delay(Constants.DETIK);
        managementPendaftaranSendiriPage.BtnSubmitPendaftaranSendiri();
        Hooks.delay(10);
        extentTest.log(LogStatus.PASS, "User submit valid data pendaftaran sendiri");
    }
    @Then("User delete valid data pendaftaran sendiri")
    public void user_delete_valid_data_pendaftaran_sendiri() {
        Hooks.delay(Constants.DETIK);
        managementPendaftaranSendiriPage.BtnPendaftaranSendiri();
        Hooks.delay(3);
        managementPendaftaranSendiriPage.BtnDeleteDataPendaftaranSendiri();
        Hooks.delay(5);
        managementPendaftaranSendiriPage.BtnYesDeletePendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User delete valid data pendaftaran sendiri");
    }
    @When("User delete invalid data pendaftaran sendiri")
    public void user_delete_invalid_data_pendaftaran_sendiri() {
        Hooks.delay(Constants.DETIK);
        managementPendaftaranSendiriPage.BtnPendaftaranSendiri();
        Hooks.delay(3);
        managementPendaftaranSendiriPage.BtnDeleteDataPendaftaranSendiri();
        Hooks.delay(5);
        managementPendaftaranSendiriPage.BtnNoDeletePendaftaranSendiri();
        extentTest.log(LogStatus.PASS, "User delete invalid data pendaftaran sendiri");
    }
    @Then("User get text invalid credentials pendaftaran sendiri")
    public void user_get_text_invalid_credentials_pendaftaran_sendiri() {
        Hooks.delay(Constants.DETIK);
        Assert.assertEquals(managementPendaftaranSendiriPage.getTxtInvalidCredentialsPendaftaranSendiri(),"Data User Registrasi Mobile");
        extentTest.log(LogStatus.PASS,"User get text invalid credentials pendaftaran sendiri");
    }
}
