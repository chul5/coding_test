class Solution {
    private int target;
    private int count = 0;
    public int solution(int[] numbers, int target) {
        int answer = 0;
        // 각 원소마다 + / - 둘 중에 하나를 결정해야한다.
        int sum = 0;
        this.target = target;
        dfs(sum, numbers, 0);
        return count;
    }
    private void dfs(int sum, int[] numbers, int depth){
        if (depth == numbers.length){
            if (sum == target)
                count++;
        }
        else{
            int number = numbers[depth];
            dfs(sum + number, numbers, depth + 1);
            dfs(sum - number, numbers, depth + 1);
        }
    }
    
}