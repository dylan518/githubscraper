package figures.figure;

import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import figures.circle.Circle;
import figures.rectangle.Rectangle;
import figures.square.Square;

import static com.fasterxml.jackson.annotation.JsonTypeInfo.Id.DEDUCTION;


@JsonTypeInfo(use = DEDUCTION)
@JsonSubTypes({
        @JsonSubTypes.Type(value = Circle.class),
        @JsonSubTypes.Type(value = Rectangle.class),
        @JsonSubTypes.Type(value = Square.class),
})
public abstract class Shape {
    private final String type;

    public Shape() {
        this.type = this.getClass().getSimpleName();
    }

    public abstract double getArea();

    public abstract double getPerimeter();

    public String getType() {
        return type;
    }


}
