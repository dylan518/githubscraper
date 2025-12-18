package com.jeju.main.api.reservation.service;

import com.jeju.main.domain.guesthouse.domain.GuestHouse;
import com.jeju.main.domain.guesthouse.repository.GuestHouseRepository;
import com.jeju.main.domain.user.domain.User;
import com.jeju.main.domain.user.repository.UserRepository;
import com.jeju.main.global.exception.EntityNotFoundException;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import static com.jeju.main.global.error.ErrorCode.GUESTHOUSE_NOT_FOUND;
import static com.jeju.main.global.error.ErrorCode.USER_NOT_FOUND;

@Service
@RequiredArgsConstructor
public class ReservationService {
    private final UserRepository userRepository;
    private final GuestHouseRepository guestHouseRepository;
    public void reservation(Long userId, Long guestHouseId){
        User user = findUserByUserId(userId);
        GuestHouse guestHouse = findGuestHouseByGuestHouseId(guestHouseId);
        userReservation(user, guestHouse);
    }
    private void userReservation(User user, GuestHouse guestHouse){

    }
    private User findUserByUserId(Long userId){
        return userRepository.findById(userId).orElseThrow(()-> new EntityNotFoundException(USER_NOT_FOUND));
    }
    private GuestHouse findGuestHouseByGuestHouseId(Long guestHouseId){
        return guestHouseRepository.findById(guestHouseId).orElseThrow(()->new EntityNotFoundException(GUESTHOUSE_NOT_FOUND));
    }
}
