import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        while (!line.equals("0 0 0")) {
            int[] numbers = new int[3];
            int i = 0;
            for (String item : line.split(" ")) {
                numbers[i] = Integer.parseInt(item);
                i++;
            }
            Arrays.sort(numbers);
            int bigValue = numbers[numbers.length-1];
            if (bigValue == (int) Math.sqrt(numbers[0] * numbers[0] + numbers[1] * numbers[1])) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
            line = br.readLine();
        }
    }
}
