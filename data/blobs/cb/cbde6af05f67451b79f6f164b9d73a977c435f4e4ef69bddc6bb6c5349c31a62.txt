package com.buildfor2030.api.PartnerAPIs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/apis")
public class APIController {

    @Autowired
    private APIService apiService;

    @Autowired
    private CategoryService categoryService;

    @GetMapping
    public ResponseEntity<List<PartnerAPIVO>> getAllAPIs(){
        List<PartnerAPIVO> apis = apiService.retrieveAllAPIs();
        return new ResponseEntity<>(apis, HttpStatus.OK);
    }

    @GetMapping("/{slug}")
    public ResponseEntity<PartnerAPI> getAPI(@PathVariable String slug) {
        PartnerAPI api = apiService.retrieveAPI(slug);
        return new ResponseEntity<>(api, HttpStatus.OK);
    }

    @GetMapping("/categories")
    public ResponseEntity<List<CategoryVO>> getAllCategories(){
        List<CategoryVO> categories = categoryService.retrieveAllCategories();
        return new ResponseEntity<>(categories, HttpStatus.OK);
    }

    @GetMapping("/categories/{slug}")
    public ResponseEntity<List<PartnerAPIVO>> getAPIsByCategory(@PathVariable String slug){
        List<PartnerAPIVO> apis = apiService.retrieveAPIsByCategory(slug);
        return new ResponseEntity<>(apis, HttpStatus.OK);
    }

}
