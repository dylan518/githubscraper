import java.util.Scanner;

class CalculatorUsingConstructors {

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter two numbers to run the calculator: ");
    float num1 = scan.nextFloat();
    float num2 = scan.nextFloat();

    Add addConstructor = new Add(num1, num2);
    Sub subConstructor = new Sub(num1, num2);
    Mul mulConstructor = new Mul(num1, num2);
    Div divConstructor = new Div(num1, num2);

    scan.close();
  }
}

class Add {

  Add(float a, float b) {
    System.out.println(
      "Adding " + a + " and " + b + " gives output: " + (a + b)
    );
  }
}

class Sub {

  Sub(float a, float b) {
    System.out.println(
      "Subtracting" + a + " and " + b + " gives output: " + (a - b)
    );
  }
}

class Mul {

  Mul(float a, float b) {
    System.out.println(
      "Multiplying " + a + " and " + b + " gives output: " + (a * b)
    );
  }
}

class Div {

  Div(float a, float b) {
    System.out.println(
      "Dividing " + a + " by " + b + " gives output: " + (a / b)
    );
  }
}
