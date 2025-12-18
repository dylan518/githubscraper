package ru.pazik98.ZuzexTestTask.service.impl;

import org.springframework.stereotype.Service;
import ru.pazik98.ZuzexTestTask.entity.RegistrationEntity;
import ru.pazik98.ZuzexTestTask.repository.RegistrationRepository;
import ru.pazik98.ZuzexTestTask.service.RegistrationService;

import java.util.List;
import java.util.Optional;

@Service
public class RegistrationServiceImpl implements RegistrationService {
    
    private final RegistrationRepository registrationRepository;

    public RegistrationServiceImpl(RegistrationRepository registrationRepository) {
        this.registrationRepository = registrationRepository;
    }

    @Override
    public List<RegistrationEntity> getAll() {
        return registrationRepository.findAll();
    }

    @Override
    public Optional<RegistrationEntity> getById(Long id) {
        return registrationRepository.findById(id);
    }

    @Override
    public RegistrationEntity save(RegistrationEntity RegistrationEntity) {
        return registrationRepository.save(RegistrationEntity);
    }

    @Override
    public RegistrationEntity update(RegistrationEntity RegistrationEntity) {
        return registrationRepository.save(RegistrationEntity);
    }

    @Override
    public void delete(Long id) {
        registrationRepository.deleteById(id);
    }
}
