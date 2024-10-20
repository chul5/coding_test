
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    private static final List<Integer> arr = new ArrayList<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int n = sc.nextInt();

        for (int i = 0; i < k; i++) {
            arr.add(sc.nextInt());
        }

        long left = 1;
        long right = arr.stream().max(Integer::compareTo).get();
        long maxLength = 0;

        while (left <= right) {
            long mid = (left + right) / 2;
            long sum = 0;

            for (int item : arr)
                sum += item / mid;

            if (sum >= n) {
                maxLength = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        System.out.println(maxLength);
    }
}
