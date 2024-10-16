import java.util.*;
class Solution {
    private boolean[] visit;
    private int[][] d;
    private int ans = 0; 
    public int solution(int k, int[][] dungeons) {
        // 정렬 후 pq써서 하려고 했는데 실패함..
        // 그냥 완탐 해보려고 함.
        visit = new boolean[dungeons.length];
        d = dungeons;
        dfs(k, 0);
        
        return ans;
    }
    
    private void dfs(int currentTired, int result){ 
        for (int i = 0; i < d.length; i++){
            if (!visit[i] && currentTired >= d[i][0]){
                visit[i] = true;
                dfs(currentTired - d[i][1], result + 1);
                visit[i] = false;
            }
        }
        
        ans = Math.max(ans, result);
        }
}