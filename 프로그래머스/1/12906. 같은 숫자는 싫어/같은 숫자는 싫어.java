import java.util.*;
import java.util.stream.*;
public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> items = new ArrayList<>();
        int beforeItem = -1;
        for (int i : arr){
            if (beforeItem != i){
                items.add(i);
                beforeItem = i;
            }
        }
        return items.stream().mapToInt(i -> (int)i).toArray();
        
    }
}