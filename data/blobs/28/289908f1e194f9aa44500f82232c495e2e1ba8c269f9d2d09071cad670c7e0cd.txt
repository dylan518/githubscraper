package com.javarush.task.task35.task3513;

public class MoveEfficiency implements Comparable<MoveEfficiency> {
    private int numberOfEmptyTiles;
    private int score;
    private Move move;

    public MoveEfficiency(int numberOfEmptyTiles, int score, Move move) {
        this.numberOfEmptyTiles = numberOfEmptyTiles;
        this.score = score;
        this.move = move;
    }

    public Move getMove() {
        return move;
    }

    @Override
    public int compareTo(MoveEfficiency o) {
        int numberOfEmptyTilesDifference = this.numberOfEmptyTiles - o.numberOfEmptyTiles;
        if (numberOfEmptyTilesDifference != 0) {
            return numberOfEmptyTilesDifference > 0 ? 1 : -1;
        }

        int scoreDifference = this.score - o.score;
        if (scoreDifference != 0) {
            return scoreDifference > 0 ? 1 : -1;
        }
        else return 0;

    }
}
