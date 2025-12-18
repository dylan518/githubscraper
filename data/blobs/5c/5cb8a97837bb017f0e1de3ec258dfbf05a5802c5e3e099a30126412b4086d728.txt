package org.boyerfamily.sudoku;

import java.util.BitSet;
import java.util.Iterator;
import java.util.List;

public class Board {
    public static final int BOARD_SIZE = 9;
    private static final String DIVIDER = "------+-------+------\n";
    private final Cell[][] cells = new Cell[BOARD_SIZE][BOARD_SIZE];
    private final BitSet[] rows = new BitSet[BOARD_SIZE];
    private final BitSet[] columns = new BitSet[BOARD_SIZE];
    private final BitSet[] grids = new BitSet[BOARD_SIZE];
    private int passCount = 0;

    public Board() {
        for (int i = 0; i < BOARD_SIZE; i++) {
            rows[i] = new BitSet(BOARD_SIZE);
            columns[i] = new BitSet(BOARD_SIZE);
            grids[i] = new BitSet(BOARD_SIZE);
        }

        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                cells[i][j] = new Cell(rows[i], columns[j], grids[getGridIndex(i, j)], i, j);
            }
        }
    }

    public Board(List<Integer> startValues) {
        this();

        Iterator<Integer> iter = startValues.listIterator();
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                cells[i][j].setValue(Value.fromInt(iter.next()));
            }
        }
    }

    static int getGridIndex(int row, int column) {
        int index = 0;

        switch (row) {
            case 3, 4, 5 -> index += 3;
            case 6, 7, 8 -> index += 6;
        }

        switch (column) {
            case 3, 4, 5 -> index += 1;
            case 6, 7, 8 -> index += 2;
        }

        return index;
    }

    public Cell getCell(int row, int column) {
        return cells[row][column];
    }

    public Value getCellValue(int row, int column) {
        return cells[row][column].getValue();
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                Value value = cells[i][j].getValue();

                stringBuilder.append(value != null ? value : '0');
                stringBuilder.append(' ');
                if (j == 2 || j == 5) {
                    stringBuilder.append("| ");
                }
            }

            stringBuilder.append('\n');
            if (i == 2 || i == 5) {
                stringBuilder.append(DIVIDER);
            }
        }

        stringBuilder.append('\n');
        return stringBuilder.toString();
    }

    public boolean isSolved() {
        return bitsetsFull(rows) && bitsetsFull(columns) && bitsetsFull(grids);
    }

    public boolean scanForSolvedCells() {
        boolean changed = false;

//        System.out.println("Starting scan number: " + passCount++ + " ...");
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                if (cells[i][j].getValue() == null) {
                    if (isCellSolved(cells[i][j])) {
                        changed = true;
                    }
                }
            }
        }

        return changed;
    }

    private boolean isCellSolved(Cell cell) {
        BitSet possibles = new BitSet(BOARD_SIZE);
        possibles.set(0, BOARD_SIZE);

        // exclude all bits that already exist in row, column, or grid
        possibles.andNot(cell.getRowValues());
        possibles.andNot(cell.getColumnValues());
        possibles.andNot(cell.getGridValues());

        if (possibles.cardinality() == 1) {
//            System.out.println(String.format("Found single value  %s at (%d, %d)",
//                    possibles.nextSetBit(0)+1, cell.getRow()+1, cell.getColumn()+1));
            cell.setValue(possibles.nextSetBit(0) + 1);
            return true;
        }

        int nextIndex = 0;
        for (int i = 0; i < possibles.cardinality(); i++) {
            nextIndex = possibles.nextSetBit(nextIndex);
            if (isOnlyValidValue(cell, nextIndex)) {
//                System.out.println(String.format("Found only valid value  %s at (%d, %d)",
//                        nextIndex+1, cell.getRow()+1, cell.getColumn()+1));
                cell.setValue(nextIndex + 1);
                return true;
            }
        }
        return false;
    }

    boolean isOnlyValidValue(Cell cell, int index) {
        int row1 = -1, row2 = -1;
        int col1 = -1, col2 = -1;
        int rowNum = cell.getRow();
        int columnNum = cell.getColumn();

        if (cell.getRowValues().get(index) || cell.getColumnValues().get(index)) {
            return false;
        }

        switch (columnNum) {
            case 0, 3, 6 -> {
                col1 = columnNum + 1;
                col2 = columnNum + 2;
            }
            case 1, 4, 7 -> {
                col1 = columnNum - 1;
                col2 = columnNum + 1;
            }
            case 2, 5, 8 -> {
                col1 = columnNum - 2;
                col2 = columnNum - 1;
            }
        }

        switch (rowNum) {
            case 0, 3, 6 -> {
                row1 = rowNum + 1;
                row2 = rowNum + 2;
            }
            case 1, 4, 7 -> {
                row1 = rowNum + 1;
                row2 = rowNum - 1;
            }
            case 2, 5, 8 -> {
                row1 = rowNum - 2;
                row2 = rowNum - 1;
            }
        }

        boolean rowMatch = (rows[row1].get(index) || (cells[row1][columnNum].getValue() != null)) &&
                (rows[row2].get(index) || (cells[row2][columnNum].getValue() != null));
        boolean columnMatch = (columns[col1].get(index) || (cells[rowNum][col1].getValue() != null)) &&
                (columns[col2].get(index) || (cells[rowNum][col2].getValue() != null));

        if ((cells[row1][columnNum].getValue() != null) && (cells[row2][columnNum].getValue() != null)) {
            rowMatch = false;
        }

        if ((cells[rowNum][col1].getValue() != null) && (cells[rowNum][col2].getValue() != null)) {
            columnMatch = false;
        }

        return rowMatch && columnMatch;
    }

    private boolean bitsetsFull(BitSet[] bitSets) {
        for (BitSet bitSet : bitSets) {
            if (bitSet.cardinality() < BOARD_SIZE) {
                return false;
            }
        }

        return true;
    }
}
