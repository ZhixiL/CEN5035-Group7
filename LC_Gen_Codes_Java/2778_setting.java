class Solution {
    public int sumOfSquares(int[] nums) {
        int result = 0; // Initialize the result variable
        int n = nums.length; // Get the length of the array
        
        for (int i = 1; i <= n; i++) { // Iterate from 1 to n (inclusive)
            if (n % i == 0) { // Check if i divides n
                result += nums[i - 1] * nums[i - 1]; // Add the square of the special element to the result
            }
        }
        
        return result; // Return the final result
    }
}