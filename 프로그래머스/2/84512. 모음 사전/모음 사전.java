import java.util.*;
class Solution {
    private char[] arr;
    private String word;
    private int answer = 1;
    private boolean flag = false;
    public int solution(String word) {
        arr = new char[]{'A','E', 'I', 'O', 'U'};
        this.word = word;
        dfs(0, "");
        return answer;
    }
    
    private void dfs(int depth, String current){
        if (depth == 5)
            return ;
        for (char item : arr){
            String line = current + item;
            if (line.equals(word))
                flag = true;
            if(!flag){
                answer++;
                dfs(depth + 1, line);
            }
        }
    }
}