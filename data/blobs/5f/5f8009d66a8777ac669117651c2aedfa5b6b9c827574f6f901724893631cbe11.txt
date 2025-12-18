package jandbuser.api.controller;

import jandbuser.api.dto.UserInfoDto;
import jandbuser.api.service.UserService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * 사용자 controller
 *
 * <pre>
 * 코드 히스토리 (필요시 변경사항 기록)
 * </pre>
 *
 * @author JandB
 * @since 1.0
 */
@Slf4j
@RestController
@RequiredArgsConstructor
@RequestMapping("/")
public class UserController {

    private final UserService userService;

    /**
     * test
     * @return String
     */
    @GetMapping("/test")
    public String getTestUser(){
        log.debug("##############################################");
        log.debug("test :: getTestBoard() :: {}","hi");
        log.debug("##############################################");
        return userService.getTestUser();
    }

    /**
     * 사용자 목록 조회
     * @return 사용자목록
     */
    @GetMapping("/list")
    public List<UserInfoDto> getUserList(){
        List<UserInfoDto> list = userService.getUserList();

        log.debug("################################################");
        list.forEach(dto -> log.debug(dto.getUserId()));
        log.debug("################################################");

        return list;
    }

    /**
     * 사용자정보 저장
     * @param userInfoDto 사용자정보DTO
     */
    @PostMapping("/save")
    public void saveUser(@RequestBody UserInfoDto userInfoDto){
        userService.saveUser(userInfoDto);
    }
}
