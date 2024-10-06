import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        // 1.명함의 긴 쪽은 가로 짧은 쪽은 세로로 설정하기.
        int row = 0;
        int col = 0;
        for (int[] size : sizes){
            int width = Math.max(size[0], size[1]);
            int height = Math.min(size[0], size[1]);
            
            if (row < width)
                row = width;
            if (col < height)
                col = height;
        }
        
        return row*col;
    }
}