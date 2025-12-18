package taskCarProject.characteristics.enums;

import taskCarProject.interfaces.WheelSizeInter;

public enum WheelSizeBmw implements WheelSizeInter {
    SIZE14(14), SIZE19(19);
    private int sizeValue;

    WheelSizeBmw(int sizeValue) {
        this.sizeValue = sizeValue;
    }

    public int getSizeValue() {
        return sizeValue;
    }
}
