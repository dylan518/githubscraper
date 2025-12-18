package com.pmm.budgetcalculator.expensing.service;

import com.pmm.budgetcalculator.expensing.entity.ExpenseType;
import com.pmm.budgetcalculator.expensing.entity.dto.ExpenseTypeDto;
import com.pmm.budgetcalculator.expensing.entity.mapper.ExpenseTypeMapper;
import com.pmm.budgetcalculator.expensing.exeption.EntityNotFoundException;
import com.pmm.budgetcalculator.expensing.repository.ExpenseTypeRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class ExpenseTypeService {


    private final ExpenseTypeRepository expenseTypeRepository;
    private final ExpenseTypeMapper expenseTypeMapper;

    public List<ExpenseTypeDto> getAllExpenseTypes() {
        return expenseTypeRepository
                .findAll()
                .stream()
                .map(expenseType -> expenseTypeMapper.entityToDto(expenseType))
                .collect(Collectors.toList());
    }

    public ExpenseTypeDto getExpenseTypeById(Long id) {
        return expenseTypeRepository
                .findById(id)
                .map(expenseType -> expenseTypeMapper.entityToDto(expenseType))
                .orElseThrow(() -> new EntityNotFoundException(id));
    }

    public ExpenseTypeDto createExpenseType(ExpenseTypeDto expenseTypeDto) {
        ExpenseType expenseType = expenseTypeMapper.dtoToEntity(expenseTypeDto);
        ExpenseType savedExpenseType = expenseTypeRepository.save(expenseType);
        return expenseTypeMapper.entityToDto(savedExpenseType);
    }

    public void removeExpenseTypeById(Long id) {
        if (expenseTypeRepository.existsById(id)) {
            expenseTypeRepository.deleteById(id);
        }
        else {
            throw new EntityNotFoundException(id);
        }
    }

    public ExpenseTypeDto updateExpenseType(Long id, ExpenseTypeDto expenseTypeDetailsDto) {
        if (expenseTypeRepository.existsById(id)) {
            ExpenseType expenseType = expenseTypeMapper.dtoToEntity(expenseTypeDetailsDto);
            ExpenseType updateExpenseType = expenseTypeRepository.getExpenseTypeById(id);
            updateExpenseType.setExpenseTypeName(expenseTypeDetailsDto.getExpenseTypeName());
            ExpenseType updatedExpenseType = expenseTypeRepository.save(updateExpenseType);
            return expenseTypeMapper.entityToDto(updatedExpenseType);
        }
        else {
            throw new EntityNotFoundException(id);
        }
    }

    public List<ExpenseTypeDto> findByCriteria(String expenseTypeName) {
        if (Objects.nonNull(expenseTypeName)) {
            return expenseTypeRepository
                    .findByExpenseTypeName(expenseTypeName)
                    .stream()
                    .map(expenseType -> expenseTypeMapper.entityToDto(expenseType))
                    .collect(Collectors.toList());
        } else {
            throw new RuntimeException("ExpenseTypeName is incorrect");
        }
    }
}

