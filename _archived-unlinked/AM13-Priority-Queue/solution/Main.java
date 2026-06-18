 
import java.util.PriorityQueue;
import java.util.Iterator;
  
public class Main{ 
  public static void main(String args[]){ 

    // 1) Creating a Priority Queue 
    PriorityQueue<String> pQueue = new PriorityQueue<>(); 

    // 2) Add
    pQueue.add("Python"); 
    pQueue.add("C"); 
    pQueue.add("C++"); 
    pQueue.add("Java"); 

    // 3) Peek 
    System.out.println("\nHead value using peek function: " + pQueue.peek()); 

    // 4) Iterator
    System.out.println("\nThe queue elements:"); 
    Iterator itr = pQueue.iterator(); 
    while(itr.hasNext()) {
      System.out.println(itr.next()); 
    }

    // 5) Poll
    pQueue.poll(); 
    System.out.println("\nAfter removing an element with poll function:"); 
    Iterator<String> itr2 = pQueue.iterator(); 
    while (itr2.hasNext()) {
        System.out.println(itr2.next()); 
    }

    // 6) Remove
    pQueue.remove("Java"); 
    System.out.println("\nAfter removing Java with remove function: "); 
    Iterator<String> itr3 = pQueue.iterator(); 
    while (itr3.hasNext()) {
        System.out.println(itr3.next()); 
    }

    // 7) Contains
    boolean b = pQueue.contains("C"); 
    System.out.println ("\nDoes the priority queue contain C? " + b); 

    // 8) ToArray 
    Object[] arr = pQueue.toArray(); 
    System.out.println ("\nValues in array: "); 
    for (int i = 0; i<arr.length; i++) {
      System.out.println("Value: " + arr[i].toString()); 
    }
  } 
} 