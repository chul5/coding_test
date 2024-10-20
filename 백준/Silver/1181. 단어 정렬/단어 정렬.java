import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static List<String> arr = new ArrayList<>();
    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            if (!arr.contains(line))
                arr.add(line);
        }
        arr.sort((a,b) -> {
            if (a.length() != b.length())
                return a.length() - b.length();
            else
                return a.compareTo(b);
        });
        for (String word : arr) {
            System.out.println(word);
        }
    }
}