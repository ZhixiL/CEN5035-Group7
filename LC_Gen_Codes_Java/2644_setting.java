class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {
        int[] score = new int[divisors.length]; // initialize score array with zeros
        for (int num : nums) {
            for (int i = 0; i < divisors.length; i++) {
                if (num % divisors[i] == 0) {
                    score[i] += 1; // increment the score if num is divisible by divisor
                }
            }
        }
        int max_score = Integer.MIN_VALUE;
        for (int s : score) {
            max_score = Math.max(max_score, s); // find the maximum score
        }
        List<Integer> max_score_divisors = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            if (score[i] == max_score) {
                max_score_divisors.add(divisors[i]);
            }
        }
        int min_divisor = Integer.MAX_VALUE;
        for (int divisor : max_score_divisors) {
            min_divisor = Math.min(min_divisor, divisor); // find the minimum of the divisors with maximum score
        }
        return min_divisor;
    }
}