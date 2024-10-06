import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] arr1 = {1,2,3,4,5};
        int[] arr2 = {2,1,2,3,2,4,2,5};
        int[] arr3 = {3,3,1,1,2,2,4,4,5,5};
        int[] count = new int[3];
        for (int i = 0; i < answers.length; i++){
            if (answers[i] == arr1[i % arr1.length])
                count[0]++;
            if (answers[i] == arr2[i % arr2.length])
                count[1]++;
            if (answers[i] == arr3[i % arr3.length])
                count[2]++;
        }
        // count내의 정답을 맞춘 값들을 비교해야한다.
        int max = 0;
        for (int item : count){
            if (item > max)
                max = item;
        }
        int sameScore = 0;
        ArrayList<Integer> winner = new ArrayList<>();
        for (int i = 0; i<3; i++){
            if (max == count[i])
                winner.add(i + 1);
        }
        int[] answer = new int[winner.size()];
        for (int i = 0; i < winner.size(); i++){
            answer[i] = winner.get(i);
        }
            
        return answer;
    }
}