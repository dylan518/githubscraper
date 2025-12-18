package br.com.likwi.arquiteturahexagonal.adapters.handle.pessoaListar;


import br.com.likwi.arquiteturahexagonal.adapters.outbound.persistence.PessoaJpaRepository;
import br.com.likwi.arquiteturahexagonal.core.domain.PageManual;
import br.com.likwi.arquiteturahexagonal.core.domain.PessoaDomain;
import br.com.likwi.arquiteturahexagonal.core.ports.PessoaListarServicePort;
import org.modelmapper.ModelMapper;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service("M")
public class PessoaListarMasculinoHandle implements PessoaListarServicePort {

    private final PessoaJpaRepository pessoaJPARepository;

    private final ModelMapper moodelMapper;

    public PessoaListarMasculinoHandle(ModelMapper modelMapper, PessoaJpaRepository pessoaJPARepository) {
        this.moodelMapper = modelMapper;
        this.pessoaJPARepository = pessoaJPARepository;
    }


    @Override
    public List<PessoaDomain> listar(String tipo, String nome, PageManual pageManual) {
        Pageable pageable = PageRequest.of(pageManual.getPageNumber(), pageManual.getPageSize());

        return this.pessoaJPARepository.findMale(nome,pageable)
                .stream()
                .map(entity -> this.moodelMapper.map(entity, PessoaDomain.class))
                .collect(Collectors.toList());

    }
}
