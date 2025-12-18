package katas;

public class FlippingNumbers {
  public static long solution(long number) {
    String binaryString = String.format("%32s", Long.toBinaryString(number)).replace(' ', '0');

    StringBuilder flippedBinaryString = new StringBuilder();
    for (char bit : binaryString.toCharArray()) {
      if (bit == '0') {
        flippedBinaryString.append('1');
      } else {
        flippedBinaryString.append('0');
      }
    }

    return Long.parseUnsignedLong(flippedBinaryString.toString(), 2);
  }

}
