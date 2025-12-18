package sistemadevendas.Sale.Service;

import com.example.sistemadevendas.Sale.Model.Sale;
import com.example.sistemadevendas.Sale.Service.SaleRepository;
import com.example.sistemadevendas.Sale.Service.SaleService;
import org.junit.Before;
import org.junit.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.math.BigDecimal;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;
import static org.mockito.Mockito.when;

public class SaleServiceTest {

    @InjectMocks
    private SaleService saleService;

    @Mock
    private SaleRepository saleRepository;

    @Before
    public void init() {
        MockitoAnnotations.initMocks(this);
    }

    //test cadastrar uma venda
    @Test
    public void testCreateSale_Success() {
        Sale sale = new Sale();
        sale.setProduct_code(123L);
        sale.setProduct_name("Product ABC");
        sale.setPrice_product(BigDecimal.valueOf(10.0));
        sale.setQty_product(5);

        BigDecimal expectedAmount = BigDecimal.valueOf(50.0);

        Sale savedSale = new Sale();
        savedSale.setId(1L);
        savedSale.setProduct_code(123L);
        savedSale.setProduct_name("Product ABC");
        savedSale.setPrice_product(BigDecimal.valueOf(10.0));
        savedSale.setQty_product(5);
        savedSale.setAmount(expectedAmount);

        when(saleRepository.save(sale)).thenReturn(savedSale);

        Sale createdSale = saleService.createSale(sale);

        assertEquals(savedSale, createdSale);
        assertEquals(expectedAmount, createdSale.getAmount());
    }

    @Test
    public void testCreateSale_InvalidData() {
        Sale sale = new Sale();

        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> {
            saleService.createSale(sale);
        });

        assertEquals("product_code e product_name são obrigatórios.", exception.getMessage());
    }

    @Test
    public void testCreateSale_InvalidPriceOrQty() {
        Sale sale = new Sale();
        sale.setProduct_code(123L);
        sale.setProduct_name("Product ABC");
        sale.setPrice_product(BigDecimal.valueOf(10.0));
        sale.setQty_product(0);

        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> {
            saleService.createSale(sale);
        });

        assertEquals("Preço e quantidade são obrigatórios.", exception.getMessage());
    }
}
