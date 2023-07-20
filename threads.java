class MyThread extends Thread {
private String name;
public MyThread(String name) {
this.name = name;
}
public void run() {
for (int i = 1; i <= 5; i++) {
System.out.println("Thread " + name + ": " + i);
try {
Thread.sleep(1000);
} catch (InterruptedException e) {
e.printStackTrace();
}
}
}
}
public class Threads {
public static void main(String[] args) {
new MyThread("Thread 1").start();
new MyThread("Thread 2").start();
}
}