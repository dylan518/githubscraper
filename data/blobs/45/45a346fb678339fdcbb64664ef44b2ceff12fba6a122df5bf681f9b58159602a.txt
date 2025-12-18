
package eapli.base.customer.application;


import eapli.base.customer.domain.model.Customer;
import eapli.base.infrastructure.persistence.PersistenceContext;
import eapli.base.product.application.SearchProductCatalogService;
import eapli.base.product.domain.model.InternalCode;
import eapli.base.product.domain.model.Product;
import eapli.base.product.repositories.ProductRepository;
import eapli.framework.infrastructure.authz.application.AuthorizationService;


public class AddToShoppingCartController {
    private AuthorizationService authorizationService;
    private final ProductRepository productRepository = PersistenceContext.repositories().products();
    SearchProductCatalogService svc = new SearchProductCatalogService();
    private Customer cust;


    public AddToShoppingCartController(){

    }

    public Iterable<Product> getAvailableProducts(){
        return svc.availableProducts();
    }


    public boolean AddProductToShoppingCart(String id){
        InternalCode ic=new InternalCode(id);
        Product p= (Product)productRepository.findProductByInternalCode(ic);
        if(p==null)
            return false;

        cust.getShoppingCart().addProduct(p);
        return true;
    }
}