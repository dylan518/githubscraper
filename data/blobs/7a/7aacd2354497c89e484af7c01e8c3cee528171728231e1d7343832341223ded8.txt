package Structural.AdapterPattern;

// Client Code
public class AdapterPatternExample {
    public static void main(String[] args) {
        MediaPlayer mp3Player = new Mp3Player();
        mp3Player.play("mp3", "song.mp3"); // Output: Playing MP3 file. Name: song.mp3

        MediaPlayer vlcPlayer = new MediaAdapter();
        vlcPlayer.play("vlc", "movie.vlc"); // Output: Playing VLC file. Name: movie.vlc

        // Trying to play an unsupported format
        mp3Player.play("vlc", "movie.vlc"); // Output: Invalid media type: vlc
        vlcPlayer.play("mp3", "song.mp3"); // Output: Invalid media type: mp3
    }
}
