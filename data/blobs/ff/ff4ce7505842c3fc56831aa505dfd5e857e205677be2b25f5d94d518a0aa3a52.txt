package JavaStreams;

import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class streams {
    @Test
    public void regular(){  // This is the regular method we use to get the names which start with A.
        ArrayList<String> names=new ArrayList<String>();
        names.add("Adam");
        names.add("Raj");
        names.add("Kamal");
        names.add("Aadarsh");
        names.add("Praveen");
        int count=0;
        for(int i=0;i<names.size();i++){
            String actual=names.get(i);
            if(actual.startsWith("A")){
                count++;
            }

        }
        System.out.println(count);
    }
    @Test
    public void streamFilter(){   // here we can see the usage of streams filter and compact all the regular code into 1 line concise code
        ArrayList<String> names=new ArrayList<String>();
        names.add("Adam");
        names.add("Raj");
        names.add("Kamal");
        names.add("Aadarsh");
        names.add("Praveen");

        Long c=names.stream().filter(i->i.startsWith("A")).count(); // so here we have used streams to filter our array and lambda expression to get the required output.
        System.out.println(c);

        //we can directly creat a strem in the below method
        Stream.of("Adam","prem","Adarsh","kamal","Raj");
        //and we can apply our requred filter on this stream
        Stream.of("Adam","prem","Adarsh","kamal","Raj").filter(i->i.startsWith("A")).forEach(i->System.out.println(i));
        // if we want to print only 1st name that starts with A.Here in the below code we are limiting with only 1 element to print
        Stream.of("Adam","prem","Adarsh","kamal","Raj").filter(i->i.startsWith("A")).limit(1).forEach(i-> System.out.println("1st name that starts with A "+i));

    }
    @Test
    public void streamMap(){
        ArrayList<String> name=new ArrayList<String>();
        name.add("Adam");
        name.add("Raja");
        name.add("Kamal");
        name.add("Aadarsh");
        name.add("Praveena");

        // Print names which is having last letter as "a" with uppercase.
        Stream.of("Adam","prem","Adarsh","kamala","Raja").filter(s->s.endsWith("a")).map(s->s.toUpperCase(Locale.ROOT)).forEach(s->System.out.println(s));
        // Print names which start with "A" and sorted
        List<String> namestest= Arrays.asList("Adam","prem","Adarsh","kamala","Raja");
        namestest.stream().filter(s->s.startsWith("A")).sorted().map(s->s.toUpperCase(Locale.ROOT)).forEach(s-> System.out.println(s));
        System.out.println("*****************************************************************");
        //Merging 2 list
        List<String> names1= Arrays.asList("Adam","prem","Adarsh","kamala","Raja");
        Stream<String> newStream=Stream.concat(name.stream(),names1.stream());
//        newStream.forEach(s-> System.out.println(s));
        //to validate if the string is present in the list or not
        boolean t=newStream.anyMatch(s->s.equalsIgnoreCase("prem"));
        Assert.assertTrue(t);
    }
    @Test
    public void collectorStream(){  //collect method in the stream is used to store the processed streams in list,array,set etc and perform further actions on it
       List <String> values= Stream.of("Adam","prem","Adarsh","kamala","Raja").filter(s->s.startsWith("A")).collect(Collectors.toList());
        System.out.println(values.get(1));

        List<Integer> num=Arrays.asList(1,3,4,2,5,6,6,7,7,8,8,9,0);
        num.stream().distinct().forEach(s-> System.out.println(s));  // disctinct is used to collect only unique values from the stream

    }
}
