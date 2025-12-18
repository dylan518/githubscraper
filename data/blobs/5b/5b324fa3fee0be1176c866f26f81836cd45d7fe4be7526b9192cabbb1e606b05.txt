package com.eidiko.query.controller;

import com.eidiko.query.dto.IncentiveDTO;
import com.eidiko.query.exception.IncentiveNotFoundException;
import com.eidiko.query.response.ApiResponseEntity;
import com.eidiko.query.service.IncentiveService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/incentives")
@Tag(name = "Incentive")
public class IncentiveController {

    private final IncentiveService incentiveService;

    public IncentiveController(IncentiveService incentiveService) {
        this.incentiveService = incentiveService;
    }

    @GetMapping("/{id}")
    @Operation(
            summary = "gets incentive using employee id",
            description = "this end point allows to fetch incentive data by using the employee id",
            parameters = {
                    @Parameter(name = "id", description = "Employee Id", required = true, in = ParameterIn.PATH)
            },
            responses = {
                    @ApiResponse(responseCode = "200", description = "Ok"),
                    @ApiResponse(responseCode = "400", description = "Bad Request"),
                    @ApiResponse(responseCode = "500", description = "Internal Server Error")
            }
    )
    public ResponseEntity<ApiResponseEntity<List<IncentiveDTO>>> getIncentiveById(@PathVariable int id)
            throws IncentiveNotFoundException {
        return ResponseEntity.ok(new ApiResponseEntity<>(
                HttpStatus.OK,
                "Incentive Fetched",
                incentiveService.getIncentiveById(id)
        ));
    }

    @GetMapping
    @Operation(
            summary = "gets all incentives",
            description = "this end point allows to fetch all incentive data",
            responses = {
                    @ApiResponse(responseCode = "200", description = "Ok"),
                    @ApiResponse(responseCode = "400", description = "Bad Request"),
                    @ApiResponse(responseCode = "500", description = "Internal Server Error")
            }
    )
    public ResponseEntity<ApiResponseEntity<List<IncentiveDTO>>> getAllIncentives() {
        return ResponseEntity.ok(new ApiResponseEntity<>(
                HttpStatus.OK,
                "Incentives Fetched",
                incentiveService.getAllIncentives()
        ));
    }

}
