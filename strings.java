import java.util.Scanner;
public class StringManipulations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a text:");
        String text = scanner.nextLine();
        System.out.println("Original String: " + text);
        System.out.println("Length of the string: " + text.length());
        System.out.println("Substring from index 3: " + text.substring(3));
        System.out.println("Uppercase: " + text.toUpperCase());
        System.out.println("Lowercase: " + text.toLowerCase());
        System.out.println("Enter a sentence:");
        String sentence = scanner.nextLine();
        String[] words = sentence.split(" ");
        System.out.println("Words in the sentence:");
        for (String word : words) {
            System.out.println(word);
        }
        System.out.println("Enter the string to be replaced:");
        String oldString = scanner.nextLine();
        System.out.println("Enter the string to replace with:");
        String newString = scanner.nextLine();
        String replacedString = text.replace(oldString, newString);
        System.out.println("Replaced String: " + replacedString);
        System.out.println(String.format("Replaced '%s' with '%s'.", oldString, newString));
        scanner.close();
    }
}