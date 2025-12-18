package Pages;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import com.google.common.base.Verify;


public class ProductsAndCart {
    private WebDriver driver;
    public ProductsAndCart(WebDriver driver) {
        this.driver = driver;
    }
    public void clickFirstProduct(){
        WebElement firstProduct = driver.findElement(By.xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div/div[2]/div/div/div/div[1]/prod-grid-box"));
        firstProduct.click();
    }
    public void addToCart(){
        WebElement addProductToCart = driver.findElement(By.xpath("//*[@id=\"cartu-add-to-cart-btn-x\"]/a"));
        addProductToCart.click();
    }
    public void viewCart(){
        WebElement viewCart = driver.findElement(By.xpath("/html/body/div[4]/div[1]/div/div[2]/div/a"));
        viewCart.click();
    }
    public void deleteFromCart(){
        WebElement deleteProductFromCart = driver.findElement(By.xpath("/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr/td[3]/a/i"));
        deleteProductFromCart.click();
    }
    public void addToWishlist(){
        WebElement addProductToWishlist = driver.findElement(By.xpath("/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/md-card/md-card-content/div[1]/a"));
        addProductToWishlist.click();
    }
    public void chooseWishList(){
        WebElement chooseWishlist = driver.findElement(By.xpath("/html/body/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/md-card/md-card-content/div[1]/div/div[1]"));
        chooseWishlist.click();
    }
    public void goToWishlist(){
        WebElement clickWishlist = driver.findElement(By.xpath("/html/body/div[4]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[3]/ul/li[3]/a"));
        clickWishlist.click();
    }
    public void removeFromWishlist(){
        WebElement removeItemFromWishlist = driver.findElement(By.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div/md-card/md-card-content/md-list/md-card/md-card-actions/i[2]"));
        removeItemFromWishlist.click();
        WebElement confirmRemove = driver.findElement(By.xpath("/html/body/div[9]/md-dialog/md-dialog-actions/button[2]"));
        confirmRemove.click();
    }
}
