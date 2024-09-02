import java.util.*;
public class Main{
	private static int n;
	private static int m;
	private static ArrayList<Integer> arr = new ArrayList<>();
	private static StringBuilder sb = new StringBuilder();
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();

		dfs(0);
		System.out.println(sb);

	}

	private static void dfs(int depth){
		if (depth == m)
		{
			for (int num : arr){
				sb.append(num).append(' ');
			}
			sb.append('\n');
		}
		else{
			for(int i=1; i<=n; i++){
				if (!arr.contains(i)){
					arr.add(i);
					dfs(depth + 1);
					arr.remove((Integer) i);
				}
			}
		}
	}
}