package BacktrackingProblems;

import java.util.*;

/*Given an undirected graph and a number m, determine if the graph can be
colored with at most m colors such that no two adjacent vertices of the
graph are colored with the same color*/

/*Another Approach: Using BFS (Breadth-First-Search)

First, begin the BFS traversal.

Secondly, Discover the nearby (neighboring) nodes to the present node.
Give the neighboring node the following color if the current node’s
colour and the adjacent node’s color match. Verify whether
the current node has been visited. If it has not been visited yet,
mark it as visited and put it in a queue.
Finally, Verify whether the color is available. Return if the scenario changes to
false.  Carry out the action on each of the nodes that have been supplied.(all the nodes)*/
public class ColoringGraphBFS {
    static int possiblePaint(ArrayList<Node> nodes, int n, int m) {

        // Create a visited array of n nodes
        ArrayList<Integer> visited = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            visited.add(0);
        }

        // maxColors used till now are 1 as all nodes are painted color 1
        int maxColors = 1;

        for (int sv = 1; sv <= n; sv++) {
            if (visited.get(sv) > 0) {
                continue;
            }

            // If the starting point is unvisited, mark it visited and push it in queue
            visited.set(sv, 1);
            Queue<Integer> q = new LinkedList<>();
            q.add(sv);

            // BFS
            while (!q.isEmpty()) {
                int top = q.peek();
                q.remove();

                // Checking all adjacent nodes to "top" edge in our queue
                for (int it : nodes.get(top).edges) {

                    // If the color of the adjacent node is same, increase it by 1
                    if (nodes.get(top).color
                            == nodes.get(it).color) {
                        nodes.get(it).color += 1;
                    }

                    // If the number of colors used exceeds m, return 0
                    maxColors =
                            Math.max(maxColors, Math.max(nodes.get(top).color, nodes.get(it).color));
                    if (maxColors > m)
                        return 0;

                    // If the adjacent node is not visited, mark it visited and push it in queue
                    if (visited.get(it) == 0) {
                        visited.set(it, 1);
                        q.remove(it);
                    }
                }
            }
        }
        return 1;
    }

    // Driver code
    public static void main(String[] args) {
        int n = 4;
        int[][] graph = {{0, 1, 1, 1},
                {1, 0, 1, 0},
                {1, 1, 0, 1},
                {1, 0, 1, 0}};
        int colorsNumber = 3; // Number of colors

        ArrayList<Node> nodes = new ArrayList<>();

        for (int i = 0; i < n + 1; i++) {
            nodes.add(new Node());
        }

        // Add edges to each node as per given input
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] > 0) {
                    nodes.get(i).edges.add(i);
                    nodes.get(j).edges.add(j);
                }
            }
        }

        int res = possiblePaint(nodes, n, colorsNumber);
        if (res == 1) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
}

class Node {
    int color = 1;
    Set<Integer> edges = new HashSet<>();
}

/*Expected Output::

True

* */
