import java.util.*;
class Solution {
    private int length;
    private int[][] map;
    private int count=0;
    private int[] visit;
    public int solution(int n, int[][] computers) {
        length = n;
        visit = new int[n];
        map = computers;
        for (int i = 0; i<n; i++)
            if(dfs(i) == true)
                count++;
         
        return count;
    }
    
    boolean dfs(int computer){
        if (visit[computer] == 1)
            return false;
        // 방문시켜주기
        visit[computer] = 1;
        for(int i=0; i<length; i++){
            // 방문하지 않았고 연결되어 있다면
            if (visit[i] == 0 && map[computer][i] == 1){
                dfs(i);
            }
        }
        return true;
    }
        
    
    
}