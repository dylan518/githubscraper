package org.example.structural.facade.hometheatre;

public class HomeTheatreFacade {
    Amplifier amp;
    Tuner tuner;
    StreamingPlayer streaming;
    CdPlayer cd;
    Projector projector;
    TheaterLights lights;
    Screen screen;
    PopcornPopper popper;

    public HomeTheatreFacade(Amplifier amp, Tuner tuner,
                             StreamingPlayer streaming, CdPlayer cd,
                             Projector projector, TheaterLights lights,
                             Screen screen, PopcornPopper popper) {
        this.amp = amp;
        this.tuner = tuner;
        this.streaming = streaming;
        this.cd = cd;
        this.projector = projector;
        this.lights = lights;
        this.screen = screen;
        this.popper = popper;
    }

    public void watchMovie(String movie) {
        System.out.println("Get ready to watch a movie...");
        popper.on();
        popper.pop();
        lights.dim(10);
        screen.down();
        projector.on();
        projector.wideScreenMode();
        amp.on();
        amp.setStreamingPlayer(streaming);
        amp.setVolume(5);
        streaming.on();
        streaming.play(movie);
    }

    public void endMovie() {
        System.out.println("Shutting movie theater down...");
        popper.off();
        lights.on();
        screen.up();
        projector.off();
        amp.off();
        streaming.stop();
        streaming.off();
    }
}
