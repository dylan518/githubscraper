package org.example;

import java.io.UnsupportedEncodingException;

public class Base64 {

    private Base64() {}

    private static final String Base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    public static String encrypt(byte[] byteMass) {
        String ost = "";
        String binaryString = "";
        String answer = "";
        for (int i = 0; i < byteMass.length; ++i) {
            binaryString += toBinaryString(byteMass[i]);
        }
        if (byteMass.length % 3 != 0) {
            switch (byteMass.length % 3) {
                case 1:
                    ost = "==";
                    binaryString += "0000";
                    break;
                case 2:
                    ost = "=";
                    binaryString += "00";
                    break;
            }
        }
        String[] sixByted = splitByNum(binaryString, 6);
        for (String sixBytes: sixByted) {
            answer += Base64Chars.charAt(Integer.parseInt(sixBytes, 2));
        }
        return answer + ost;
    }

    public static String encrypt(String str) {
        byte[] byteMas = new byte[0];
        try {
            byteMas = str.getBytes("cp866");
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }
        return encrypt(byteMas);
    }

    public static byte[] decryptToBinaryMas(String cypher) {
        try {
            checkValidness(cypher);
        } catch (NotBase64StringException e) {
            System.out.println(e.getMessage());
            return null;
        }
        String binaryString = "";
        for (int i = 0; i < cypher.length(); ++i) {
            if (cypher.charAt(i) != '=') {
                byte index = 0;
                for (int j = 0; j < Base64Chars.length(); ++j) {
                    if (cypher.charAt(i) == Base64Chars.charAt(j)) {
                        index = (byte)j;
                        break;
                    }
                }
                binaryString += toBinaryString(index).substring(2, 8);
            } else {
                binaryString = binaryString.substring(0, binaryString.length() - 2);
            }
        }
        String[] eightByted = splitByNum(binaryString, 8);
        byte[] answer = new byte[eightByted.length];
        for (int i = 0; i < eightByted.length; ++i) {
            answer[i] = toByte(eightByted[i]);
        }
        return answer;
    }

    public static String decryptToString(String cypher) {
        byte[] bytes = decryptToBinaryMas(cypher);
        String result = null;
        result = new String(bytes);
        return result;
    }

    private static String toBinaryString(byte byte_) {
        String tmp = "";
        int neededZeros = 8 - Integer.toBinaryString(byte_).length();
        while (neededZeros > 0) {
            tmp += "0";
            --neededZeros;
        }
        tmp += Integer.toBinaryString(byte_);
        return tmp;
    }

    private static byte toByte(String str) {
        return (byte) Integer.parseInt(str, 2);
    }

    private static String[] splitByNum(String str, int num) {
        int masIndex = 0, ind = 0;
        String[] strings = new String[(int)Math.ceil((double)str.length() / num)];
        while (ind < str.length()) {
            strings[masIndex] = str.substring(ind, Math.min(ind + num, str.length()));
            ind += num;
            ++masIndex;
        }
        return strings;
    }

    private static void checkValidness(String str) throws NotBase64StringException{
        boolean legit = true;
        for (int i = 0; i < str.length(); ++i) {
            if (!Base64Chars.contains("" + str.charAt(i)) && str.charAt(i) != '=') {
                legit = false;
                break;
            }
        }
        if (str.length() % 4 != 0) legit = false;
        if (!legit) throw new NotBase64StringException();
    }
}
