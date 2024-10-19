

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine(); // 개행제거
        String line = sc.nextLine();
        int t = sc.nextInt();
        int p = sc.nextInt();

        int tSum = 0;
        for (String number : line.split(" ")) {
            int item = Integer.parseInt(number);
            if (item / t > 0)
                tSum += item / t;
            if (item % t == 0)
                continue;
            tSum++;
        }
        int quote = n / p;
        int rest = n % p;
        System.out.println(tSum);
        System.out.println(quote + " " + rest);
    }
}
