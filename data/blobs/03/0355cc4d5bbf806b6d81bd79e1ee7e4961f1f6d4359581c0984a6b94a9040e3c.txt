package org.gro.texteditor.characters;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.shape.ArcType;
import org.gro.texteditor.Properties;

final class Numbers {
    static final double height = Properties.height,
                         width = Properties.width;

    private static GraphicsContext canvas;

    public static void draw(int character, GraphicsContext draw){
        canvas = draw;

        switch(character) {
            case '1':   one(); break; case '2':   two(); break; case '3': three(); break;
            case '4':  four(); break; case '5':  five(); break; case '6':   six(); break;
            case '7': seven(); break; case '8': eight(); break; case '9':  nine(); break;
            case '0':  zero(); break;
        }
    }

    private static void zero() {
        canvas.strokeArc(0.10 * width, 0.15 * height, 0.80 * width, 0.70 * height, 0, 360, ArcType.OPEN);
    }

    private static void one() {
        canvas.strokeLine(0.20 * width, 0.85 * height, 0.80 * width, 0.85 * height);
        canvas.strokeLine(0.50 * width, 0.15 * height, 0.50 * width, 0.85 * height);
        canvas.strokeLine(0.50 * width, 0.15 * height, 0.25 * width, 0.30 * height);
    }

    private static void two() {
        canvas.strokeLine(0.10 * width, 0.85 * height, 0.90 * width, 0.85 * height);
        canvas.strokeLine(0.10 * width, 0.85 * height, 0.81 * width, 0.44 * height);
        canvas.strokeArc (0.10 * width, 0.15 * height, 0.80 * width, 0.35 * height, 320, 220, ArcType.OPEN);
    }

    private static void three() {
        canvas.strokeArc(0.10 * width, 0.15 * height, 0.80 * width, 0.35 * height, 270, 230, ArcType.OPEN);
        canvas.strokeArc(0.10 * width, 0.50 * height, 0.80 * width, 0.35 * height, 210, 240, ArcType.OPEN);
    }

    private static void four() {
        canvas.strokeLine(0.70 * width, 0.15 * height, 0.70 * width, 0.85 * height);
        canvas.strokeLine(0.10 * width, 0.70 * height, 0.85 * width, 0.70 * height);
        canvas.strokeLine(0.10 * width, 0.70 * height, 0.70 * width, 0.15 * height);
    }

    private static void five() {
        canvas.strokeLine(0.10 * width, 0.15 * height, 0.90 * width, 0.15 * height);
        canvas.strokeLine(0.10 * width, 0.15 * height, 0.10 * width, 0.55 * height);
        canvas.strokeArc (0.10 * width, 0.30 * height, 0.80 * width, 0.55 * height, 220, 310, ArcType.OPEN);
    }

    private static void six() {
        canvas.strokeLine(0.12 * width, 0.58 * height, 0.66 * width, 0.15 * height);
        canvas.strokeArc (0.10 * width, 0.45 * height, 0.80 * width, 0.40 * height, 0, 360, ArcType.OPEN);
    }

    private static void seven() {
        canvas.strokeLine(0.20 * width, 0.85 * height, 0.90 * width, 0.15 * height);
        canvas.strokeLine(0.10 * width, 0.15 * height, 0.90 * width, 0.15 * height);
        canvas.strokeLine(0.10 * width, 0.15 * height, 0.10 * width, 0.25 * height);
    }

    private static void eight() {
        canvas.strokeArc(0.10 * width, 0.15 * height, 0.80 * width, 0.35 * height, 0, 360, ArcType.OPEN);
        canvas.strokeArc(0.10 * width, 0.50 * height, 0.80 * width, 0.35 * height, 0, 360, ArcType.OPEN);
    }

    private static void nine() {
        canvas.strokeArc (0.10 * width, 0.15 * height, 0.80 * width, 0.40 * height, 0, 360, ArcType.OPEN);
        canvas.strokeLine(0.30 * width, 0.85 * height, 0.87 * width, 0.43 * height);
    }
}