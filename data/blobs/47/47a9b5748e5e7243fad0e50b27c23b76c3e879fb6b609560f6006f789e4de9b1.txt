package project.backend.domain.ingredient.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.util.ObjectUtils;
import org.springframework.web.bind.annotation.*;
import project.backend.domain.ingredient.dto.IngredientPatchRequestDto;
import project.backend.domain.ingredient.dto.IngredientPostRequestDto;
import project.backend.domain.ingredient.dto.IngredientResponseDto;
import project.backend.domain.ingredient.entity.Ingredient;
import project.backend.domain.ingredient.mapper.IngredientMapper;
import project.backend.domain.ingredient.service.IngredientService;
import project.backend.global.error.exception.BusinessException;
import project.backend.global.error.exception.ErrorCode;
import springfox.documentation.annotations.ApiIgnore;

import java.util.List;

@Api(tags = "재료 API - 완료 API(프론트 작업 가능)")
@RestController
@RequestMapping("/api/ingredients")
@RequiredArgsConstructor
public class IngredientController {

    private final IngredientService ingredientService;
    private final IngredientMapper ingredientMapper;


    @ApiIgnore
    @PostMapping
    public ResponseEntity postIngredient(@RequestBody(required = false) IngredientPostRequestDto ingredientPostRequestDto) {
        if (ObjectUtils.isEmpty(ingredientPostRequestDto)){
            throw new BusinessException(ErrorCode.MISSING_REQUEST);
        }
        Ingredient ingredient = ingredientService.createIngredient(ingredientPostRequestDto);
        return ResponseEntity.status(HttpStatus.CREATED).body(ingredientMapper.ingredientToIngredientResponseDto(ingredient));
    }

    @ApiIgnore
    @GetMapping("/{ingredientId}")
    public ResponseEntity getIngredient(@PathVariable(required = false) Long ingredientId) {
        if (ObjectUtils.isEmpty(ingredientId)){
            throw new BusinessException(ErrorCode.MISSING_REQUEST);
        }
        IngredientResponseDto ingredientResponseDto = ingredientMapper.ingredientToIngredientResponseDto(ingredientService.getIngredient(ingredientId));
        return ResponseEntity.status(HttpStatus.OK).body(ingredientResponseDto);
    }

    @ApiOperation(value = "전체 재료 목록 조회(재료명, 권고 유통기한_하루기준)")
    @GetMapping
    public ResponseEntity getIngredientList() {
        List<IngredientResponseDto> ingredientResponseDtoList = ingredientMapper.ingredientsToIngredientResponseDtos(ingredientService.getIngredientList());
        return ResponseEntity.status(HttpStatus.OK).body(ingredientResponseDtoList);
    }

    @ApiIgnore
    @PatchMapping("/{ingredientId}")
    public ResponseEntity putIngredient(
            @PathVariable(required = false) Long ingredientId,
            @RequestBody(required = false) IngredientPatchRequestDto ingredientPatchRequestDto) {
        if (ObjectUtils.isEmpty(ingredientId) || ObjectUtils.isEmpty(ingredientPatchRequestDto)){
            throw new BusinessException(ErrorCode.MISSING_REQUEST);
        }
        IngredientResponseDto ingredientResponseDto = ingredientMapper.ingredientToIngredientResponseDto(ingredientService.patchIngredient(ingredientId, ingredientPatchRequestDto));
        return ResponseEntity.status(HttpStatus.OK).body(ingredientResponseDto);
    }

    @ApiIgnore
    @DeleteMapping("/{ingredientId}")
    public ResponseEntity deleteIngredient(@PathVariable(required = false) Long ingredientId) {
        if (ObjectUtils.isEmpty(ingredientId)){
            throw new BusinessException(ErrorCode.MISSING_REQUEST);
        }
        ingredientService.deleteIngredient(ingredientId);
        return ResponseEntity.status(HttpStatus.NO_CONTENT).body(null);
    }
}
