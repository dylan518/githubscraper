package com.pratikkroy.designpatterns.structural.adapterPattern.incompatibleProduct;

public class SquarePeg {
    private int length;

    public SquarePeg(final int length) {
        this.length = length;
    }

    public int getLength() {
        return length;
    }

    public void setLength(final int length) {
        this.length = length;
    }
}
