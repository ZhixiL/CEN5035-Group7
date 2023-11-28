class Solution {
    public int maxSum(int[] nums) {
        int max_sum = -1;
        
        // Loop through each pair of numbers
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                // Find the maximum digit in both numbers
                int max_digit = findMaxDigit(nums[i]);
                if (max_digit == findMaxDigit(nums[j])) {
                    // Calculate the sum and update max_sum if necessary
                    int pair_sum = nums[i] + nums[j];
                    max_sum = Math.max(max_sum, pair_sum);
                }
            }
        }
        
        return max_sum;
    }
    
    // Helper function to find the maximum digit in a number
    private int findMaxDigit(int num) {
        int max_digit = 0;
        while (num > 0) {
            int digit = num % 10;
            max_digit = Math.max(max_digit, digit);
            num /= 10;
        }
        return max_digit;
    }
}