

import java.rmi.dgc.VMID;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int left = 0;
        int right = n;
        int minValue = 0;

//        while (left <= right) {
//            int mid = (left + right) / 2;
//            int sum = 0;
//
//            sum = mid + dfs(mid);
//            System.out.println("mid = " + mid);
//            if (sum == n)
//                minValue = mid;
//            if (sum >= n) {
//                right = mid - 1;
//            } else {
//                left = mid + 1;
//            }
//        }
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum = i + dfs(i);
            if (sum == n) {
                minValue = i;
                break;
            }
        }
        System.out.println(minValue);
    }

    private static int dfs(int number) {
        if (number == 0)
            return 0;
        else {
            int result = number % 10;
            result += dfs(number / 10);
            return result;
        }
    }
}
