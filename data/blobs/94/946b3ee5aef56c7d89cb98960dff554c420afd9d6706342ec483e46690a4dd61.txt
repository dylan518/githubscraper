package com.design.pattern.db.interator.v4;

public class LikedListNew implements CollectionNew {
    Node head = null;
    Node tail = null;
    private int size = 0;

    @Override
    public void add(Object o) {
        Node n = new Node(o);
        n.next = null;

        if (head == null) {
            head = n;
            tail = n;
        }

        tail.next = n;
        tail = n;
        size++;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public IteratorNew iterator() {
        return new ListItr();
    }

    private class ListItr implements IteratorNew {
        Node cur;

        ListItr() {
            cur = head;
        }

        @Override
        public boolean hasNext() {
            return cur != null;
        }

        @Override
        public Object next() {
            Object o = cur.o;
            cur = cur.next;
            return o;
        }
    }

    private class Node {
        private Object o;
        Node next;

        public Node(Object o) {
            this.o = o;
        }
    }

}
