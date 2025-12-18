package ar.com.utn.frc.msi.tpi.vipFarmaBackEnd.entity;

import ar.com.utn.frc.msi.tpi.vipFarmaBackEnd.model.stock.Stock;
import ar.com.utn.frc.msi.tpi.vipFarmaBackEnd.model.stock.StockStatus;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class StockSummaryEntity {

    private ProductEntity product;
    private StockStatus stockStatus;
    private LockerEntity lockerId;
    private Long value;

    public StockSummaryEntity(ProductEntity product, Long value) {
        this.product = product;
        this.value = value;
    }

    public StockSummaryEntity(StockStatus stockStatus, Long value) {
        this.stockStatus = stockStatus;
        this.value = value;
    }

    public StockSummaryEntity(LockerEntity lockerId, Long value) {
        this.lockerId = lockerId;
        this.value = value;
    }

    public StockSummaryEntity(ProductEntity product, StockStatus stockStatus, Long value) {
        this.product = product;
        this.stockStatus = stockStatus;
        this.value = value;
    }
}
