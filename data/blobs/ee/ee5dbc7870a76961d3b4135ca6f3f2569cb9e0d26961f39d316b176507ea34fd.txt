package com.keyin.rest.TakeOff;

import com.keyin.rest.AirCraft.AirCraft;
import com.keyin.rest.Airport.AirPort;
import com.keyin.rest.Airport.AirPortService;
import com.keyin.rest.City.City;
import com.keyin.rest.City.CityRepository;
import com.keyin.rest.City.CityService;
import com.keyin.rest.Gate.Gate;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;

import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class TakeOffServiceTest {

    @Mock
    private TakeOffRepository takeOffRepository;
    @InjectMocks
    private TakeOffService takeOffService;



    private AirPortService airPortService;
    @Test
    public void testGetAllTakeOff(){
        City stJohnsCity =  new City(1,"St John's","States", 2000);

        AirPort airport = new AirPort(1,"St John's", "YYH",stJohnsCity);
        AirCraft boeing = new AirCraft(1, "Boeing 757", "Pal", 130);
        Gate gate = new Gate (1, "gate A");
        Date date = new Date();

        TakeOff takeOff = new TakeOff(1, airport,date, boeing, gate);

        List<TakeOff> takeOffs = new ArrayList<TakeOff>();

        when(takeOffRepository.findAll()).thenReturn(takeOffs);



        List<TakeOff> takeOffResponse = takeOffService.getAllTakeOff();

        Assertions.assertNotNull(takeOffResponse);

    }

    @Test
    public void testTakeOffByID(){
        City stJohnsCity =  new City(1,"St John's","States", 2000);

        AirPort airport = new AirPort(1,"St John's", "YYH",stJohnsCity);
        AirCraft boeing = new AirCraft(1, "Boeing 757", "Pal", 130);
        Gate gate = new Gate (1, "gate A");
        Date date = new Date();

        TakeOff takeOff = new TakeOff(1, airport,date, boeing, gate);

        List<TakeOff> takeOffs = new ArrayList<TakeOff>();

        when(takeOffRepository.findById(Long.valueOf(1))).thenReturn(Optional.of(takeOff));

        TakeOff takeOffResponse = takeOffService.getTakeOffById(1);

        Assertions.assertNotNull(takeOffResponse);

    }


}
