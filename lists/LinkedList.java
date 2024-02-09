/* doubly linked-list implementation with a single sentinel node */


public class LinkedList<T> {
    Node sentinel;
    int size;
    class Node {
        T data;
        Node next;
        Node prev;
        Node(T d) {
            data = d;
            next = null;
            prev=null;
        }
    }
    public LinkedList() {
        sentinel = new Node(null);
        sentinel.next = sentinel;
        sentinel.prev=sentinel;
        size=0;
    }   
    public boolean isEmpty() {
        return sentinel.next == sentinel;
    }
    public void push_front(T data) {
        Node newNode = new Node(data);
        newNode.next = sentinel.next;
        newNode.prev=sentinel;
        sentinel.next.prev=newNode;
        sentinel.next = newNode;
        size++;
        
    }
    public void push_back(T data) {
        Node newNode = new Node(data);
        newNode.next = sentinel;
        newNode.prev=sentinel.prev;
        sentinel.prev.next=newNode;
        sentinel.prev = newNode;
        size++;
    }
    public T pop_front() {
        if(isEmpty()) {
            return null;
        }
        Node temp = sentinel.next;
        sentinel.next = temp.next;
        temp.next.prev=sentinel;
        size--;
        return temp.data;
    }
    public T pop_back() {
        if(isEmpty()) {
            return null;
        }
        Node temp = sentinel.prev;
        sentinel.prev = temp.prev;
        temp.prev.next=sentinel;
        size--;
        return temp.data;
    }
    public void print(){
        Node node = sentinel.next;
        while(node != sentinel) {
            System.out.print(node.data);
            node = node.next;
            if(node!=sentinel)
                System.out.print(",");
        }
        System.out.println();
    }
    public T get(int index) {
        if(index < 0 || index >= size) {
            return null;
        }
        Node temp = sentinel.next;
        for(int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp.data;
    }
    public boolean insert(T data, int index) {
        if(index < 0 || index > size) {
            return false;
        }
        Node newNode = new Node(data);
        Node temp = sentinel;
        for(int i = 0; i < index; i++) {
            temp = temp.next;
        }
        newNode.next = temp.next;
        newNode.prev=temp;
        temp.next.prev=newNode;
        temp.next = newNode;
        size++;
        return true;
    }
    public void remove(int index) {
        if(index < 0 || index >= size) {
            return;
        }
        Node temp = sentinel;
        for(int i = 0; i < index; i++) {
            temp = temp.next;
        }
        temp.next = temp.next.next;
        temp.next.prev=temp;
        size--;
    }
    public void remove(T data) {
        Node temp = sentinel.next;
        while(temp != sentinel) {
            if(temp.data.equals(data)) {
                temp.prev.next = temp.next;
                temp.next.prev=temp.prev;
                size--;
                return;
            }
            temp = temp.next;
        }
    }
    Node head(){
        if(isEmpty())
            return null;
        return sentinel.next;
    }
    Node tail(){
        if(isEmpty())
            return null;
        return sentinel.prev;
    }
    public static void main(String[] args) {
        LinkedList<Integer> l = new LinkedList<>();
        l.push_front(1);
        l.push_front(2);
        l.push_front(3);
        l.push_back(4);
        l.remove(Integer.valueOf(2));
        l.print();
    }
}
