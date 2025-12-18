package com.carshop.app.adapter.persistence.brand.adapter;

import com.carshop.app.adapter.persistence.brand.repository.BrandRepository;
import com.carshop.app.adapter.persistence.brand.mapper.BrandJpaMapper;
import com.carshop.app.application.port.persistence.brand.BrandPublicRepositoryPort;
import com.carshop.app.domain.Brand;
import com.carshop.app.infrastructure.annotation.Adapter;

import java.util.Collection;
import java.util.stream.Collectors;

@Adapter
public class BrandPublicRepositoryAdapter implements BrandPublicRepositoryPort {

    private final BrandRepository brandRepository;
    private final BrandJpaMapper brandJpaMapper;

    public BrandPublicRepositoryAdapter(final BrandRepository brandRepository, final BrandJpaMapper brandJpaMapper) {
        this.brandRepository = brandRepository;
        this.brandJpaMapper = brandJpaMapper;
    }

    @Override
    public Collection<Brand> findUniversal() {
        return this.brandRepository
                .findUniversal()
                .stream()
                .map(this.brandJpaMapper::toDomain)
                .collect(Collectors.toList());
    }
}
