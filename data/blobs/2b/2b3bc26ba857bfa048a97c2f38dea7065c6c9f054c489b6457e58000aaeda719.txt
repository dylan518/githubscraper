package integration.factory.steps;
import integration.factory.funcs.CartFunc;
import integration.factory.funcs.CheckoutFunc;
import integration.factory.funcs.ProductFunc;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;



public class ProductStep {

    ProductFunc productFunc = new ProductFunc();
    CartFunc cartFunc = new CartFunc();

    CheckoutFunc checkoutFunc = new CheckoutFunc();

    @Given("which I filtered to the {string} item")
    public void filterPrice(String filter){
         productFunc.filterPrice(filter);
    }
    @When("I add the first product to my cart")
    public void addProduct(){
        productFunc.addFirstToCard();
    }
    @And("realize the flow of checkout with my data {string} {string} and {string}")
    public void realizeCheckout(String FirstName, String LastName , String ZipCode){
        cartFunc.advanceCheckout();
        checkoutFunc.formsCheckout(FirstName,LastName,ZipCode);
    }
    @And("remove itens from cart and click to back shopping")
    public void removeItensBackShopping(){
        cartFunc.removeItens();
    }
    @Then("should return to list of items")
    public void validateReturnHomeList(){
        Assert.assertTrue(productFunc.validateLogin());
    }

    @Then("valid that my checkout was a success")
        public void validateCheckoutSuccess() {
            Assert.assertTrue(checkoutFunc.finishCheckout());
        }



    @Then("I should be logged in successfully")
    public void validateLoginSuccess(){
            Assert.assertTrue(productFunc.validateLogin());
     }

}
