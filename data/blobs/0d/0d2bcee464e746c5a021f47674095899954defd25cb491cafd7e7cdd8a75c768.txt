package Task2;

import java.lang.annotation.Annotation;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.Scanner;

public class ClassReflectionInfo {
    public static void main(String[] args) {

        String s = (char) 27 + "[31m";
        String s1 = (char) 27 + "[39m";
        String s2 = (char) 27 + "[34m";


        Scanner scan = new Scanner(System.in);
        System.out.println("Enter Class name: ");
        String str = scan.nextLine();

        Class<?> cl = null;


        try {
            cl = Class.forName(str);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println(s2 + "Short name: " + s1 + cl.getName().substring(cl.getName().lastIndexOf('.') + 1));
        System.out.println(s2 + "Full name: " + s1 + cl.getName());

        Field[] fieldArr = cl.getDeclaredFields();
        System.out.println(s2 + "Class fields: " + s1 + Arrays.asList(fieldArr));

        Method[] methArr = cl.getDeclaredMethods();
        System.out.println(s2 + "Class methods: " + s1 + Arrays.asList(methArr));

        Annotation[] annoArr = cl.getDeclaredAnnotations();
        System.out.println(s2 + "Class annotations: " + s1 + Arrays.asList(annoArr));

        Constructor[] constArr = cl.getConstructors();
        System.out.println(s2 + "Class constructors: " + s1 + Arrays.asList(constArr));
    }
}
