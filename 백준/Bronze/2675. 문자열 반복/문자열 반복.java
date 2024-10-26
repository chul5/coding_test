import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String line = sc.nextLine();
            int repeatNumber = sc.nextInt();
            String data = sc.next();
            for (int j = 0; j < data.length(); j++) {
                for (int k = 0; k < repeatNumber; k++) {
                    sb.append(data.charAt(j));
                }
            }
            sb.append('\n');
        }
        System.out.println(sb.toString());

    }
}