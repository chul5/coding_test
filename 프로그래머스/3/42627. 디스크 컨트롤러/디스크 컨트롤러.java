import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        // 1. 요청 시작 시간 기준으로 정렬
            // 1-1. 가장 빠른 요청 작업들 중 빠른 작업 실행 -> 우선순위큐
        Arrays.sort(jobs, (a, b) -> (a[0] - b[0]));
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        
        int currentTime=0;
        int totalTime=0;
        int jobTotalCount = jobs.length;
        int idx=0;
        
        while(idx < jobTotalCount || !pq.isEmpty()){
            // 도착한 job들을 큐에 넣어준다.
            while (idx < jobTotalCount && jobs[idx][0] <= currentTime){
                pq.offer(jobs[idx]);
                idx++;
            }
            if (!pq.isEmpty()){
                int[] job = pq.poll();
                currentTime += job[1];
                totalTime += currentTime - job[0];
            } else {
                currentTime = jobs[idx][0];
            }
        }//와일문 끝
        return totalTime/idx;
    }
}

// import java.util.*;

// class Solution {
//     public int solution(int[][] jobs) {
//         // 작업을 요청 시점 기준으로 정렬 (첫 번째 요소 기준으로 정렬)
//         Arrays.sort(jobs, (a, b) -> a[0] - b[0]);

//         // 우선순위 큐: 소요 시간을 기준으로 오름차순 정렬
//         PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);

//         int time = 0; // 현재 시간
//         int idx = 0;  // jobs 배열에서 처리할 작업의 인덱스
//         int total = 0; // 전체 요청부터 종료까지 걸린 시간 합계
//         int count = jobs.length; // 작업의 총 개수

//         // 모든 작업을 처리할 때까지 반복
//         while (idx < count || !pq.isEmpty()) {
//             // 현재 시간보다 이전에 도착한 작업들을 모두 우선순위 큐에 추가
//             while (idx < count && jobs[idx][0] <= time) {
//                 pq.offer(jobs[idx]);
//                 idx++;
//             }

//             // 큐에서 가장 소요 시간이 짧은 작업을 꺼내서 처리
//             if (!pq.isEmpty()) {
//                 int[] job = pq.poll();
//                 time += job[1]; // 작업 소요 시간만큼 시간 경과
//                 total += time - job[0]; // 요청부터 종료까지 걸린 시간 계산
//             } else {
//                 // 큐가 비어있는 경우, 다음 작업의 도착 시점으로 시간을 업데이트
//                 // 여기서 time을 다음 작업의 도착 시점으로 이동시켜야 함.
//                 time = jobs[idx][0];
//             }
//         }

//         // 평균 시간 계산
//         return total / count;
//     }
// }