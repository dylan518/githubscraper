package com.gobinda.Recipe.Management.System.controllers;

import com.gobinda.Recipe.Management.System.models.Comment;
import com.gobinda.Recipe.Management.System.models.Dto.AuthenticationInputDto;
import com.gobinda.Recipe.Management.System.models.Recipe;
import com.gobinda.Recipe.Management.System.models.UserRecipeBody;
import com.gobinda.Recipe.Management.System.services.RecipeService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@Validated
public class RecipeController {
    @Autowired
    RecipeService recipeService;


    @PostMapping("recipe")
    public String addRecipe(@Valid @RequestBody UserRecipeBody userRecipeBody){
        return recipeService.addRecipes(userRecipeBody);
    }
    @GetMapping("recipes")
    public List<Recipe> getAllRecipes(){
        return recipeService.getAllRecipes();
    }
    @PutMapping("recipes/name/{name}")
    public String updateRecipe(@Valid @RequestBody UserRecipeBody userRecipeBody,@PathVariable String name){
        return recipeService.updateRecipe(userRecipeBody,name);
    }
    @DeleteMapping("recipes/name/{name}")
    public String deleteRecipe(@Valid @RequestBody AuthenticationInputDto authInfo,@PathVariable String name){
        return recipeService.deleteRecipe(authInfo,name);
    }


}
