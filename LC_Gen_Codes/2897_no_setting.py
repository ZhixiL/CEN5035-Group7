class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # Determine the length of the array
        n = len(nums)
        
        # Calculate the prefix sums of the array
        prefix_sums = [0] * (n+1)
        for i in range(1, n+1):
            prefix_sums[i] = prefix_sums[i-1] + nums[i-1]
        
        # Initialize the result variable
        result = 0
        
        # Iterate through all possible combinations of k elements
        for i in range(k, n+1):
            # Calculate the sum of squares for the current combination
            curr_sum = (prefix_sums[i] - prefix_sums[i-k]) % (10**9 + 7)
            curr_sum_sq = curr_sum * curr_sum % (10**9 + 7)
            
            # Update the result if necessary
            result = max(result, curr_sum_sq)
        
        return result