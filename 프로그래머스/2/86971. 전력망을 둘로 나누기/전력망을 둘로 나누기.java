import java.util.*;
class Solution {
    private boolean[] visit;
    private int ans = 0;
    private int numberOfNode;
    private List<List<Integer>> graph;
    public int solution(int n, int[][] wires) {
        numberOfNode = n;
        ans = n;
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++){
            graph.add(new ArrayList<>());
        }
        for (int[] wire : wires){
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
        }
        
        for (int[] wire : wires){
            graph.get(wire[0]).remove(Integer.valueOf(wire[1]));
            graph.get(wire[1]).remove(Integer.valueOf(wire[0]));
            visit = new boolean[n+1];
            
            int count = dfs(wire[0]);
            ans = Math.min(ans, Math.abs(numberOfNode - 2 * count));
            
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
        }
        return ans;
    }
    
    private int dfs(int startNode){
        int count = 1;
        visit[startNode] = true;
        for (int nextNode : graph.get(startNode)){
            if (!visit[nextNode]){
                count += dfs(nextNode);
            }
        }
        return count;
        
    }
}