package com.example.helloworld.service.member;

import com.example.helloworld.dto.member.TokenDTO;
import com.example.helloworld.entity.member.TokenEntity;
import com.example.helloworld.jwt.JwtProvider;
import com.example.helloworld.repository.member.MemberRepository;
import com.example.helloworld.repository.member.TokenRepository;
import com.example.helloworld.transform.member.MemberTransform;
import com.example.helloworld.transform.member.TokenTransform;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.stereotype.Service;

@Log4j2
@Service
@RequiredArgsConstructor
public class TokenService {

    private final TokenRepository tokenRepository;
    private final TokenTransform tokenTransform;

    public TokenDTO saveRefreshToken(String email, String token) {
        TokenEntity tokenEntity = TokenEntity.builder().email(email).refreshToken(token).build();
        return tokenTransform.toDTO(tokenRepository.save(tokenEntity));
    }
    public TokenDTO saveRefreshToken(TokenDTO tokenDTO) {
        return tokenTransform.toDTO(tokenRepository.save(tokenTransform.toEntity(tokenDTO)));
    }
    public String getToken(String email) {
        TokenEntity tokenEntity = tokenRepository.findById(email).orElse(null);
        if(tokenEntity != null)
            return tokenEntity.getRefreshToken();
        return null;
    }
}
