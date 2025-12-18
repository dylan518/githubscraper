import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.stream.Collectors;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

public class Driver {
    static Queue<String> queue = new LinkedList<>();
    static Map<String, Integer> visitedUrls = new HashMap<>();
    static final int MAX_DEPTH = 5;
    public static void main(String[] args) {
        try {
            queue.add("https://abcnews.go.com");
            ExecutorService executorService = Executors.newFixedThreadPool(5);
            while (!queue.isEmpty()) {
                List<Callable<String>> callables = queue.stream()
                        .map(url -> (Callable<String>) (() -> read(url)))
                        .collect(Collectors.toList());
                System.out.println(queue);
                queue.clear();
                List<Future<String>> futures = executorService.invokeAll(callables);
                for(Future f: futures){
                    f.get();
                }
                System.out.println("Visited URLs:\n"+visitedUrls);
                System.out.println("Distinct URLs visited:\n"+visitedUrls.size());

            }
        }
        catch (Exception ex){
            System.out.println(ex.getMessage());
        }
    }
    public static String read(String URL){
        try{
            if(visitedUrls.containsKey(URL))
                return "";
            Connection conn = Jsoup.connect(URL);
            Document doc = conn.get();
            if(conn.response().statusCode()==200){
                System.out.println("Received Webpage at "+URL);
                String title = doc.title();
                System.out.println(title);
                synchronized (Driver.class) {
                    visitedUrls.put(URL, visitedUrls.getOrDefault(URL, 0) + 1);
                }
                int currDepth = 1;
                if(doc!=null){
                    for(Element link: doc.select("a[href]")){
                        String nextLink = link.absUrl("href");
                        if(nextLink.endsWith("/") || nextLink.endsWith("#")){
                            nextLink = nextLink.substring(0,nextLink.length()-1);
                        }
                        if(!visitedUrls.containsKey(nextLink)){
                            queue.add(nextLink);
                            if(++currDepth==MAX_DEPTH){
                                break;
                            }
                        }
                    }
                }
            }
        }
        catch (Exception ex){
            System.out.println(ex.getMessage());
        }
        return "";
    }
}
