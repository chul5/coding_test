import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> set = new HashSet<>();
        HashSet<Integer> fullSet = new HashSet<>();
        for (int j = 1; j <= 20; j++) fullSet.add(j);

        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();

            if (cmd.equals("add")) {
                set.add(Integer.parseInt(st.nextToken()));
            } else if (cmd.equals("remove")) {
                set.remove(Integer.parseInt(st.nextToken()));
            } else if (cmd.equals("check")) {
                int num = Integer.parseInt(st.nextToken());
                sb.append(set.contains(num) ? 1 : 0).append("\n");
            } else if (cmd.equals("toggle")) {
                int num = Integer.parseInt(st.nextToken());
                if (set.contains(num)) {
                    set.remove(num);
                } else {
                    set.add(num);
                }
            } else if (cmd.equals("all")) {
                set = new HashSet<>(fullSet);
            } else if (cmd.equals("empty")) {
                set.clear();
            }
        }
        System.out.print(sb);
    }
}