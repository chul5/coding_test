import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
import javax.sound.sampled.Line;

public class Main {
    private static int[][] map;
    private static int n;
    private static int m;
    private static Node start;
    private static boolean[][] visit;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] nm = br.readLine().split(" ");
        n = Integer.parseInt(nm[0]);
        m = Integer.parseInt(nm[1]);
        map = new int[n][m];
        visit = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            int col = 0;
            for (String data : line) {
                map[i][col] = Integer.parseInt(data);
                if (map[i][col] == 2) {
                    start = new Node(i, col);
                }
                col++;
            }
        }

        bfs();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {

            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visit[i][j] && map[i][j] == 1) {
                    sb.append(-1).append(' ');
                } else {
                    sb.append(map[i][j]).append(' ');
                }
            }
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }
    private static void bfs() {
        Queue<Node> q = new LinkedList<>();
        q.add(start);
        map[start.row][start.col] = 0;
        visit[start.row][start.col] = true;

        int[] drow = {0, 1, 0, -1};
        int[] dcol = {1, 0, -1, 0};
        while (!q.isEmpty()) {
            Node node = q.poll();
            for (int i = 0; i < 4; i++) {
                int nr = drow[i] + node.row;
                int nc = dcol[i] + node.col;
                if (0 <= nr && nr < n && 0 <= nc && nc < m && map[nr][nc] != 0 && !visit[nr][nc]) {
                    visit[nr][nc] = true;
                    q.add(new Node(nr, nc));
                    map[nr][nc] = map[node.row][node.col] + 1;
                }
            }
        }
    }

    static class Node{
        int row;
        int col;

        public Node(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}
