import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

    private static final int ROWS = 10;
    private static final int COLUMNS = 10;
    private static final int TITLE_SIZE = 580;

    public static void main(String[] args) {
        generateRandomTitleMap();
    }

    private static void generateRandomTitleMap() {
        ArrayList<Title> titles = createTitles();
        Title[][] outputList = new Title[ROWS][COLUMNS];

        for (int x = 0; x < ROWS; x++) {
            for (int y = 0; y < COLUMNS; y++) {
                if (x == 0 && y == 0) {
                    outputList[x][y] = createFirstTitle(titles);
                } else {
                    ArrayList<Title> titlesCopy = new ArrayList<>(titles);
                    outputList[x][y] = findGoodTitle(titlesCopy, outputList, x, y);
                }
            }
        }

        generateTitleMap(outputList);
    }

    private static Title findGoodTitle(ArrayList<Title> titles, Title[][] outputList, int row, int col) {
        while (!titles.isEmpty()) {
            int index = (int) (Math.random() * titles.size());
            Title title = titles.get(index);

            if (row == 0 && title.checkLeft(outputList[0][col - 1])) {
                return title;
            } else if (col == 0 && title.checkTop(outputList[row - 1][0])) {
                return title;
            } else if (col != 0 && row != 0 && title.checkLeft(outputList[row][col - 1]) && title.checkTop(outputList[row - 1][col])) {
                return title;
            }

            titles.remove(index);
        }
        return new Title(5, 0, 0, 0, 0);
    }

    private static Title createFirstTitle(ArrayList<Title> list) {
        int randomTitle = (int) (Math.random() * 5);
        return list.get(randomTitle);
    }

    private static void generateTitleMap(Title[][] outputList) {
        try {
            BufferedImage result = new BufferedImage(COLUMNS * TITLE_SIZE, ROWS * TITLE_SIZE, BufferedImage.TYPE_INT_RGB);
            Graphics2D g = result.createGraphics();

            for (int x = 0; x < ROWS; x++) {
                for (int y = 0; y < COLUMNS; y++) {
                    BufferedImage tile = ImageIO.read(new File("images/image_" + outputList[x][y].index + ".PNG"));
                    g.drawImage(tile, y * TITLE_SIZE, x * TITLE_SIZE, null);
                }
            }

            g.dispose();
            ImageIO.write(result, "jpg", new File("outputImage/op.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static ArrayList<Title> createTitles() {
        ArrayList<Title> list = new ArrayList<>();
        list.add(new Title(0, 1, 1, 1, 1));
        list.add(new Title(1, 0, 0, 1, 0));
        list.add(new Title(2, 0, 1, 1, 0));
        list.add(new Title(3, 1, 1, 0, 0));
        list.add(new Title(4, 1, 0, 0, 1));
        return list;
    }
}