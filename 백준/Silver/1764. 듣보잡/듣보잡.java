import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Map;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws Exception{
        HashSet<String> noSee = new HashSet<>();
        PriorityQueue<String> noHear = new PriorityQueue<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] datas = br.readLine().split(" ");

        int n = Integer.parseInt(datas[0]);
        int m = Integer.parseInt(datas[1]);

        for (int i = 0; i < n; i++) {
            noSee.add(br.readLine());
        }

        for (int i = 0; i < m; i++) {
            String name = br.readLine();
            if (noSee.contains(name))
                noHear.add(name);
        }
        System.out.println(noHear.size());
        while (!noHear.isEmpty()) {
            System.out.println(noHear.poll());
        }
    }
}