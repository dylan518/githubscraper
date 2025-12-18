package com.task.inquireapplication.service.implement;

import com.task.forecastdomain.entity.ForecastEntity;
import com.task.forecastdomain.repository.ForecastRepository;
import com.task.inquireapplication.dto.response.GetForecastListResponseDto;
import com.task.inquireapplication.dto.response.common.ResponseDto;
import com.task.inquireapplication.service.InquireService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class InquireServiceImpl implements InquireService {

    private final ForecastRepository forecastRepository;
    @Override
    public ResponseEntity<? super GetForecastListResponseDto> getForecastList() {

        List<ForecastEntity> entities = new ArrayList<>();

        try {
            entities = forecastRepository.findAll();
            if(entities.isEmpty()) return GetForecastListResponseDto.noContent();

        }catch (Exception exception){
            exception.printStackTrace();
            return ResponseDto.databaseError();
        }
        return GetForecastListResponseDto.success(entities);
    }
}
