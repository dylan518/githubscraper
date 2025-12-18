package ru.lukyanov.service;

import lombok.AccessLevel;
import lombok.Data;
import lombok.experimental.FieldDefaults;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Qualifier;
import ru.lukyanov.entity.music.Music;
import ru.lukyanov.entity.music.MusicInstrument;

@Data
@Slf4j
@FieldDefaults(level = AccessLevel.PRIVATE)
public class MusicPlayer {
    String name;
    int volume;
    Music music1;
    Music music2;

    public MusicPlayer(Music music1, @Qualifier("rockMusic") Music music2) {
        this.music1 = music1;
        this.music2 = music2;
    }

    public void setMusic1(Music music1) {
        this.music1 = music1;
    }

    public void setMusic2(Music music2) {
        this.music2 = music2;
    }

    public void playMusic(MusicInstrument musicInstrument) {
        switch (musicInstrument) {
            case PIANO -> log.info("Playing: {}", music1.getSong());
            case GUITAR -> log.info("Playing: {}",music2.getSong());
        }


    }
}
