import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.InstanceOfAssertFactories.LIST;

public class Client {


    List<Shape> shapes;
    List<Shape> shapesCopy;
    @Before
    public  void init(){
        shapes=new ArrayList<>();
        shapesCopy=new ArrayList<>();
        Circle c1=new Circle(10,20,"red",15);
        shapes.add(c1);

        Circle _c1= (Circle) c1.clone();
        shapes.add(_c1);
        Rectangle r1=new Rectangle(10,20,"red",15,20);
        shapes.add(r1);
        Rectangle _r1= (Rectangle) r1.clone();
        shapes.add(_r1);
        for (Shape shape : shapes) {
            shapesCopy.add((Shape) shape.clone());
        }

    }

    @Test
    public void objectAndCloneObjectAreNotTheSame(){

        for (int i = 0; i < shapes.size(); i++) {
           assertThat(shapes.get(i)==shapesCopy.get(i)).isFalse();
        }
    }
    @Test
    public void objectAndCloneObjectAreIdentical(){
        for (int i = 0; i < shapes.size(); i++) {
            assertThat(shapes.get(i).equals(shapesCopy.get(i))).isTrue();
        }
    }

    @Test
    public void cache(){
        Circle c1=new Circle(10,20,"red",15);
        c1.saveInCache("BigRedCircle");
        Circle _c1= (Circle) Shape.getFromCache("BigRedCircle");
        assertThat(c1.equals(_c1)).isTrue();
        assertThat(c1==_c1).isFalse();
    }



}
