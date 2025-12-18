package com.challenge.meli.trilateracion.api.services.dto;

import com.challenge.meli.trilateracion.api.model.domain.Satellite;
import com.challenge.meli.trilateracion.api.repositories.SatelliteRepository;
import org.springframework.stereotype.Service;

@Service
public class SatelliteDtoServiceImpl implements SatelliteDtoService {

    private final SatelliteRepository satelliteRepository;

    public SatelliteDtoServiceImpl(SatelliteRepository satelliteRepository) {
        this.satelliteRepository = satelliteRepository;
    }

    @Override
    public Satellite save(Satellite satelliteP) {
        Satellite satellite = satelliteRepository.getByName(satelliteP.getName());

        if (satellite == null) {
            satellite = satelliteRepository.save(satelliteP);
        }

        return satellite;
    }
}
