import java.io.*;
import java.util.*;
 
class stack<T> {
 
    ArrayList<T> A;
 
    int top = -1;
 
    int size;
 
    stack(int size)
    {
        this.size = size;
        this.A = new ArrayList<T>(size);
    }
 
    void push(T X)
    {
        if (top + 1 == size) {
         System.out.println("Stack Overflow");
        }
        else {
 
              top = top + 1;
 
            if (A.size() > top)
                A.set(top, X);
 
            else
 
                A.add(X);
        }
    }
    T top()
    {
        if (top == -1) {
 
            System.out.println("Stack Underflow");
            return null;
        }
 
        else
            return A.get(top);
    }
 
    void pop()
    {
        if (top == -1) {
 
            System.out.println("Stack Underflow");
        }
 
        else
 
            top--;
    }
 
    boolean empty() { return top == -1; }
 
    public String toString()
    {
 
        String Ans = "";
 
        for (int i = 0; i < top; i++) {
            Ans += String.valueOf(A.get(i)) + "->";
        }
 
        Ans += String.valueOf(A.get(top));
 
        return Ans;
    }
}

public class stackops {
 
    public static void main(String[] args)
    {
 
        stack<Integer> s1 = new stack<>(5);
 
        s1.push(10);
        s1.push(20);
        s1.push(30);
s1.push(40);
s1.push(50);
 
        System.out.println("s1 after pushing 10, 20,30,40 and 50 :\n" + s1);
 
        s1.pop();
 
        System.out.println("s1 after pop :\n" + s1);
 
        stack<String> s2 = new stack<>(5);
 
        s2.push("rama");
        s2.push("rahim");
        s2.push("john");
s2.push("lakshmi");
s2.push("megana");
 
        System.out.println("\ns2 after pushing 3 elements :\n" + s2);
 
        System.out.println("s2 after pushing 4th element :");
 
        s2.push("Sneha");
 
        stack<Float> s3 = new stack<>(2);
 
        s3.push(100.0f);
        s3.push(200.0f);
        System.out.println("\ns3 after pushing 2 elements :\n" + s3);
        System.out.println("top element of s3:\n"+ s3.top());
    }
}