import java.util.Objects;

public class Leaf {
  String color = "Green";
  LeafState state = LeafState.CLEAN;

  public void YellowLeaf() {
    color = "Yellow";
  }

  public void SnowLeaf() {
    state = LeafState.SNOWY;
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Leaf leaf = (Leaf) o;
    return color.equals(leaf.color) && state.equals(leaf.state);
  }

  @Override
  public int hashCode() {
    return Objects.hash(color + state.toString());
  }

  @Override
  public String toString() {
      return "Leaf{" +
              "color='" + color + '\'' +
              "state='" + state + '\'' +
              '}';
  }
}
