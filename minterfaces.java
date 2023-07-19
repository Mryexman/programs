interface MyInterface1 {
    void method1();
}
interface MyInterface2 {
    void method2();
}
class MyClass implements MyInterface1, MyInterface2 {
    public void method1() {
        System.out.println("Method 1");
    }
    public void method2() {
        System.out.println("Method 2");
    }
}
public class MultipleInheritanceExample {
    public static void main(String[] args) {
        MyClass myObj = new MyClass();
        myObj.method1();
        myObj.method2();
    }
}
