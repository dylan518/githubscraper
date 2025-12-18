package com.example.segurityshoppingcart.Segurity.Controller;

import java.util.List;
import java.util.Optional;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.segurityshoppingcart.Base.Controller.ABaseController;
import com.example.segurityshoppingcart.Base.DTO.ApiResponseDto;
import com.example.segurityshoppingcart.Segurity.DTO.IUserDto;
import com.example.segurityshoppingcart.Segurity.DTO.IUserModuleDto;
import com.example.segurityshoppingcart.Segurity.DTO.IUserViewDto;
import com.example.segurityshoppingcart.Segurity.DTO.SaveUserPersonDto;
import com.example.segurityshoppingcart.Segurity.Entity.User;
import com.example.segurityshoppingcart.Segurity.IService.IUserService;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("v1/api/user")
public class UserController extends ABaseController<User,IUserService>{
	public UserController(IUserService service) {
        super(service, "User");
    }
	
	  @GetMapping("/login/{username}/{password}")
	    public ResponseEntity<ApiResponseDto<Optional<IUserDto>>> login(@PathVariable String username, @PathVariable String password) {
	        try {
	            Optional<IUserDto> entity = service.getUserByLogin(username, password);
	            return ResponseEntity.ok(new ApiResponseDto<Optional<IUserDto>>("Registro encontrado", entity, true));
	        } catch (Exception e) {
	            return ResponseEntity.internalServerError().body(new ApiResponseDto<Optional<IUserDto>>(e.getMessage(), null, false));
	        }
	    }
	    @PostMapping("/userPerson")
	    public ResponseEntity<ApiResponseDto<User>> saveUserPerson(@RequestBody SaveUserPersonDto userPerson ) {
	        try {
	            return ResponseEntity.ok(new ApiResponseDto<User>("Datos guardados", service.saveUserPerson(userPerson), true));
	        } catch (Exception e) {
	            return ResponseEntity.internalServerError().body(new ApiResponseDto<User>(e.getMessage(), null, false));
	        }
	    }
		  @GetMapping("/view/{id}")
		    public ResponseEntity<ApiResponseDto<List<IUserViewDto>>> getUserView(@PathVariable Long id) {
		        try {
		            List<IUserViewDto> entity = service.getUserView(id);
		            return ResponseEntity.ok(new ApiResponseDto<List<IUserViewDto>>("Registro encontrado", entity, true));
		        } catch (Exception e) {
		            return ResponseEntity.internalServerError().body(new ApiResponseDto<List<IUserViewDto>>(e.getMessage(), null, false));
		        }
		    }
		  @GetMapping("/module/{id}")
		    public ResponseEntity<ApiResponseDto<List<IUserModuleDto>>> getUserModule(@PathVariable Long id) {
		        try {
		            List<IUserModuleDto> entity = service.getUserModule(id);
		            return ResponseEntity.ok(new ApiResponseDto<List<IUserModuleDto>>("Registro encontrado", entity, true));
		        } catch (Exception e) {
		            return ResponseEntity.internalServerError().body(new ApiResponseDto<List<IUserModuleDto>>(e.getMessage(), null, false));
		        }
		    }
}
