package com.example.labsproject.laba3;

public class Matrix {
    private float[][] data;
    private int rows;
    private int cols;
    private int state;

    public Matrix() {
        this.rows = 1;
        this.cols = 1;
        this.state = 0;
        this.data = new float[rows][cols];
        this.data[0][0] = 0;
    }

    public Matrix(int size) {
        this.rows = size;
        this.cols = size;
        this.state = 0;
        this.data = new float[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                this.data[i][j] = i + j;
            }
        }
    }

    public Matrix(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
        this.state = 0;
        this.data = new float[rows][cols];
    }

    public float get(int row, int col) {
        if (row < 0 || row >= rows || col < 0 || col >= cols) {
            this.state = 2;
            return 0;
        }
        return this.data[row][col];
    }

    public void set(int row, int col, float value) {
        if (row < 0 || row >= rows || col < 0 || col >= cols) {
            this.state = 2;
        } else {
            this.data[row][col] = value;
            this.state = 0;
        }
    }

    public void print() {
        if (state != 0) {
            System.out.println("Ошибка состояния: " + state);
            return;
        }
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(data[i][j] + " ");
            }
            System.out.println();
        }
    }

    public Matrix add(Matrix other) {
        if (this.rows != other.rows || this.cols != other.cols) {
            this.state = 3;
            return null;
        }
        Matrix result = new Matrix(rows, cols);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result.data[i][j] = this.data[i][j] + other.data[i][j];
            }
        }
        return result;
    }

    public Matrix subtract(Matrix other) {
        if (this.rows != other.rows || this.cols != other.cols) {
            this.state = 3;
            return null;
        }
        Matrix result = new Matrix(rows, cols);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result.data[i][j] = this.data[i][j] - other.data[i][j];
            }
        }
        return result;
    }

    public Matrix multiply(Matrix other) {
        if (this.cols != other.rows) {
            this.state = 3;
            return null;
        }
        Matrix result = new Matrix(this.rows, other.cols);
        for (int i = 0; i < this.rows; i++) {
            for (int j = 0; j < other.cols; j++) {
                result.data[i][j] = 0;
                for (int k = 0; k < this.cols; k++) {
                    result.data[i][j] += this.data[i][k] * other.data[k][j];
                }
            }
        }
        return result;
    }
}

