package dev.redonkuci.manuopsmanufacturingapp.dtos.Stock;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import lombok.Data;

import java.time.LocalDate;

@Data
public class StockViewDto {
    @NotBlank(message = "Product number is required")
    @Size(max = 50, message = "Product number must not exceed 50 characters")
    private String productNumber;

    @NotBlank(message = "Item name is required")
    @Size(max = 100, message = "Item name must not exceed 100 characters")
    private String itemName;

    @NotBlank(message = "Category is required")
    @Size(max = 50, message = "Category must not exceed 50 characters")
    private String category;

    @NotNull(message = "Quantity is required")
    @Min(value = 0, message = "Quantity cannot be negative")
    private Integer quantity;

    @NotBlank(message = "Unit is required")
    @Size(max = 20, message = "Unit must not exceed 20 characters")
    private String unit;

    @Min(value = 0, message = "Reorder level cannot be negative")
    private Integer reorderLevel;

    @Size(max = 100, message = "Supplier name must not exceed 100 characters")
    private String supplier;

    @NotBlank(message = "Storage location is required")
    @Size(max = 100, message = "Storage location must not exceed 100 characters")
    private String storageLocation;

    private LocalDate expiryDate;

    private LocalDate addedDate;
}
