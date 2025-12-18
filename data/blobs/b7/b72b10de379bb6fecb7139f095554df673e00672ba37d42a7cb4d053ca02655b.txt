package com.mvan.estruturas.fila;


/**
 * 
 */
public class PriorityQueue { 
    private NodePriority head;
    private NodePriority tail;
    int size;

    public PriorityQueue () {
        this.head = new NodePriority();
        this.tail = new NodePriority();
        this.head.setNextPointer(tail);
        this.tail.setPrevPointer(head);
        this.size = 0;
    }


    private void createPriority(int p) {
        NodePriority np = new NodePriority();
        np.setPriority(p);
        // System.out.println(np.getPriority());
        np.setNextPointer(tail);
        np.setPrevPointer(tail.getPrevPointer());
        tail.getPrevPointer().setNextPointer(np);
        tail.setPrevPointer(np);
        np.setQueue(new Queue());
    }

    public void setPriorityInterval(int maxPriority, int minPriority) {
        if (maxPriority > minPriority) {
            throw new Error("A prioridade maxima deve ser de valor menor que a prioridade minima");
        } else {
            int i = maxPriority;
            
            while (i <= minPriority) {
                
                createPriority(i);
                this.size++;
                i++;
            }
        }
    }

    public void enqueue(NodeQueue node) {
        if(node.getPriority() < this.head.getNextPointer().getPriority() ||
            node.getPriority() > this.tail.getPrevPointer().getPriority()
            ) {
                throw new Error("insira uma prioridade dentro do intervalo");
        }
        NodePriority np = this.head.getNextPointer();
        while (np.getPriority() != node.getPriority()) {
            np = np.getNextPointer();
        }
        Queue q = np.getQueue();
        q.enqueue(node);
        np.setQueue(q);
    }

    public NodeQueue dequeue() {
        NodePriority np = this.head.getNextPointer();
        while(np.getQueue().size == 0) {
            np = np.getNextPointer();
        }

        return np.getQueue().dequeue();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Head - ");
        NodePriority np = this.head.getNextPointer();
        int i = 0;
        while (i < this.size) {
            sb.append("\n");
            sb.append(np.getPriority() + " --> ");
            sb.append(np.getQueue().toString());
            np = np.getNextPointer();
            i++;
        }
        sb.append("\n");
        sb.append("tail");

        return sb.toString();


    }
}
