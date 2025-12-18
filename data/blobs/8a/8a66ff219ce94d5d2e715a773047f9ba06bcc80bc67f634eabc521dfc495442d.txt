package tests;

import core.BaseTest;
import org.junit.Assert;
import org.junit.Test;
import screen.DragNDropScreen;
import screen.MenuScreen;

public class DragNDropTest extends BaseTest {

    private final MenuScreen menuScreen = new MenuScreen();
    private final DragNDropScreen dragNDropScreen = new DragNDropScreen();

    private final String[] initStatus = new String[]{"Esta", "é uma lista", "Drag em Drop!", "Faça um clique longo,",
            "e arraste para", "qualquer local desejado."};
    private final String[] intermediaryStatus = new String[]{"é uma lista", "Drag em Drop!", "Faça um clique longo,",
            "e arraste para", "Esta", "qualquer local desejado."};
    private final String[] finalStatus = new String[]{"Faça um clique longo,", "é uma lista", "Drag em Drop!",
            "e arraste para", "Esta", "qualquer local desejado."};

    @Test
    public void shouldInteractDragNDrop() {
        menuScreen.clickDragNDropMenu();

        Assert.assertArrayEquals(initStatus, dragNDropScreen.getList());

        dragNDropScreen.dragNDropThisToDragTo();

        Assert.assertArrayEquals(intermediaryStatus, dragNDropScreen.getList());

        dragNDropScreen.dragNDropDoingLongClickToThisIsList();

        Assert.assertArrayEquals(finalStatus, dragNDropScreen.getList());
    }
}
