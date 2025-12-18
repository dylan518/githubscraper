import java.math.BigInteger;

public class Java00005 {
  public String solution(String a, String b) {
    BigInteger bigA = new BigInteger(a);
    BigInteger bigB = new BigInteger(b);

    BigInteger sum = bigA.add(bigB);

    String answer = sum.toString();
    return answer;
}
}
