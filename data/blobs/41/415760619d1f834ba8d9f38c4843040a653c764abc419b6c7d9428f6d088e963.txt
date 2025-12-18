/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package classes;

/**
 * @author carre
 * The TablaHash class represents a generic hash table.
 * It allows storing elements of type T using a hash function to calculate the storage index.
 *
 * @param <T> The type of element to store in the hash table.
 */
public class TablaHash<T> {
    private int capacity;
    public Lista<T>[] table;
    private int size;
    /**
     * Constructs a new TablaHash with the specified capacity.
     *
     * @param capacity The capacity of the hash table.
     */
    public TablaHash(int capacity){
        this.capacity = capacity;
        this.table = new Lista[capacity];
    }
    /**
     * Initializes the hash table with the specified capacity.
     *
     * @param capacity The capacity of the hash table.
     */
    final void intit(int capacity){
        for(int i= 0;i<capacity;i++){
            Lista<T> temp = new Lista<>();
            this.table[i] = temp;
        }
    }
    /**
     * Hash function that calculates the storage index for a given key.
     *
     * @param key The key or element used to calculate the storage index.
     * @return The calculated storage index.
     */
    private int hashFunction(Object key) {
        int hashCode = key.hashCode();
        return Math.abs(hashCode) % table.length;
}
    /**
     * Adds an element to the hash table.
     *
     * @param element The element to add.
     */
    public void addElement(T element){
        int index = hashFunction(element);
        table[index].addAtTheEndT(element);
    }
    /**
     * Checks if an element is present in the hash table.
     *
     * @param element The element to search for.
     * @return true if the element is present, false otherwise.
     */
    public boolean findElement(T element){
        int index = hashFunction(element);
        return table[index].findElement(element);
    }
    /**
     * Deletes an element from the hash table.
     *
     * @param element The element to delete.
     * @return true if the element was deleted, false otherwise.
     */
    public boolean deleteElement(T element){
        int index = hashFunction(element);
        return table[index].deleteIntN(element);
    }
    /**
     * Adds an element with a specific key to the hash table.
     *
     * @param element The element to add.
     * @param key The key used to determine the storage index.
     */
    public void addElementK(T element, int key){
        table[key].addAtTheEndT(element);
    }
    /**
     * Prints the contents of the hash table.
     */
    public void print(){
        for(int i = 0; i<this.capacity;i++){
            table[i].print();
        }
    }
}
