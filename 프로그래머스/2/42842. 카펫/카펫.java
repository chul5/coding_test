class Solution {
    public int[] solution(int brown, int yellow) {
        int sum = brown + yellow;
        int row = 1;
        int col = 1;
        for (int i = 2; i <= Math.sqrt(sum); i++){
            if (sum % i == 0){
                row = sum / i;
                if ((row-2)*(i-2) == yellow)
                    return new int[]{row,i};
            }
        }
        return null;
    }
}