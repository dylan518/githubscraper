package dirapp;

import java.util.PriorityQueue;
import java.util.Queue;

public class JQueueApp {
    public static void main(String[] args) {

        // Queue adalah implementasi dari struktur data antrian atau FIFO (First In First Out)
        // Queue adalah interface, untuk membuat object nya bisa menggunakan class yg implement, contohnya ArrayDeque(), PriorityQueue(), LinkedList()

        // ArrayDeque() menggunakan Array sebagai implementasi Queue nya
        // Queue<String> queue = new ArrayDeque<>();

        // PriorityQueue() menggunakan Array sebagai implementasi Queue nya, namun diurutkan menggunakan Comparable atau Comparator
        Queue<String> queue = new PriorityQueue<>();

        // LinkedList() menggunakan double linked list sebagai implementasi queue nya
        // Queue<String> queue = new LinkedList<>();

        queue.add("Sanjaya");
        queue.add("Dira");
        queue.add("Wardana");

        for (String next = queue.poll(); next != null; next = queue.poll()) {
            System.out.println(next);
        }

        System.out.println(queue.size());
    }
}


// beberapa mtehod yang ada di Queue Interface
// offer(E): boolean
// remove(): E --> mengambil data pertama dan menghapusnya, jika sudah habis akan return exception
// poll(): E --> mengambil data pertama dan menghapusnya, beda return errornya dengan remove(), jika datanya sudah habis akan return null
// element(): E --> mengambil data pertama, jika data tidak ada akan return exception
// peek(): E --> mengambil data pertama, jika data tidak ada akan return null