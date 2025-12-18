package edu.school21.printer.logic;

import java.awt.Color;
import java.awt.image.BufferedImage;

public class Logic {
    private static final int W = 1;
    private static final int B = 0;

    BufferedImage bufferedImage;

    public Logic(BufferedImage bufferedImage) {
        this.bufferedImage = bufferedImage;
    }

    public int[][] takeArrayFromImage()
    {
        int [][] arrayPoints = new int[bufferedImage.getHeight()][bufferedImage.getWidth()];

        for (int y = 0; y < bufferedImage.getHeight(); y++) {
            for (int x = 0; x < bufferedImage.getWidth(); x++) {
                if (bufferedImage.getRGB(x, y) == Color.WHITE.getRGB()) {
                    arrayPoints[y][x] = W;
                } else {
                    arrayPoints[y][x] = B;
                }
            }
        }
        return arrayPoints;
    }
}
