public class Circle {
    Point center;
    double radius;

    public Circle(Point center, double radius) {
        this.center = center;
        this.radius = radius;
    }



    public boolean pointInsideCircle(Point p) {
        /*int x1 = center.x;
        int y1 = center.y;
        int x2 = p.x;
        int y2 = p.y;*/
        //double dis=center.distance(p);
        double dis = p.distance(center);
        //double distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        if (dis <= radius) {
            return true;
        }
        else
            return false;
    }


    public boolean circleInsideCircle(Circle C) {
        double dis=center.distance(C.center);
        if(dis+C.radius<=this.radius) return true;
        else return false;
    }
}
