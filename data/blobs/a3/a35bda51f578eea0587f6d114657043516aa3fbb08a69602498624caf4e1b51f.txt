package NIO;

import java.nio.file.*;



public class PathDemo {
    public static void main(String[] args) {
        Path path = Paths.get("Example.txt");               // у Path куча всяких методов крутых
        try {
             Files.lines(path).forEach(System.out::println);     // и у класса Files. можно не изобретать велосипеды, а в одну строку получить строки из файла :)
        }
        catch (Exception e){
            e.printStackTrace();
        }
        System.out.println(path.toAbsolutePath());
    }
}
