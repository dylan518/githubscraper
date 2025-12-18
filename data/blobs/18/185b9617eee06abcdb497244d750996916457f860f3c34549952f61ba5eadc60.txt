package AssetsPackage.ProductPackage;

import java.util.Date;

public class Product {

    //Product class and properties

    private String name;
    private String productId;
    private String marketId;
    private String productCategory;
    private Date dateOfProduction;
    private Date dateOfRecommendedLastConsumption;
    private Date dateOfRegisteredInMarket;
    private Date dateOfPurchase;

    public Product() {
        this.name = "";
        this.productId = "";
        this.marketId = "";
        this.productCategory = "";
        this.dateOfProduction = null;
        this.dateOfRecommendedLastConsumption = null;
        this.dateOfRegisteredInMarket = null;
        this.dateOfPurchase = null;
    }

    public Product(String name, String productId, String marketId, String productCategory, Date dateOfProduction, Date dateOfRecommendedLastConsumption, Date dateOfRegisteredInMarket, Date dateOfPurchase) {
        this.name = name;
        this.productId = productId;
        this.marketId = marketId;
        this.productCategory = productCategory;
        this.dateOfProduction = dateOfProduction;
        this.dateOfRecommendedLastConsumption = dateOfRecommendedLastConsumption;
        this.dateOfRegisteredInMarket = dateOfRegisteredInMarket;
        this.dateOfPurchase = dateOfPurchase;
    }

    public Product(Product product) {
        this.name = product.name;
        this.productId = product.productId;
        this.marketId = product.marketId;
        this.productCategory = product.productCategory;
        this.dateOfProduction = product.dateOfProduction;
        this.dateOfRecommendedLastConsumption = product.dateOfRecommendedLastConsumption;
        this.dateOfRegisteredInMarket = product.dateOfRegisteredInMarket;
        this.dateOfPurchase = product.dateOfPurchase;
    }
}
