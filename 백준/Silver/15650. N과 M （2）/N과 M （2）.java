import java.util.Scanner;

public class Main {
	private static int n;
	private static int m;
	private static boolean[] visit;
	private static int[] arr;
//	private static ArrayList<Integer> arr = new ArrayList<>();
	private static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();

		arr = new int[m];
		visit = new boolean[n + 1];
		dfs(0, 0);
		System.out.println(sb.toString());
	}

	private static void dfs(int depth, int startIndex) {
		if (depth == m) {
			for (int item : arr) {
				sb.append(item).append(' ');
			}
			sb.append('\n');
		}
		else{
			for (int i = startIndex; i < n; i++) {
				if (!visit[i]){
					visit[i] = true;
					arr[depth] = i + 1;
					dfs(depth + 1, i);
					visit[i] = false;
				}
			}
		}
	}
}
