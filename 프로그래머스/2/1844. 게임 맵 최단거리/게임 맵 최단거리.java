import java.util.*;
class Solution {
    private int map[][];
    private int row;
    private int col;
    public int solution(int[][] maps) {
        int answer = 0;
        this.map = maps;
        this.row = map.length - 1;
        this.col = map[0].length - 1;
        bfs();
        if (map[row][col] == 1)
            return -1;
        return map[row][col];
        
    }
    
    void bfs(){
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0,0));
        int[] dRow = {0,1,0,-1};
        int[] dCol = {1,0,-1,0};
        while(!q.isEmpty()){
            Node node = q.poll();
            for (int i = 0; i < 4; i++){
                int newRow = node.row + dRow[i];
                int newCol = node.col + dCol[i];
                if (newRow < 0 || newCol < 0 || newRow > row || newCol > col)
                    continue;
                if (map[newRow][newCol] == 1){
                    q.add(new Node(newRow, newCol));
                    map[newRow][newCol] = map[node.row][node.col] + 1;
                }
            }
        }
    }
    
    public class Node{
        int row;
        int col;
        
        public Node(int row, int col){
            this.row = row;
            this.col = col;
        }
    }
}