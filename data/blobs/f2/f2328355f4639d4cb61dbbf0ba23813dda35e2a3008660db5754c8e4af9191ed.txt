package com.example.hanghae4th.service.users;

import com.example.hanghae4th.domain.businesslogic.BadResponse;
import com.example.hanghae4th.domain.businesslogic.SuccessResponse;
import com.example.hanghae4th.domain.dto.ResponseBodyDto;
import com.example.hanghae4th.domain.dto.users.LoginRequestDto;
import com.example.hanghae4th.domain.dto.users.SignupRequestDto;
import com.example.hanghae4th.domain.jwt.JwtUtil;
import com.example.hanghae4th.domain.model.users.Users;
import com.example.hanghae4th.domain.repository.users.UsersRepository;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

@RequiredArgsConstructor
@Service
public class UsersService {
    private final UsersRepository usersRepository;
    private final SuccessResponse successResponse;
    private final BadResponse badResponse;
    private final JwtUtil jwtUtil;

    //회원 등록
    @Transactional
    public ResponseEntity<ResponseBodyDto> signup(SignupRequestDto signupRequestDto){
        Optional<Users> usersOptional = usersRepository.findByUsername(signupRequestDto.getUsername());

        //등록된 username이 없을 경우 회원가입 진행
        if(usersOptional.isEmpty()){
            usersRepository.save(signupRequestDto.toEntity());
            return successResponse.respondCreated();
        }

        //등록된 username 있을 경우 400, msg 반환
        return badResponse.respondBadRequest("이미 가입된 아이디입니다.");
    }

    //로그인
    @Transactional
    public ResponseEntity<ResponseBodyDto> login(LoginRequestDto loginRequestDto, HttpServletResponse response){
        String username = loginRequestDto.getUsername();
        String password = loginRequestDto.getPassword();

        // username 확인
        Users user = usersRepository.findByUsername(username).
                orElseThrow(() -> new IllegalArgumentException("회원 정보가 일치하지 않습니다.")
        );
        // 비밀번호 확인
        if(!user.getPassword().equals(password)){
            throw  new IllegalArgumentException("회원 정보가 일치하지 않습니다.");
        }

        //jwt 토큰 발급
        response.addHeader(JwtUtil.AUTHORIZATION_HEADER, jwtUtil.createToken(user.getUsername()));
        return successResponse.respondOK();
    }
}
