package com.koc.themeServer.theme.domain;

import com.koc.themeServer.theme.dto.ThemeLikeDto;
import com.koc.themeServer.theme.service.ThemeLikeService;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class ThemeLikeDomainService {
    private final ThemeLikeService themeLikeService;

    public ThemeLikeDto like(ThemeLikeDto dto) {
        ThemeLikeDto themeLikeDto = themeLikeService.findByUserIdAndThemeId(dto.getUserId(), dto.getThemeId())
                .map(ThemeLikeDto::switchLike)
                .orElse(dto);
        return themeLikeService.save(themeLikeDto);
    }
}
