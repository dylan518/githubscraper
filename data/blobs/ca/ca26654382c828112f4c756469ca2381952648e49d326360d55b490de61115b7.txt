package RentACar_pack1.webApi.controllers;

import RentACar_pack1.dataAccess.abstracts.BrandService;
import RentACar_pack1.entities.Brand;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController //annotation
@RequestMapping("/api/brands")
public class BrandsController   {

    private  BrandService brandService;

    public BrandsController() {

    }
    @Autowired
    public BrandsController( BrandService brandService)
    {
        this.brandService = brandService;
    }
    @GetMapping("/get-all")
    public List<Brand> getAll(){
        return brandService.getAll();
    }
}
