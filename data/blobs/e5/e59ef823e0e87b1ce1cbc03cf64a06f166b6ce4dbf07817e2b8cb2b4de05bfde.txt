package com.bagile.gmo.util;

import com.bagile.gmo.exceptions.AttributesNotFound;
import com.bagile.gmo.exceptions.ErrorType;
import com.querydsl.core.types.dsl.BooleanExpression;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by adadi on 12/23/2015.
 */

public class Search {
    private Search() {
    }




    public static String getField(String name, String search) throws ClassNotFoundException, NoSuchMethodException, IllegalAccessException, InstantiationException, InvocationTargetException, NoSuchFieldException {
        String field = "";
        if ("StockView".equals(name)) {
        	name = "Stock";
        }
        if ("ContainerView".equals(name)) {
        	name = "Container";
        }
        if ("ProductView".equals(name)) {
            name = "Product";
        }
        if ("AccountView".equals(name)) {
            name = "Account";
        }
        if (search.indexOf('.') == -1) {
            Class<?> cls = Class.forName("com.bagile.gmo.mapper." + name + "Mapper");
            //Object mapper = cls.newInstance();
            Method method = cls.getDeclaredMethod("getField", String.class);
            field = (String) method.invoke(null, search);
        } else {

            StringTokenizer stringTokenizer = new StringTokenizer(search, ".");
            String str = (String) stringTokenizer.nextElement();
            Class<?> cls = Class.forName("com.bagile.gmo.mapper." + name + "Mapper");
            //Object mapper = cls.newInstance();
            Method method = cls.getDeclaredMethod("getField", String.class);
            field = (String) method.invoke(null, str);
            cls = Class.forName("com.bagile.gmo.dto." + name);
            String finalStr = str;
            Class<?> type = Arrays.stream(cls.getDeclaredFields()).map(field1 -> field1.getName()).anyMatch(s -> s.equals(finalStr)) ?  cls.getDeclaredField(str).getType() : cls.getSuperclass().getDeclaredField(str).getType();
            if (type.getTypeName().toString().equals("java.util.Set")) {
                ParameterizedType parameterizedType = (ParameterizedType) cls.getDeclaredField(str).getGenericType();
                type = (Class<?>) parameterizedType.getActualTypeArguments()[0];
            }
            while (stringTokenizer.hasMoreElements()) {
                str = (String) stringTokenizer.nextElement();
                name = type.getSimpleName();
                cls = Class.forName("com.bagile.gmo.mapper." + name + "Mapper");
                //mapper = cls.newInstance();
                method = cls.getDeclaredMethod("getField", String.class);
                field += "." + (String) method.invoke(null, str);
                cls = Class.forName("com.bagile.gmo.dto." + name);
                type = cls.getDeclaredField(str).getType();
                if (type.getTypeName().toString().equals("java.util.Set")) {
                    ParameterizedType parameterizedType = (ParameterizedType) cls.getDeclaredField(str).getGenericType();
                    type = (Class<?>) parameterizedType.getActualTypeArguments()[0];
                }
            }
        }
        return field;
    }

    private static String search(Map<String, String> map, String value) {

        for (Map.Entry entry : map.entrySet()
                ) {
            if (value.equals(map.get(entry.getKey()))) {
                return entry.getKey().toString();
            }
        }
        return "";
    }












    public static String getFieldDto(String name, String search) throws ClassNotFoundException, NoSuchMethodException, IllegalAccessException, InstantiationException, InvocationTargetException, NoSuchFieldException {
        String field = "";
        if (search.indexOf('.') == -1) {
            Class<?> cls = Class.forName("com.bagile.gmo.mapper." + name + "Mapper");
            Object mapper = cls.newInstance();
            Method method = cls.getDeclaredMethod("getMap");
            Map<String, String> map = (HashMap<String, String>) method.invoke(mapper);
            field = search(map, search);
        } else {
            StringTokenizer stringTokenizer = new StringTokenizer(search, ".");
            String field0 = (String) stringTokenizer.nextElement();
            String field1 = (String) stringTokenizer.nextElement();
            Class<?> cls = Class.forName("com.bagile.gmo.mapper." + name + "Mapper");
            Object mapper = cls.newInstance();
            Method method = cls.getDeclaredMethod("getMap", String.class);
            Map<String, String> map = (HashMap<String, String>) method.invoke(mapper);
            field = search(map, field0);
            cls = Class.forName("com.bagile.gmo.dto." + name);
            cls = Class.forName("com.bagile.gmo.mapper." + cls.getDeclaredField(field0).getType().getSimpleName() + "Mapper");
            Object mapper2 = cls.newInstance();
            method = cls.getDeclaredMethod("getMap");
            map = (HashMap<String, String>) method.invoke(mapper2);
            field += "." + (String) search(map, field1);
        }
        return field;
    }

    public static BooleanExpression expression(String search, Class<?> entity) throws AttributesNotFound, ErrorType {
        PredicatesBuilder builder = new PredicatesBuilder();
        if (null == search) {
            throw new AttributesNotFound("");
        }
        Pattern pattern = Pattern.compile("([a-z]\\w+(\\.[a-z]\\w+)*)\\s*([:~<>!^])\\s*(((?!,).)*)\\s*,\\s*");
        Matcher matcher = pattern.matcher(search + ",");
        boolean patternTrue = false;
        while (matcher.find()) {
            try {
                builder.with(getField(entity.getSimpleName().substring(3), matcher.group(1))
                        , matcher.group(3), matcher.group(4));
            } catch (Exception e) {
                throw new AttributesNotFound(search);
            }
            patternTrue = true;
        }
        if (!patternTrue) {
            throw new AttributesNotFound(search);
        }
        return builder.buildAND(entity);
    }

    public static void main(String[] args) throws IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException, NoSuchFieldException, ClassNotFoundException {
        String search = "product.aliases.eanCode";
        String name = "Stock";
        StringTokenizer stringTokenizer = new StringTokenizer(search, ".");
        String str = (String) stringTokenizer.nextElement();
        Class<?> cls = Class.forName("com.bagile.gmo.mapper." + name + "Mapper");
        Object mapper = cls.newInstance();
        Method method = cls.getDeclaredMethod("getField", String.class);
        String field = (String) method.invoke(mapper, str);
        cls = Class.forName("com.bagile.gmo.dto." + name);
        Class<?> type = cls.getDeclaredField(str).getType();
        if (type.getTypeName().toString().equals("java.util.Set")) {
            ParameterizedType parameterizedType = (ParameterizedType) cls.getDeclaredField(str).getGenericType();
            type = (Class<?>) parameterizedType.getActualTypeArguments()[0];
        }
        while (stringTokenizer.hasMoreElements()) {
            str = (String) stringTokenizer.nextElement();
            name = type.getSimpleName();
            cls = Class.forName("com.bagile.gmo.mapper." + name + "Mapper");
            mapper = cls.newInstance();
            method = cls.getDeclaredMethod("getField", String.class);
            field += "." + (String) method.invoke(mapper, str);
            cls = Class.forName("com.bagile.gmo.dto." + name);
            type = cls.getDeclaredField(str).getType();
            if (type.getTypeName().toString().equals("java.util.Set")) {
                ParameterizedType parameterizedType = (ParameterizedType) cls.getDeclaredField(str).getGenericType();
                type = (Class<?>) parameterizedType.getActualTypeArguments()[0];
            }
        }
    }
}
