import java.util.*;
class Solution {
    private int min = 0;
    private int minNext = 0;
    private int count = 0;
    public int solution(int[] scoville, int K) {
        
        // 배열 -> 우선순위큐 (최소힙)
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int item : scoville)
            pq.add(item);
        
        // while (poll() < K) 검증
            // poll() 2번 후 계산하고 add
        while (pq.size() >= 2 &&(min = pq.poll()) < K){
            count++;
            minNext = pq.poll();
            int newScoville = min + minNext * 2;
            pq.add(newScoville);
        }
        if(pq.size() > 0 && pq.poll() < K)
            return -1;
        return count;
    }
}