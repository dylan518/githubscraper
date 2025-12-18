package properties;

import org.aeonbits.owner.Config;
import org.aeonbits.owner.ConfigFactory;
import org.testng.Assert;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Properties;

public interface ImportConfig extends Config {

    @DefaultValue("apple")
    String foo();

//    @DisableFeature(DisableableFeature.PARAMETER_FORMATTING)
    @DefaultValue("banana %s")
    String bar(String name);

    @Key("baz")
//    @DefaultValue("pear")
    String baz();


//    @Key("list")
    @DefaultValue("[1, 2]")
    List<Integer> ints();
}

class MyPersonalDebug{
    public static void main(String[] args) throws IOException {
        Properties properties = new Properties();
//        properties.setProperty("foo", "pineapple");
//        properties.setProperty("bar", "orange");
//        properties.setProperty("baz", "lime");

        ImportConfig importConfig = ConfigFactory.create(ImportConfig.class, properties);
        System.out.println(importConfig.bar("Lua"));

        String listStrings = Arrays.toString(new int[]{1,2,3,4,5,6});
        FileOutputStream file = new FileOutputStream("src/main/java/properties/debug.properties");
        properties.setProperty("list", listStrings);
        properties.store(file, "list with integer");
        String[] listInteger = properties.getProperty("list").substring(1, properties.getProperty("list").length() -1).trim().split(", ");
        List<Integer> newList = new ArrayList<>();
//        System.out.println(listInteger);
        for (String elt: listInteger){
            System.out.println(elt);
            newList.add(Integer.parseInt(elt));
        }
        System.out.println(newList);

    }
}