public class AoifeAwesomeASCIIArt {
    public static void decoration(String lines) {
        int pointer = 0, length = 0;
        String[] temp = lines.split(" ");
        for (int i = 0; i < temp.length; i++) {
            length = Math.max(length, temp[i].length());
        }
        System.out.println(length);
        while (pointer < lines.length() - length) {
            String line = lines.substring(pointer, pointer + length);
            System.out.println(line);
            if (!line.substring(length - 1).equals(" ") && line.contains(" ")) {
                int index = line.lastIndexOf(" ");
                line = lines.substring(pointer, pointer + index);
                pointer = pointer + index;
            } else {
                pointer += length;
            }
            System.out.println(line);
        }
    }

    public static void main(String[] args) {
        decoration("Welcome to IrlCPC 2019!");
    }
}
