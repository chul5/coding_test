import java.util.*;
class Solution {
    private boolean[] visit;
    private int[][] d;
    private List<Integer> arr = new ArrayList<>();
    
    public int solution(int k, int[][] dungeons) {
        // 정렬 후 pq써서 하려고 했는데 실패함..
        // 그냥 완탐 해보려고 함.
        visit = new boolean[dungeons.length];
        d = dungeons;
        dfs(0, k, 0);
        for(int i : arr)
            System.out.println(i);
        Collections.sort(arr, Collections.reverseOrder());
        
        return arr.get(0);
    }
    
    private void dfs(int depth, int currentTired, int result){ 
        if (depth == d.length){
            arr.add(result);
            return ;
        }
        else{
            for (int i = 0; i < d.length; i++){
                if (!visit[i]){
                    visit[i] = true;
                    if (currentTired >= d[i][0]){
                        dfs(depth + 1, currentTired - d[i][1], result + 1);
                    }
                    else
                        dfs(depth + 1, currentTired, result);
                    visit[i] = false;
                }
            }
        }
            
    }
}