class Solution {
    public int maxDivScore(List<Integer> nums, List<Integer> divisors) {
        int maxScore = 0;
        int maxDivisor = Integer.MAX_VALUE;

        for (int divisor : divisors) {
            int score = 0;
            for (int num : nums) {
                if (num % divisor == 0) {
                    score++;
                }
            }

            if (score >= maxScore) {
                if (score > maxScore || divisor < maxDivisor) {
                    maxScore = score;
                    maxDivisor = divisor;
                }
            }
        }

        return maxDivisor;
    }
}