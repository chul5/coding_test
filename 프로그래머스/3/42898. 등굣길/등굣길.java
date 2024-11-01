import java.util.*;
class Solution {
    private int[][] map;
    public int solution(int m, int n, int[][] puddles) {
        map = new int[n][m];
        map[0][0] = 1;
        
        for (int[] pool : puddles){
            int row = pool[1] - 1;
            int col = pool[0] - 1;
            map[row][col] = -1;
        }
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (map[i][j] == -1){
                    map[i][j] =0;
                    continue;
                }
                if (i > 0)
                    map[i][j] += map[i - 1][j];
                map[i][j] %= 1000000007;
                if (j > 0)
                    map[i][j] += map[i][j-1];
                map[i][j] %= 1000000007;
                
            }
        }
         
        int answer = 0;
        return map[n-1][m-1];
    }
}