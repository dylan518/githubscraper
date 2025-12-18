package com.aiia.Vinteum.user;

import com.aiia.Vinteum.IntegrationTestSupport;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class UserRepositoryTest extends IntegrationTestSupport {

    @Autowired
    UserRepository userRepository;

    @AfterEach
    void tearDown() {
        userRepository.deleteAllInBatch();
    }

    @DisplayName("같은 ID를 가진 회원이 있는 지 확인할 수 있다.")
    @Test
    void existsByName_green() {
        // given
        User user1 = User.of("id1", "pw1", "kim");
        User user2 = User.of("id2", "pw1", "jung");
        User user3 = User.of("id3", "pw1", "choi");
        userRepository.saveAll(List.of(user1, user2, user3));

        // when
        boolean result = userRepository.existsByName("kim");

        // then
        assertThat(result).isTrue();
    }

    @DisplayName("같은 ID를 가진 회원이 없는 지 확인할 수 있다.")
    @Test
    void existsByName_withNoDuplicateID(){
        // given

        // when
        boolean result = userRepository.existsByName("kim");

        // then
        assertThat(result).isFalse();
    }
}