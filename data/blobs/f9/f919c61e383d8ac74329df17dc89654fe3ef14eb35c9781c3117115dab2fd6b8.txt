package Points;

import java.util.Arrays;

public class Point3d extends Point2d {
    private float z = 0.0f;

    Point3d() {
    }

    Point3d(float x, float y, float z) {
        super(x, y);
        this.z = z;
    }

    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
    }

    public void setXYZ(float x, float y, float z) {
        super.setX(x);
        super.setY(y);
        this.z = z;
    }

    public float[] getXYZ() {
        return new float[]{super.getX(), super.getY(), this.getZ()};
    }

    @Override
    public String toString() {
        return "Point3d{" +
                "x=" + super.getX() +
                ", y=" + this.getY() +
                ", z=" + this.getZ() +
                ", (x,y,z)=" + Arrays.toString(this.getXYZ()) +
                '}';
    }
}
