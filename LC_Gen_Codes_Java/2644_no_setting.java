class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {
        int max_score = 0;
        int max_divisor = Integer.MAX_VALUE;
        
        for (int divisor : divisors) {
            int score = 0;
            for (int num : nums) {
                if (num % divisor == 0) {
                    score++;
                }
            }
            
            if (score >= max_score) {
                if (score > max_score || divisor < max_divisor) {
                    max_score = score;
                    max_divisor = divisor;
                }
            }
        }
        
        return max_divisor;
    }
}