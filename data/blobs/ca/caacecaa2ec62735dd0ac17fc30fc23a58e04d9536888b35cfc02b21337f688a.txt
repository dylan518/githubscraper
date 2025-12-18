package co.ars.gw.service.mapper;

import co.ars.gw.domain.Author;
import co.ars.gw.service.dto.AuthorDTO;
import java.util.ArrayList;
import java.util.List;
import javax.annotation.processing.Generated;
import org.springframework.stereotype.Component;

@Generated(
    value = "org.mapstruct.ap.MappingProcessor",
    date = "2022-06-16T11:58:12+0300",
    comments = "version: 1.4.2.Final, compiler: Eclipse JDT (IDE) 1.4.100.v20220318-0906, environment: Java 17.0.3 (Eclipse Adoptium)"
)
@Component
public class AuthorMapperImpl implements AuthorMapper {

    @Override
    public Author toEntity(AuthorDTO dto) {
        if ( dto == null ) {
            return null;
        }

        Author author = new Author();

        author.setId( dto.getId() );
        author.setName( dto.getName() );
        author.setBirthDate( dto.getBirthDate() );

        return author;
    }

    @Override
    public AuthorDTO toDto(Author entity) {
        if ( entity == null ) {
            return null;
        }

        AuthorDTO authorDTO = new AuthorDTO();

        authorDTO.setId( entity.getId() );
        authorDTO.setName( entity.getName() );
        authorDTO.setBirthDate( entity.getBirthDate() );

        return authorDTO;
    }

    @Override
    public List<Author> toEntity(List<AuthorDTO> dtoList) {
        if ( dtoList == null ) {
            return null;
        }

        List<Author> list = new ArrayList<Author>( dtoList.size() );
        for ( AuthorDTO authorDTO : dtoList ) {
            list.add( toEntity( authorDTO ) );
        }

        return list;
    }

    @Override
    public List<AuthorDTO> toDto(List<Author> entityList) {
        if ( entityList == null ) {
            return null;
        }

        List<AuthorDTO> list = new ArrayList<AuthorDTO>( entityList.size() );
        for ( Author author : entityList ) {
            list.add( toDto( author ) );
        }

        return list;
    }

    @Override
    public void partialUpdate(Author entity, AuthorDTO dto) {
        if ( dto == null ) {
            return;
        }

        if ( dto.getId() != null ) {
            entity.setId( dto.getId() );
        }
        if ( dto.getName() != null ) {
            entity.setName( dto.getName() );
        }
        if ( dto.getBirthDate() != null ) {
            entity.setBirthDate( dto.getBirthDate() );
        }
    }
}
