package pl.migibud.dfs2;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class App {
    public static void main(String[] args) {

        Vertex a = new Vertex("A");
        Vertex b = new Vertex("B");
        Vertex c = new Vertex("C");
        Vertex d = new Vertex("D");
        Vertex e = new Vertex("E");
        Vertex f = new Vertex("F");
        Vertex g = new Vertex("G");
        Vertex h = new Vertex("H");

        Map<Vertex, List<Vertex>> adjacencyList = new HashMap<>();
        adjacencyList.put(a, List.of(b, f, g));
        adjacencyList.put(b, List.of(a, c, d));
        adjacencyList.put(f, List.of(a));
        adjacencyList.put(g, List.of(h));
        adjacencyList.put(c, List.of(b));
        adjacencyList.put(d, List.of(b, e));
        adjacencyList.put(h, List.of(g));
        adjacencyList.put(h, List.of(g));


//        Deque<String> stack = new ArrayDeque<>();
//
//        stack.addFirst("Piotr");
//        stack.addFirst("Anna");
//        stack.addFirst("Wojtek");
//
//        System.out.println(stack.remove());
//        System.out.println(stack.remove());
//        System.out.println(stack.remove());

        DfsRecursion dfs = new DfsRecursion();
        dfs.traverse(adjacencyList, a);


    }
}
