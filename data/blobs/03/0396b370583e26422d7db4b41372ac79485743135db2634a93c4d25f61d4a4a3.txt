package com.northwind.web;

import com.northwind.service.CategoryService;
import com.northwind.web.dto.CategoryDto;
import com.northwind.web.dto.ProductDto;
import jakarta.inject.Inject;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import org.eclipse.microprofile.openapi.annotations.tags.Tag;

import java.util.List;

@Path("/category")
@Tag(name = " category", description = "All the category methods")
public class CategoryResource {
    @Inject
    private CategoryService categoryService;

    @GET
    public List<CategoryDto> findAll(){
        return this.categoryService.findAll();
    }

    @GET
    @Path("/{id}")
    public CategoryDto findById(@PathParam("id") Long id) {
        return this.categoryService.findById(id);
    }

    @GET
    @Path("/{id}/products")
    @Produces(MediaType.APPLICATION_JSON)
    public List<ProductDto> findProductsByCategoryId(@PathParam("id") Long id) {
        return this.categoryService.findProductsByCategoryId(id);
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public CategoryDto create(CategoryDto categoryDto) {
        return this.categoryService.create(categoryDto);
    }

    @DELETE
    @Path("/{id}")
    public void delete(@PathParam("id") Long id) {
        this.categoryService.delete(id);
    }
}
