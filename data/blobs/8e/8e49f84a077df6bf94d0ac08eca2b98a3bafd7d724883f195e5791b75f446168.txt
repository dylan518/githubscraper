package Main.Materia.Controllers;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;

import Main.Materia.Models.NodeG;

public class Graph {

    private List<NodeG> nodes;
    
    public Graph(){
        this.nodes = new ArrayList<>();
    }

    //Metodo para añadir un nodo
    public NodeG addNode(int value){
        NodeG nodeG = new NodeG(value);
        nodes.add(nodeG);
        return nodeG;
    }

    //Metodo para añadir un arista
    public void addEdge(NodeG src, NodeG dest){
        src.addNeighbors(dest);
        dest.addNeighbors(src);
    }
    public void addEdgeDos(NodeG src, NodeG dest){
        src.addNeighbors(dest);
        //dest.addNeighbors(src);
    }

    //Metodo para imprimir el grafo
    public void printGraph(){
        for(NodeG nodeG : nodes){
            System.out.print("Vertex " + nodeG.getValue() + ": ");
            for(NodeG nei : nodeG.getNeighbors()) {
                System.out.print(nei.getValue() + " -> ");
            }
            System.out.println();
        }
    }

    public void getDFS(NodeG start){

        Set<NodeG> visitados = new HashSet<>();
        System.out.println("\nDFS desde el nodo "+ start.getValue()+" :");
        getDFSUtil(start, visitados);
        System.out.println();
    }
        
    private void getDFSUtil(NodeG node, Set<NodeG> visitados) {
        if(visitados.contains(node)){
            return;
        }
        visitados.add(node);
        System.out.print(node.getValue()+ " ");
        
        for(NodeG neighbor : node.getNeighbors()){
            getDFSUtil(neighbor, visitados);
        }
    }

    public void getBFS(NodeG start){
        Set<NodeG> visitados = new HashSet<>();
        Queue<NodeG> cola = new LinkedList<>();

        System.out.println("BFS desde el nodo "+ start.getValue());
        cola.add(start);
        visitados.add(start);

        while(!cola.isEmpty()){
            NodeG actual= cola.poll();
            System.out.print(actual.getValue() + " ");

            for(NodeG neighbor : actual.getNeighbors()){
                if(!visitados.contains(neighbor)){
                    visitados.add(neighbor);
                    cola.add(neighbor);

                }
            }
        }
    }

    public boolean getDFS(NodeG start, NodeG destino){
        Set<NodeG> visitados = new HashSet<>();
        return getDFSUtil(start, destino, visitados);
    }

    private boolean getDFSUtil(NodeG node, NodeG destino,Set<NodeG> visitados){
        if(node.equals(destino)){
            return true;
        }
        if(visitados.contains(node)){
            return false;
        }

        visitados.add(node);

        for(NodeG neighbor : node.getNeighbors()){
            if(getDFSUtil(neighbor, destino, visitados)){
                return true;
            }
        }
        return false;
    }
}
