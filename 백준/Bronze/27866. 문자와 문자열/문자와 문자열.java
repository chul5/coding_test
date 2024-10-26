import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int n = sc.nextInt();
        System.out.println(line.charAt(n - 1));
    }
}