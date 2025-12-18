package com.backend.warehouse.dto;
import com.backend.warehouse.model.Product;
import lombok.Data;
import java.time.LocalDate;

@Data
public class ProductDTO {
    private String productName;
    private String productCode;
    private Integer productQuantity;
    private Integer productMinQuantity;
    private Double productPrice;
    private LocalDate productArriveDate;
    private LocalDate productDepartureDate;
    private Long warehouseId;

    // Pretvaranje entiteta u DTO
    public static ProductDTO fromEntity(Product product) {
        ProductDTO dto = new ProductDTO();
        dto.setProductCode(product.getProductCode());
        dto.setProductName(product.getProductName());
        dto.setProductQuantity(product.getProductQuantity());
        dto.setProductMinQuantity(product.getProductMinQuantity());
        dto.setProductPrice(product.getProductPrice());
        dto.setProductArriveDate(product.getProductArriveDate());
        dto.setProductDepartureDate(product.getProductDepartureDate());
        if (product.getWarehouse() != null) {
            dto.setWarehouseId(product.getWarehouse().getWarehouseId());
        }
        return dto;
    }

    // Pretvaranje DTO-a u entitet
    public static Product toEntity(ProductDTO dto) {
        Product product = new Product();
        product.setProductCode(dto.getProductCode());
        product.setProductName(dto.getProductName());
        product.setProductQuantity(dto.getProductQuantity());
        product.setProductMinQuantity(dto.getProductMinQuantity());
        product.setProductPrice(dto.getProductPrice());
        product.setProductArriveDate(dto.getProductArriveDate());
        product.setProductDepartureDate(dto.getProductDepartureDate());
        return product;
    }
}

