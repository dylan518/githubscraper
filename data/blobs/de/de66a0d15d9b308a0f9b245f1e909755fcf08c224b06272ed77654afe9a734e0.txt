package Structural.Flyweight;

import java.util.List;

public class Forest {

    private List<Tree> trees;

    public void plantTree(double x, double y, String name, String color, String texture) {
        TreeType type = TreeFactory.getTreeType(name, color, texture);
        Tree tree = new Tree(x, y, type);
        trees.add(tree);
    }

    public void draw(String canvas) {
        for (Tree tree : trees) {
            tree.draw(canvas);
        }
    }
}
